"""
CPZ Fitness — Carousel Template Engine
---------------------------------------
Fonts: Schibsted Grotesk (headlines), Inter (body/UI), Poppins (labels/data) —
embedded as base64 from fonts_b64.py. No network calls required. Fully
self-contained HTML output.

Rebuilt against skills/cpz-carousels/references/html-rendering-spec.md.
This file renders at a 420x525 canvas; export.py captures it at
device_scale_factor = 1080/420 (~2.571x) to produce the final 1080x1350 PNG.
Every pixel value below is the html-rendering-spec.md value divided by that
scale factor — see that file for the canonical 1080-canvas numbers.

Usage:
    from template import build_carousel
    html = build_carousel(slides, meta)
    Path("html/carousel.html").write_text(html, encoding="utf-8")

Slide dict keys:
    bg            : "dark" | "surface" | "light" | "gradient"
    tag           : str   — section label (small uppercase, top of slide)
    sub_label     : str   — optional secondary label below tag (e.g. exercise name)
    heading       : str   — main headline, sentence case (use \n for line breaks)
    heading_size  : int   — px at 420-canvas scale, default 40 (~104px at 1080 scale)
    subhead       : str   — optional subtitle
    body          : str   — optional body paragraph
    info_card     : dict  — {label, body} — bordered explanation card
    data_card     : dict  — {rows: [{label, value, kind}]} — kind: "positive"|"negative"|"accent"|None
    bullets       : list[dict]  — [{label, sub}]
    pills         : list[str]   — tag row; first is filled/primary, rest are outlined/muted
    stripe        : str   — word/phrase in orange filled block (headline accent)
    diag          : bool  — diagonal corner accent
    layout        : "top" | "bottom" | "center" — default "top" (spec's dominant rhythm; use
                    "bottom" for cover/hero slides with a background image behind the content)
    is_hook       : bool  — force-show logo badge (auto-shown on cover + light slides otherwise)
    is_cta        : bool  — centered CTA layout (overrides layout)

Meta dict keys:
    id, handle, brand, caption, cta_text
"""

from pathlib import Path


def _font_face_css():
    from fonts_b64 import (
        FONT_SCHIBSTED_GROTESK, FONT_INTER,
        FONT_POPPINS_REGULAR, FONT_POPPINS_MEDIUM,
    )
    return f"""@font-face {{
  font-family: 'Schibsted Grotesk';
  src: url('{FONT_SCHIBSTED_GROTESK}') format('truetype-variations');
  font-weight: 400 900; font-style: normal;
}}
@font-face {{
  font-family: 'Inter';
  src: url('{FONT_INTER}') format('truetype-variations');
  font-weight: 100 900; font-style: normal;
}}
@font-face {{
  font-family: 'Poppins';
  src: url('{FONT_POPPINS_REGULAR}') format('truetype');
  font-weight: 400; font-style: normal;
}}
@font-face {{
  font-family: 'Poppins';
  src: url('{FONT_POPPINS_MEDIUM}') format('truetype');
  font-weight: 500 600; font-style: normal;
}}"""
# Note: Poppins has no SemiBold(600) file on disk — the Medium(500) face is
# declared to also cover the 500-600 weight range as a pragmatic substitute.
# Source real Poppins-SemiBold.ttf in a future font pass to close this exactly.


LOGO_SVG_SMALL = """<svg width="16" height="13" viewBox="0 0 550 475" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(-78.267415,-21.49039)">
    <path d="m 280.3173,367.00474 -11,57.14209 h -130 l 13.65741,-56.71116 z" fill="#ff8c00"/>
    <path d="m 377.21318,185.90748 160.89493,-0.23992 -251.22463,60.1676 z" fill="#cc7000"/>
    <path d="m 178.13455,275.76734 350.43801,-1.27781 -30.85622,92.0717 -344.86781,1.37421 z" fill="#ff8c00"/>
    <path d="m 223.66334,94.15693 343.55419,-0.32298 -29.25972,91.99242 -338.29447,0.38108 z" fill="#ff8c00"/>
  </g>
</svg>"""

