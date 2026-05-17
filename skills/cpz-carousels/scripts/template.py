"""
CPZ Fitness / Geek to Greek — Carousel Template Engine
-------------------------------------------------------
Fonts: Bebas Neue (headings) + Poppins (body) — embedded as base64 from fonts_b64.py
No network calls required. Fully self-contained HTML output.

Usage:
    from template import build_carousel
    html = build_carousel(slides, meta)
    Path("html/carousel.html").write_text(html, encoding="utf-8")

Slide dict keys:
    bg            : "light" | "dark" | "gradient"
    tag           : str   — small uppercase label
    heading       : str   — main headline (use \n for line breaks)
    heading_size  : int   — px, default 58
    subhead       : str   — optional subtitle
    body          : str   — optional body paragraph
    quote         : str   — optional pull-quote
    bullets       : list[dict]  — [{label, sub}]
    stripe        : str   — word/phrase in orange filled stripe
    ghost         : str   — giant faint background word
    diag          : bool  — diagonal corner accent
    layout        : "bottom" | "center"
    is_hook       : bool  — show logo lockup top-left
    is_cta        : bool  — centered CTA layout (overrides layout)

Meta dict keys:
    id, handle, brand, caption, cta_text
"""

from pathlib import Path


def _font_face_css():
    from fonts_b64 import (
        FONT_BEBAS,
        FONT_POPPINS_LIGHT, FONT_POPPINS_REGULAR,
        FONT_POPPINS_MEDIUM, FONT_POPPINS_SEMIBOLD, FONT_POPPINS_BOLD,
    )
    return f"""@font-face {{
  font-family: 'BebasNeue';
  src: url('{FONT_BEBAS}') format('truetype');
  font-weight: 400; font-style: normal;
}}
@font-face {{
  font-family: 'Poppins';
  src: url('{FONT_POPPINS_LIGHT}') format('truetype');
  font-weight: 300; font-style: normal;
}}
@font-face {{
  font-family: 'Poppins';
  src: url('{FONT_POPPINS_REGULAR}') format('truetype');
  font-weight: 400; font-style: normal;
}}
@font-face {{
  font-family: 'Poppins';
  src: url('{FONT_POPPINS_MEDIUM}') format('truetype');
  font-weight: 500; font-style: normal;
}}
@font-face {{
  font-family: 'Poppins';
  src: url('{FONT_POPPINS_SEMIBOLD}') format('truetype');
  font-weight: 600; font-style: normal;
}}
@font-face {{
  font-family: 'Poppins';
  src: url('{FONT_POPPINS_BOLD}') format('truetype');
  font-weight: 700; font-style: normal;
}}"""


LOGO_SVG_SMALL = """<svg width="20" height="17" viewBox="0 0 550 475" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(-78.267415,-21.49039)">
    <path d="m 280.3173,367.00474 -11,57.14209 h -130 l 13.65741,-56.71116 z" fill="#ff8200"/>
    <path d="m 377.21318,185.90748 160.89493,-0.23992 -251.22463,60.1676 z" fill="#9d5a00"/>
    <path d="m 178.13455,275.76734 350.43801,-1.27781 -30.85622,92.0717 -344.86781,1.37421 z" fill="#ff8200"/>
    <path d="m 223.66334,94.15693 343.55419,-0.32298 -29.25972,91.99242 -338.29447,0.38108 z" fill="#ff8200"/>
  </g>
</svg>"""

LOGO_SVG_LARGE = """<svg width="26" height="22" viewBox="0 0 550 475" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(-78.267415,-21.49039)">
    <path d="m 280.3173,367.00474 -11,57.14209 h -130 l 13.65741,-56.71116 z" fill="#fff"/>
    <path d="m 377.21318,185.90748 160.89493,-0.23992 -251.22463,60.1676 z" fill="rgba(255,255,255,0.55)"/>
    <path d="m 178.13455,275.76734 350.43801,-1.27781 -30.85622,92.0717 -344.86781,1.37421 z" fill="#fff"/>
    <path d="m 223.66334,94.15693 343.55419,-0.32298 -29.25972,91.99242 -338.29447,0.38108 z" fill="#fff"/>
  </g>
</svg>"""