LOGO_SVG_WHITE = """<svg width="25" height="21" viewBox="0 0 550 475" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(-78.267415,-21.49039)">
    <path d="m 280.3173,367.00474 -11,57.14209 h -130 l 13.65741,-56.71116 z" fill="#fff"/>
    <path d="m 377.21318,185.90748 160.89493,-0.23992 -251.22463,60.1676 z" fill="rgba(255,255,255,0.6)"/>
    <path d="m 178.13455,275.76734 350.43801,-1.27781 -30.85622,92.0717 -344.86781,1.37421 z" fill="#fff"/>
    <path d="m 223.66334,94.15693 343.55419,-0.32298 -29.25972,91.99242 -338.29447,0.38108 z" fill="#fff"/>
  </g>
</svg>"""


BASE_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --bg-dark:   #1c1a17;
  --bg-card:   #2c2925;
  --bg-light:  #f5f3ef;
  --accent:    #ff8c00;
  --grad-start:#cc7000;
  --grad-mid:  #ff8c00;
  --grad-end:  #ffaa33;
  --text-dark: #f2ece2;
  --text-ink:  #1c1a17;
  --muted:     #9b948a;
  --font-h:     'Schibsted Grotesk', sans-serif;
  --font-b:     'Inter', sans-serif;
  --font-label: 'Poppins', sans-serif;
}
body { margin: 0; padding: 0; background: #fff; font-family: var(--font-b); }

.slide {
  width: 420px; height: 525px;
  position: relative; overflow: hidden;
  font-family: var(--font-b);
  flex-shrink: 0;
}
.bg-dark     { background: var(--bg-dark); }
.bg-surface  { background: var(--bg-card); }
.bg-light    { background: var(--bg-light); }
.bg-gradient {
  background: linear-gradient(155deg, var(--grad-start) 0%, var(--grad-mid) 50%, var(--grad-end) 100%);
  background-image:
    repeating-linear-gradient(-45deg, rgba(255,255,255,0.06) 0, rgba(255,255,255,0.06) 1px, transparent 1px, transparent 8px),
    linear-gradient(155deg, var(--grad-start) 0%, var(--grad-mid) 50%, var(--grad-end) 100%);
}

.slide-inner {
  position: absolute; inset: 0;
  display: flex; flex-direction: column;
  padding: 25px 34px 25px 25px;
  z-index: 2;
}
.layout-top    { justify-content: flex-start; padding-top: 60px; }
.layout-bottom { justify-content: flex-end; }
.layout-center { justify-content: center; align-items: flex-start; }
.layout-cta    { justify-content: center; align-items: center; text-align: center; padding: 25px 32px; }

/* Slide Number Watermark — oversized numeral, background texture */
.slide-number {
  position: absolute; top: -16px; right: -12px; z-index: 1;
  font-family: var(--font-h); font-weight: 700; font-size: 148px; line-height: 1;
  letter-spacing: -0.02em; user-select: none; pointer-events: none;
}
.on-dark    .slide-number { color: rgba(255,255,255,0.04); }
.on-surface .slide-number { color: rgba(255,255,255,0.04); }
.on-light   .slide-number { color: rgba(0,0,0,0.05); }
.on-grad    .slide-number { color: rgba(255,255,255,0.1); }

/* Section label + sub-label */
.tag { display: flex; align-items: center; gap: 7px; margin-bottom: 10px; }
.tag span {
  font-family: var(--font-label); font-size: 11px; font-weight: 600;
  letter-spacing: 0.15em; text-transform: uppercase;
}
.on-dark    .tag span, .on-surface .tag span { color: var(--muted); }
.on-light   .tag span { color: var(--accent); }
.on-grad    .tag span { color: rgba(255,255,255,0.7); }

.sub-label {
  font-family: var(--font-h); font-weight: 600; font-size: 12px;
  color: var(--accent); margin-bottom: 6px;
}

/* Headline */
.h1 {
  font-family: var(--font-h);
  font-weight: 700;
  font-size: 40px; line-height: 1.05;
  letter-spacing: -0.01em;
}
.on-dark  .h1, .on-surface .h1 { color: var(--text-dark); }
.on-light .h1 { color: var(--text-ink); }
.on-grad  .h1 { color: #fff; }

.stripe {
  display: inline-block;
  background: var(--accent);
  color: var(--text-ink);
  font-family: var(--font-h);
  font-weight: 700;
  font-size: 40px; line-height: 1.05;
  padding: 1px 8px 3px;
  margin-bottom: 6px;
}

.subhead { font-family: var(--font-b); font-size: 14px; font-weight: 400; line-height: 1.55; margin-top: 12px; }
.body    { font-family: var(--font-b); font-size: 14px; font-weight: 400; line-height: 1.6;  margin-top: 10px; }
.on-dark    .subhead, .on-dark    .body { color: var(--text-dark); opacity: 0.85; }
.on-surface .subhead, .on-surface .body { color: var(--text-dark); opacity: 0.85; }
.on-light   .subhead, .on-light   .body { color: rgba(28,26,23,0.7); }
.on-grad    .subhead, .on-grad    .body { color: rgba(255,255,255,0.9); }

/* Info Card */
.info-card {
  padding: 12px 14px;
  border-radius: 3px;
  border-left: 1.5px solid var(--accent);
  margin: 14px 0 8px;
}
.on-dark    .info-card, .on-surface .info-card { background: rgba(255,140,0,0.04); border: 1px solid rgba(255,140,0,0.25); border-left-width: 1.5px; }
.on-light   .info-card { background: rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.08); border-left-width: 1.5px; border-left-color: var(--accent); }
.info-card-label {
  font-family: var(--font-label); font-size: 8.5px; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.1em; color: var(--accent);
  margin-bottom: 4px;
}
.info-card-body { font-family: var(--font-b); font-size: 12px; line-height: 1.5; }
.on-dark    .info-card-body, .on-surface .info-card-body { color: #c8c5c0; }
.on-light   .info-card-body { color: #444; }

/* Data Card */
.data-card {
  background: var(--bg-card);
  border: 1px solid rgba(255,140,0,0.2);
  border-radius: 3px;
  padding: 14px;
  margin: 14px 0 8px;
}
.data-row {
  display: flex; align-items: baseline; justify-content: space-between;
  padding: 6px 0;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}
.data-row:last-child { border-bottom: none; }
.data-label { font-family: var(--font-label); font-size: 10px; color: var(--muted); }
.data-value { font-family: var(--font-h); font-weight: 700; font-size: 13px; }
.data-value.positive { color: #4ade80; }
.data-value.negative { color: #ff4444; }
.data-value.accent   { color: var(--accent); }
.data-value.neutral   { color: var(--text-dark); }

/* Bullets */
.bullet { display: flex; align-items: flex-start; gap: 10px; padding: 7px 0; border-bottom: 1px solid; }
.on-dark    .bullet, .on-surface .bullet { border-color: rgba(255,255,255,0.07); }
.on-light   .bullet { border-color: rgba(0,0,0,0.08); }
.on-grad    .bullet { border-color: rgba(255,255,255,0.15); }
.bullet-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--accent); flex-shrink: 0; margin-top: 4px; }
.bullet-label { font-family: var(--font-b); font-size: 13px; font-weight: 600; }
.bullet-sub   { font-family: var(--font-b); font-size: 11px; font-weight: 400; margin-top: 2px; line-height: 1.4; }
.on-dark    .bullet-label, .on-surface .bullet-label { color: var(--text-dark); }
.on-dark    .bullet-sub,   .on-surface .bullet-sub   { color: var(--muted); }
.on-light   .bullet-label { color: rgba(28,26,23,0.85); }
.on-light   .bullet-sub   { color: rgba(28,26,23,0.5); }
.on-grad    .bullet-label { color: rgba(255,255,255,0.95); }
.on-grad    .bullet-sub   { color: rgba(255,255,255,0.6); }

/* Pill Tags */
.pills { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }
.pill {
  font-family: var(--font-label); font-size: 9px; font-weight: 500;
  padding: 4px 8px; border-radius: 5.5px;
}
.pill-primary { background: var(--accent); color: var(--text-ink); }
.on-dark    .pill-muted, .on-surface .pill-muted { color: var(--muted); border: 1px solid rgba(255,255,255,0.2); }
.on-light   .pill-muted { color: #666; border: 1px solid rgba(0,0,0,0.15); }

/* Logo badge (top-left, cover + light slides) */
.logo-badge {
  position: absolute; top: 19px; left: 25px; z-index: 3;
  display: flex; align-items: center; gap: 8px;
}
.logo-circle {
  width: 28px; height: 28px; border-radius: 50%;
  background: #2a2a2a;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0; overflow: hidden;
}
.on-light .logo-circle { background: #333; }
.logo-handle { font-family: var(--font-b); font-size: 11px; font-weight: 500; }
.on-dark    .logo-handle, .on-surface .logo-handle, .on-grad .logo-handle { color: var(--muted); }
.on-light   .logo-handle { color: #555; }

/* CTA slide */
.cta-logo-circle {
  width: 47px; height: 47px; border-radius: 50%;
  background: rgba(0,0,0,0.3);
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 14px;
}
.cta-handle { font-family: var(--font-label); font-size: 11px; color: rgba(255,255,255,0.8); margin-bottom: 16px; }
.cta-glass {
  background: rgba(0,0,0,0.2);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  border-radius: 6px;
  padding: 14px 19px;
  margin-top: 18px;
  display: flex; flex-direction: column; align-items: center; gap: 6px;
}
.cta-glass-text { font-family: var(--font-b); font-weight: 500; font-size: 12px; color: #fff; text-align: center; }
.cta-glass-link { font-family: var(--font-label); font-size: 9px; color: rgba(255,255,255,0.6); }
.cta-website { font-family: var(--font-label); font-size: 9px; color: rgba(255,255,255,0.5); margin-top: 10px; }

.cta-btn {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 8px 16px;
  background: var(--bg-light);
  color: var(--text-ink);
  font-family: var(--font-b); font-weight: 700; font-size: 12px;
  border-radius: 5.5px; letter-spacing: 0.01em;
  margin-top: 12px;
}

/* Progress bar */
.progress {
  position: absolute; bottom: 0; left: 0; right: 0;
  padding: 6px 11px 9px;
  display: flex; align-items: center; gap: 8px; z-index: 10;
}
.p-track { flex: 1; height: 1.5px; border-radius: 1px; overflow: hidden; }
.p-fill  { height: 100%; border-radius: 1px; }
.on-dark    .p-track, .on-surface .p-track { background: rgba(255,255,255,0.1); }
.on-dark    .p-fill,  .on-surface .p-fill  { background: #fff; }
.on-dark    .p-label, .on-surface .p-label { color: rgba(255,255,255,0.4); }
.on-light   .p-track { background: rgba(0,0,0,0.1); }
.on-light   .p-fill  { background: var(--accent); }
.on-light   .p-label { color: rgba(0,0,0,0.3); }
.on-grad    .p-track { background: rgba(255,255,255,0.3); }
.on-grad    .p-fill  { background: #fff; }
.on-grad    .p-label { color: rgba(255,255,255,0.6); }
.p-label { font-family: var(--font-label); font-size: 9px; font-weight: 500; }

/* Swipe arrow */
.swipe {
  position: absolute; right: 12px; top: 50%; transform: translateY(-50%);
  width: 20px; height: 20px; border-radius: 50%;
  z-index: 9; display: flex; align-items: center; justify-content: center;
}
.on-dark    .swipe, .on-surface .swipe { background: rgba(255,255,255,0.06); }
.on-light   .swipe { background: rgba(0,0,0,0.04); }
.on-grad    .swipe { background: rgba(255,255,255,0.15); }

.diag { position: absolute; top: 0; right: 0; width: 47px; height: 47px; overflow: hidden; pointer-events: none; z-index: 1; }
"""


BASE_JS = """
const states = {};
const totals = {};

function goToSlide(cid, idx) {
  const track = document.getElementById('track-' + cid);
  const dots = document.getElementById('dots-' + cid).children;
  states[cid] = idx;
  track.style.transform = 'translateX(' + (-idx * 420) + 'px)';
  for (let i = 0; i < dots.length; i++) {
    dots[i].className = 'dot ' + (i === idx ? 'dot-active' : 'dot-inactive');
  }
}

let dragStart = null, dragCid = null;
function startDrag(e, cid) {
  dragStart = e.clientX; dragCid = cid;
  document.getElementById('track-' + cid).style.transition = 'none';
  document.addEventListener('mousemove', onDrag);
  document.addEventListener('mouseup', endDrag);
}
function onDrag(e) {
  if (dragStart === null) return;
  const base = -(states[dragCid] || 0) * 420;
  document.getElementById('track-' + dragCid).style.transform = 'translateX(' + (base + e.clientX - dragStart) + 'px)';
}
function endDrag(e) {
  document.removeEventListener('mousemove', onDrag);
  document.removeEventListener('mouseup', endDrag);
  const track = document.getElementById('track-' + dragCid);
  track.style.transition = 'transform 0.35s cubic-bezier(0.4,0,0.2,1)';
  const diff = e.clientX - dragStart;
  if (Math.abs(diff) > 50) {
    const dir = diff < 0 ? 1 : -1;
    const next = Math.max(0, Math.min((totals[dragCid] || 1) - 1, (states[dragCid] || 0) + dir));
    goToSlide(dragCid, next);
  } else {
    goToSlide(dragCid, states[dragCid] || 0);
  }
  dragStart = null;
}

let tStart = null, tCid = null;
function startTouch(e, cid) { tStart = e.touches[0].clientX; tCid = cid; }
document.addEventListener('touchmove', function(e) {
  if (tStart === null) return;
  const base = -(states[tCid] || 0) * 420;
  const track = document.getElementById('track-' + tCid);
  track.style.transform = 'translateX(' + (base + e.touches[0].clientX - tStart) + 'px)';
  track.style.transition = 'none';
});
document.addEventListener('touchend', function(e) {
  if (tStart === null) return;
  const diff = e.changedTouches[0].clientX - tStart;
  const track = document.getElementById('track-' + tCid);
  track.style.transition = 'transform 0.35s cubic-bezier(0.4,0,0.2,1)';
  if (Math.abs(diff) > 40) {
    const dir = diff < 0 ? 1 : -1;
    const next = Math.max(0, Math.min((totals[tCid] || 1) - 1, (states[tCid] || 0) + dir));
    goToSlide(tCid, next);
  } else { goToSlide(tCid, states[tCid] || 0); }
  tStart = null;
});
"""

IG_FRAME_CSS = """
.ig-frame {
  width: 420px; background: #fff;
  border-radius: 12px; border: 0.5px solid #e5e5e5;
  overflow: hidden; margin: 0 auto;
  font-family: var(--font-b);
}
.ig-header {
  display: flex; align-items: center; gap: 10px;
  padding: 10px 14px; border-bottom: 0.5px solid #e5e5e5;
}
.ig-avatar {
  width: 32px; height: 32px; border-radius: 50%;
  background: var(--bg-dark);
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.ig-handle { font-size: 12px; font-weight: 600; color: #111; }
.ig-sub    { font-size: 10px; color: #888; }
.carousel-viewport {
  width: 420px; height: 525px; overflow: hidden; position: relative; cursor: grab;
}
.carousel-viewport:active { cursor: grabbing; }
.carousel-track {
  display: flex; height: 100%;
  transition: transform 0.35s cubic-bezier(0.4,0,0.2,1);
}
.ig-dots { display: flex; justify-content: center; gap: 5px; padding: 10px 0 6px; }
.dot { width: 6px; height: 6px; border-radius: 50%; transition: all 0.25s; }
.dot-active   { background: var(--accent); transform: scale(1.15); }
.dot-inactive { background: #ddd; }
.ig-actions { display: flex; align-items: center; padding: 6px 14px 4px; gap: 14px; }
.ig-icon { opacity: 0.55; cursor: pointer; }
.ig-icon:hover { opacity: 0.85; }
.ig-bookmark { margin-left: auto; }
.ig-caption { padding: 4px 14px 12px; font-size: 12px; color: #555; line-height: 1.5; }
.ig-caption strong { color: #111; font-weight: 600; }
"""


def _bg_class(bg):
    return {
        "dark": "bg-dark on-dark",
        "surface": "bg-surface on-surface",
        "light": "bg-light on-light",
        "gradient": "bg-gradient on-grad",
    }[bg]


def _ctx(bg):
    return {"dark": "on-dark", "surface": "on-surface", "light": "on-light", "gradient": "on-grad"}[bg]


def render_slide(slide, index, total):
    bg      = slide.get("bg", "light")
    is_cta  = slide.get("is_cta", False)
    is_last = index == total - 1
    pct     = round((index + 1) / total * 100, 1)
    layout  = "layout-cta" if is_cta else ("layout-" + slide.get("layout", "top"))
    show_badge = (not is_cta) and (index == 0 or bg == "light" or slide.get("is_hook"))

    p = []

    # Slide number watermark (every non-CTA slide)
    if not is_cta:
        p.append(f'<div class="slide-number">{index + 1:02d}</div>')

    if slide.get("diag"):
        p.append('<div class="diag"><svg width="47" height="47" viewBox="0 0 47 47"><polygon points="47,0 47,47 0,0" fill="rgba(255,140,0,0.06)"/></svg></div>')

    if show_badge:
        handle_color_class = ""
        p.append(f'''<div class="logo-badge">
          <div class="logo-circle">{LOGO_SVG_SMALL}</div>
          <span class="logo-handle">{slide.get("handle","@philipz.fit")}</span>
        </div>''')

    p.append(f'<div class="slide-inner {layout}">')

    if is_cta:
        p.append(f'''<div class="cta-logo-circle">{LOGO_SVG_WHITE}</div>
        <div class="cta-handle">{slide.get("brand","CPZ Fitness")}</div>''')
        if slide.get("heading"):
            lines = slide["heading"].split("\n")
            size = slide.get("heading_size", 42)
            p.append(f'<div class="h1" style="font-size:{size}px;text-align:center;color:#fff">{"<br>".join(lines)}</div>')
        if slide.get("subhead"):
            p.append(f'<div class="subhead" style="text-align:center;color:rgba(255,255,255,0.9)">{slide["subhead"].replace(chr(10),"<br>")}</div>')
        p.append(f'<div class="cta-btn">{slide.get("cta_text","Follow @philipz.fit")} →</div>')
        p.append(f'''<div class="cta-glass">
          <div class="cta-glass-text">{slide.get("glass_text", slide.get("caption_line",""))}</div>
          <div class="cta-glass-link">{slide.get("handle","@philipz.fit")}</div>
        </div>
        <div class="cta-website">www.philipz.fit</div>''')
    else:
        if slide.get("tag"):
            p.append(f'<div class="tag"><span>{slide["tag"]}</span></div>')

        if slide.get("sub_label"):
            p.append(f'<div class="sub-label">{slide["sub_label"]}</div>')

        if slide.get("stripe"):
            p.append(f'<div class="stripe">{slide["stripe"]}</div>')

        if slide.get("heading"):
            lines = slide["heading"].split("\n")
            size  = slide.get("heading_size", 40)
            p.append(f'<div class="h1" style="font-size:{size}px">{"<br>".join(lines)}</div>')

        if slide.get("subhead"):
            p.append(f'<div class="subhead">{slide["subhead"]}</div>')
        if slide.get("body"):
            p.append(f'<div class="body">{slide["body"]}</div>')

        if slide.get("info_card"):
            ic = slide["info_card"]
            label_html = f'<div class="info-card-label">{ic["label"]}</div>' if ic.get("label") else ""
            p.append(f'<div class="info-card">{label_html}<div class="info-card-body">{ic["body"]}</div></div>')

        if slide.get("data_card"):
            rows_html = "".join(
                f'<div class="data-row"><span class="data-label">{r["label"]}</span>'
                f'<span class="data-value {r.get("kind","neutral")}">{r["value"]}</span></div>'
                for r in slide["data_card"]["rows"]
            )
            p.append(f'<div class="data-card">{rows_html}</div>')

        for i, b in enumerate(slide.get("bullets", [])):
            mt = ' style="margin-top:8px"' if i == 0 else ""
            sub_html = f'<div class="bullet-sub">{b["sub"]}</div>' if b.get("sub") else ""
            p.append(f'''<div class="bullet"{mt}>
              <div class="bullet-dot"></div>
              <div><div class="bullet-label">{b["label"]}</div>{sub_html}</div>
            </div>''')

        if slide.get("pills"):
            pill_html = "".join(
                f'<span class="pill {"pill-primary" if i == 0 else "pill-muted"}">{txt}</span>'
                for i, txt in enumerate(slide["pills"])
            )
            p.append(f'<div class="pills">{pill_html}</div>')

    p.append("</div>")  # close slide-inner

    if not is_last:
        p.append('''<div class="swipe">
          <svg width="8.5" height="8.5" viewBox="0 0 24 24" fill="none">
            <path d="M9 6l6 6-6 6" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>''')

    p.append(f'''<div class="progress">
      <div class="p-track"><div class="p-fill" style="width:{pct}%"></div></div>
      <span class="p-label">{index+1}/{total}</span>
    </div>''')

    return f'<div class="slide {_bg_class(bg)}">{"".join(p)}</div>'


def build_carousel(slides, meta):
    """Returns a fully self-contained HTML string for one carousel."""
    cid     = meta.get("id", "c1")
    handle  = meta.get("handle", "@philipz.fit")
    brand   = meta.get("brand", "CPZ Fitness")
    caption = meta.get("caption", "")
    total   = len(slides)

    slide_html = "\n".join(render_slide(s, i, total) for i, s in enumerate(slides))
    dots = "\n".join(
        f'<div class="dot {"dot-active" if i==0 else "dot-inactive"}"></div>'
        for i in range(total)
    )
    font_css = _font_face_css()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=420">
<title>{brand} — {cid}</title>
<style>
{font_css}
{BASE_CSS}
{IG_FRAME_CSS}
</style>
</head>
<body>
<div class="ig-frame">
  <div class="ig-header">
    <div class="ig-avatar">{LOGO_SVG_SMALL}</div>
    <div style="flex:1">
      <div class="ig-handle">{handle}</div>
      <div class="ig-sub">{brand}</div>
    </div>
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" style="opacity:0.3">
      <circle cx="12" cy="12" r="2" fill="#333"/>
      <circle cx="19" cy="12" r="2" fill="#333"/>
      <circle cx="5" cy="12" r="2" fill="#333"/>
    </svg>
  </div>
  <div class="carousel-viewport" id="vp-{cid}"
       onmousedown="startDrag(event,'{cid}')"
       ontouchstart="startTouch(event,'{cid}')">
    <div class="carousel-track" id="track-{cid}">
      {slide_html}
    </div>
  </div>
  <div class="ig-dots" id="dots-{cid}">{dots}</div>
  <div class="ig-actions">
    <svg class="ig-icon" width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke="#333" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <svg class="ig-icon" width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" stroke="#333" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <svg class="ig-icon" width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8M16 6l-4-4-4 4M12 2v13" stroke="#333" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <svg class="ig-icon ig-bookmark" width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" stroke="#333" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </div>
  <div class="ig-caption"><strong>{handle}</strong> {caption}</div>
</div>
<script>
{BASE_JS}
totals['{cid}'] = {total};
states['{cid}'] = 0;
</script>
</body>
</html>"""