BASE_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --primary: #ff8200;
  --vivid:   #ff9a00;
  --muted:   #b35a00;
  --deep:    #8c3d00;
  --light:   #FAF7F4;
  --border:  #EDE8E2;
  --dark:    #181614;
  --font-h:  'BebasNeue', sans-serif;
  --font-b:  'Poppins', sans-serif;
}
body { margin: 0; padding: 0; background: #fff; font-family: var(--font-b); }

.slide {
  width: 420px; height: 525px;
  position: relative; overflow: hidden;
  font-family: var(--font-b);
  flex-shrink: 0;
}
.bg-light    { background: var(--light); }
.bg-dark     { background: var(--dark); }
.bg-gradient { background: linear-gradient(155deg, var(--deep) 0%, var(--primary) 55%, var(--vivid) 100%); }

.slide-inner {
  position: absolute; inset: 0;
  display: flex; flex-direction: column;
  padding: 32px 36px 56px;
}
.layout-bottom { justify-content: flex-end; }
.layout-center { justify-content: center; align-items: flex-start; }
.layout-cta    { justify-content: center; align-items: center; text-align: center; }

.tag { display: flex; align-items: center; gap: 8px; margin-bottom: 14px; }
.tag-line { width: 14px; height: 1px; }
.tag span { font-size: 10px; font-weight: 600; letter-spacing: 2.5px; text-transform: uppercase; }
.on-dark  .tag-line { background: rgba(255,255,255,0.4); }
.on-dark  .tag span { color: rgba(255,255,255,0.55); }
.on-light .tag-line { background: var(--primary); opacity: 0.7; }
.on-light .tag span { color: var(--primary); }
.on-grad  .tag-line { background: rgba(255,255,255,0.4); }
.on-grad  .tag span { color: rgba(255,255,255,0.55); }

.h1 {
  font-family: var(--font-h);
  font-size: 58px; line-height: 0.92;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.on-dark  .h1 { color: #fff; }
.on-light .h1 { color: var(--dark); }
.on-grad  .h1 { color: #fff; }

.stripe {
  display: inline-block;
  background: var(--primary);
  color: var(--dark);
  font-family: var(--font-h);
  font-size: 58px; line-height: 0.92;
  padding: 2px 10px 4px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 6px;
}

.subhead { font-size: 14px; font-weight: 400; line-height: 1.55; margin-top: 14px; }
.body    { font-size: 14px; font-weight: 400; line-height: 1.6;  margin-top: 10px; }
.on-dark  .subhead, .on-dark  .body { color: rgba(255,255,255,0.7); }
.on-light .subhead, .on-light .body { color: rgba(24,22,20,0.65); }
.on-grad  .subhead, .on-grad  .body { color: rgba(255,255,255,0.85); }

.pull-quote {
  padding: 16px 18px;
  border-left: 3px solid var(--primary);
  border-radius: 0 8px 8px 0;
  margin: 18px 0 10px;
}
.on-dark  .pull-quote { background: rgba(255,255,255,0.04); }
.on-light .pull-quote { background: rgba(255,130,0,0.07); }
.on-grad  .pull-quote { background: rgba(255,255,255,0.1); }
.pull-quote p { font-size: 14px; font-style: italic; font-weight: 300; line-height: 1.55; }
.on-dark  .pull-quote p { color: rgba(255,255,255,0.85); }
.on-light .pull-quote p { color: rgba(24,22,20,0.8); }
.on-grad  .pull-quote p { color: rgba(255,255,255,0.9); }

.bullet { display: flex; align-items: flex-start; gap: 12px; padding: 9px 0; border-bottom: 1px solid; }
.on-dark  .bullet { border-color: rgba(255,255,255,0.07); }
.on-light .bullet { border-color: var(--border); }
.on-grad  .bullet { border-color: rgba(255,255,255,0.15); }
.bullet-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--primary); flex-shrink: 0; margin-top: 5px; }
.bullet-label { font-size: 13px; font-weight: 600; }
.bullet-sub   { font-size: 11px; font-weight: 400; margin-top: 2px; line-height: 1.4; }
.on-dark  .bullet-label { color: rgba(255,255,255,0.9); }
.on-dark  .bullet-sub   { color: rgba(255,255,255,0.45); }
.on-light .bullet-label { color: rgba(24,22,20,0.85); }
.on-light .bullet-sub   { color: rgba(24,22,20,0.5); }
.on-grad  .bullet-label { color: rgba(255,255,255,0.95); }
.on-grad  .bullet-sub   { color: rgba(255,255,255,0.6); }

.logo-lockup { display: flex; align-items: center; gap: 9px; margin-bottom: 20px; }
.logo-circle {
  width: 36px; height: 36px; border-radius: 50%;
  background: var(--dark);
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0; overflow: hidden;
}
.logo-circle-cta {
  width: 48px; height: 48px; border-radius: 50%;
  background: var(--primary);
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 6px;
}
.logo-name { font-size: 12px; font-weight: 600; letter-spacing: 0.5px; }
.on-dark  .logo-name, .on-grad .logo-name { color: rgba(255,255,255,0.9); }
.on-light .logo-name { color: var(--dark); }

.cta-btn {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 13px 28px;
  background: var(--light);
  color: var(--deep);
  font-family: var(--font-b); font-weight: 700; font-size: 14px;
  border-radius: 30px; letter-spacing: 0.2px;
  margin-top: 24px;
}
.cta-name { font-size: 14px; font-weight: 600; letter-spacing: 0.5px; color: rgba(255,255,255,0.9); margin-top: 4px; }

.progress {
  position: absolute; bottom: 0; left: 0; right: 0;
  padding: 12px 28px 18px;
  display: flex; align-items: center; gap: 10px; z-index: 10;
}
.p-track { flex: 1; height: 3px; border-radius: 2px; overflow: hidden; }
.p-fill  { height: 100%; border-radius: 2px; }
.on-dark  .p-track { background: rgba(255,255,255,0.12); }
.on-dark  .p-fill  { background: #fff; }
.on-dark  .p-label { color: rgba(255,255,255,0.4); }
.on-light .p-track { background: rgba(0,0,0,0.08); }
.on-light .p-fill  { background: var(--primary); }
.on-light .p-label { color: rgba(0,0,0,0.3); }
.on-grad  .p-track { background: rgba(255,255,255,0.2); }
.on-grad  .p-fill  { background: #fff; }
.on-grad  .p-label { color: rgba(255,255,255,0.5); }
.p-label { font-size: 10px; font-weight: 500; }

.swipe {
  position: absolute; right: 0; top: 0; bottom: 0; width: 46px;
  z-index: 9; display: flex; align-items: center; justify-content: center;
}
.diag { position: absolute; top: 0; right: 0; width: 120px; height: 120px; overflow: hidden; pointer-events: none; }
.ghost-bg {
  position: absolute; bottom: 40px; right: -20px;
  font-family: var(--font-h); font-size: 200px; line-height: 1;
  color: rgba(255,130,0,0.06); pointer-events: none; user-select: none;
  letter-spacing: -5px;
}
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
  background: var(--dark);
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
.dot-active   { background: var(--primary); transform: scale(1.15); }
.dot-inactive { background: #ddd; }
.ig-actions { display: flex; align-items: center; padding: 6px 14px 4px; gap: 14px; }
.ig-icon { opacity: 0.55; cursor: pointer; }
.ig-icon:hover { opacity: 0.85; }
.ig-bookmark { margin-left: auto; }
.ig-caption { padding: 4px 14px 12px; font-size: 12px; color: #555; line-height: 1.5; }
.ig-caption strong { color: #111; font-weight: 600; }
"""


def _bg_class(bg):
    return {"light": "bg-light on-light", "dark": "bg-dark on-dark", "gradient": "bg-gradient on-grad"}[bg]

def _ctx(bg):
    return {"light": "on-light", "dark": "on-dark", "gradient": "on-grad"}[bg]

def _arrow_stroke(bg):
    return {"light": "rgba(0,0,0,0.2)", "dark": "rgba(255,255,255,0.3)", "gradient": "rgba(255,255,255,0.35)"}[bg]


def render_slide(slide, index, total):
    bg      = slide.get("bg", "light")
    ctx     = _ctx(bg)
    is_cta  = slide.get("is_cta", False)
    is_hook = slide.get("is_hook", False)
    is_last = index == total - 1
    pct     = round((index + 1) / total * 100, 1)
    layout  = "layout-cta" if is_cta else ("layout-" + slide.get("layout", "bottom"))

    p = []

    if slide.get("ghost"):
        p.append(f'<div class="ghost-bg">{slide["ghost"]}</div>')
    if slide.get("diag"):
        p.append('<div class="diag"><svg width="120" height="120" viewBox="0 0 120 120"><polygon points="120,0 120,120 0,0" fill="rgba(255,130,0,0.06)"/></svg></div>')

    p.append(f'<div class="slide-inner {layout}">')

    if is_cta:
        p.append(f'''<div style="display:flex;flex-direction:column;align-items:center;margin-bottom:28px;">
          <div class="logo-circle-cta">{LOGO_SVG_LARGE}</div>
          <div class="cta-name">{slide.get("brand","Geek to Greek")}</div>
        </div>''')
        if slide.get("heading"):
            lines = slide["heading"].split("\n")
            p.append(f'<div class="h1" style="font-size:48px;text-align:center;line-height:0.96">{"<br>".join(lines)}</div>')
        if slide.get("subhead"):
            p.append(f'<div class="subhead" style="text-align:center;margin-top:14px">{slide["subhead"].replace(chr(10),"<br>")}</div>')
        p.append(f'<div class="cta-btn">{slide.get("cta_text","Follow @philipz.fit")} →</div>')
        p.append(f'''<div style="display:flex;flex-direction:column;align-items:center;gap:4px;margin-top:18px;">
          <span style="font-size:12px;font-weight:600;color:rgba(255,255,255,0.7);letter-spacing:0.5px;">{slide.get("handle","@philipz.fit")}</span>
          <span style="font-size:11px;font-weight:400;color:rgba(255,255,255,0.45);letter-spacing:0.3px;">www.philipz.fit</span>
        </div>''')
    else:
        if is_hook:
            name_color = "rgba(255,255,255,0.9)" if bg in ("dark","gradient") else "var(--dark)"
            p.append(f'''<div class="logo-lockup">
              <div class="logo-circle">{LOGO_SVG_SMALL}</div>
              <span class="logo-name" style="color:{name_color}">{slide.get("handle","@philipz.fit")}</span>
            </div>''')

        if slide.get("tag"):
            p.append(f'<div class="tag"><div class="tag-line"></div><span>{slide["tag"]}</span></div>')

        if slide.get("stripe"):
            p.append(f'<div class="stripe">{slide["stripe"]}</div>')

        if slide.get("heading"):
            lines = slide["heading"].split("\n")
            size  = slide.get("heading_size", 58)
            p.append(f'<div class="h1" style="font-size:{size}px">{"<br>".join(lines)}</div>')

        if slide.get("subhead"):
            p.append(f'<div class="subhead">{slide["subhead"]}</div>')
        if slide.get("body"):
            p.append(f'<div class="body" style="margin-top:14px">{slide["body"]}</div>')
        if slide.get("quote"):
            mt = "18" if not slide.get("body") else "16"
            p.append(f'<div class="pull-quote" style="margin-top:{mt}px"><p>{slide["quote"]}</p></div>')

        for i, b in enumerate(slide.get("bullets", [])):
            mt = ' style="margin-top:8px"' if i == 0 and not slide.get("quote") else ""
            sub_html = f'<div class="bullet-sub">{b["sub"]}</div>' if b.get("sub") else ""
            p.append(f'''<div class="bullet"{mt}>
              <div class="bullet-dot"></div>
              <div><div class="bullet-label">{b["label"]}</div>{sub_html}</div>
            </div>''')

    p.append("</div>")  # close slide-inner

    if not is_last:
        stroke = _arrow_stroke(bg)
        p.append(f'''<div class="swipe">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
            <path d="M9 6l6 6-6 6" stroke="{stroke}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
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
    brand   = meta.get("brand", "Geek to Greek")
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
