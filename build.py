import os, html
os.makedirs("assets", exist_ok=True)
FONT = "'Segoe UI', Inter, 'Helvetica Neue', Arial, sans-serif"
MONO = "'JetBrains Mono', 'Fira Code', Consolas, 'Courier New', monospace"

def banner(path, w, h, title, sub, title_size, sub_y_off):
    cy = h / 2 + title_size * 0.32 - (18 if sub else 0)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<style>
 .t{{font-family:{FONT};font-weight:800;}}
 .main{{opacity:0;animation:rise 1.2s cubic-bezier(.2,.8,.2,1) .2s forwards}}
 .g1{{animation:gl1 5s steps(1) infinite 2s;opacity:0}}
 .g2{{animation:gl2 5s steps(1) infinite 2s;opacity:0}}
 .sub{{opacity:0;animation:fade 1s ease 1.1s forwards}}
 @keyframes rise{{from{{opacity:0;transform:translateY(30px);letter-spacing:{title_size*0.45:.0f}px}}to{{opacity:1;transform:translateY(0);letter-spacing:{title_size*0.1:.0f}px}}}}
 @keyframes fade{{to{{opacity:1}}}}
 @keyframes gl1{{0%{{opacity:0}}92%{{opacity:.8;transform:translate(-5px,2px)}}94%{{opacity:.8;transform:translate(4px,-2px)}}96%{{opacity:0}}}}
 @keyframes gl2{{0%{{opacity:0}}92%{{opacity:.8;transform:translate(5px,-2px)}}94%{{opacity:.8;transform:translate(-4px,2px)}}96%{{opacity:0}}}}
</style>
<defs>
 <clipPath id="r"><rect width="{w}" height="{h}" rx="22"/></clipPath>
 <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#070b14"/><stop offset="1" stop-color="#150a26"/></linearGradient>
 <linearGradient id="tx" x1="0" y1="0" x2="1" y2="0" spreadMethod="reflect">
  <stop offset="0" stop-color="#22d3ee"/><stop offset=".5" stop-color="#a855f7"/><stop offset="1" stop-color="#f472b6"/>
  <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1 0;0 0" dur="6s" repeatCount="indefinite"/>
 </linearGradient>
 <pattern id="grid" width="44" height="44" patternUnits="userSpaceOnUse"><path d="M44 0H0V44" fill="none" stroke="#7c3aed" stroke-opacity=".18"/></pattern>
 <linearGradient id="fadeG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity=".9"/></linearGradient>
 <mask id="m"><rect width="{w}" height="{h}" fill="url(#fadeG)"/></mask>
 <filter id="blur"><feGaussianBlur stdDeviation="40"/></filter>
 <filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<g clip-path="url(#r)">
 <rect width="{w}" height="{h}" fill="url(#bg)"/>
 <g mask="url(#m)"><rect x="0" y="-44" width="{w}" height="{h+88}" fill="url(#grid)">
  <animateTransform attributeName="transform" type="translate" values="0 0;0 44" dur="2.5s" repeatCount="indefinite"/></rect></g>
 <g filter="url(#blur)" opacity=".55">
  <circle r="{h*0.45:.0f}" fill="#7c3aed"><animate attributeName="cx" values="{w*.15};{w*.35};{w*.15}" dur="12s" repeatCount="indefinite"/><animate attributeName="cy" values="{h*.3};{h*.8};{h*.3}" dur="10s" repeatCount="indefinite"/></circle>
  <circle r="{h*0.4:.0f}" fill="#0891b2"><animate attributeName="cx" values="{w*.85};{w*.6};{w*.85}" dur="14s" repeatCount="indefinite"/><animate attributeName="cy" values="{h*.7};{h*.2};{h*.7}" dur="11s" repeatCount="indefinite"/></circle>
  <circle r="{h*0.3:.0f}" fill="#db2777"><animate attributeName="cx" values="{w*.5};{w*.7};{w*.4};{w*.5}" dur="16s" repeatCount="indefinite"/><animate attributeName="cy" values="{h*.9};{h*.5};{h*.9}" dur="13s" repeatCount="indefinite"/></circle>
 </g>
 <rect width="{w}" height="2" fill="#22d3ee" opacity=".25"><animate attributeName="y" values="0;{h}" dur="4s" repeatCount="indefinite"/></rect>
 <g class="t" text-anchor="middle" font-size="{title_size}">
  <text class="g1" x="{w/2}" y="{cy:.0f}" fill="#22d3ee" letter-spacing="{title_size*0.1:.0f}">{html.escape(title)}</text>
  <text class="g2" x="{w/2}" y="{cy:.0f}" fill="#f472b6" letter-spacing="{title_size*0.1:.0f}">{html.escape(title)}</text>
  <g class="main"><text x="{w/2}" y="{cy:.0f}" fill="url(#tx)" filter="url(#glow)" letter-spacing="{title_size*0.1:.0f}">{html.escape(title)}</text></g>
 </g>
'''
    if sub:
        svg += f''' <text class="sub" x="{w/2}" y="{cy+sub_y_off:.0f}" text-anchor="middle" font-family="{MONO}" font-size="18" fill="#a5b4fc" letter-spacing="3">{html.escape(sub)}</text>\n'''
    svg += f''' <rect width="{w}" height="{h}" rx="22" fill="none" stroke="url(#tx)" stroke-opacity=".6" stroke-width="2"/>
</g></svg>'''
    open(path, "w").write(svg)

banner("assets/header.svg", 1200, 320, "VENKAT", "</>  FRONTEND DEVELOPER  ·  REACT  ·  TYPESCRIPT  ·  OPEN SOURCE", 120, 62)
banner("assets/footer.svg", 1200, 150, "Let's build something fast & beautiful", "", 40, 0)

# ---------------- Terminal ----------------
lines = [
  ("cmd", "whoami"),
  ("out", [("#e2e8f0", "Venkat"), ("#64748b", " — "), ("#22d3ee", "Frontend Developer"), ("#64748b", " · 3+ years")]),
  ("cmd", "cat stack.json"),
  ("out", [("#64748b", "{ "), ("#f472b6", "core"), ("#64748b", ": "), ("#a3e635", "[React, TypeScript, Redux]"), ("#64748b", ", "), ("#f472b6", "ui"), ("#64748b", ": "), ("#a3e635", "[Tailwind, MUI]"), ("#64748b", " }")]),
  ("cmd", "cat focus.txt"),
  ("out", [("#c4b5fd", "Performance optimization · Clean architecture · Scalable UI systems")]),
  ("cmd", "git log --open-source --oneline"),
  ("out", [("#fbbf24", "a1f3c9e "), ("#e2e8f0", "freeCodeCamp  "), ("#94a3b8", "feat: Facebook share · fix: mobile search UI · docs")]),
  ("out", [("#fbbf24", "7d02b4a "), ("#e2e8f0", "mdn/content   "), ("#94a3b8", "fix: Django docs · docs: content clarity")]),
  ("out", [("#fbbf24", "e95c118 "), ("#e2e8f0", "nodejs.org    "), ("#94a3b8", "docs: readability & command examples")]),
  ("cmd", "echo $CURRENTLY_LEARNING"),
  ("out", [("#22d3ee", "Frontend System Design")]),
]
W, LH, top = 1000, 30, 70
H = top + LH * (len(lines) + 1) + 20
CH = 10.2  # approx monospace char width at 17px
body, t = [], 0.6
for i, (kind, val) in enumerate(lines):
    y = top + i * LH
    if kind == "cmd":
        text = val
        width = (len("~ ❯ ") + len(text)) * CH + 10
        dur = max(0.5, len(text) * 0.05)
        body.append(f'''<clipPath id="c{i}"><rect x="40" y="{y-22}" height="30" width="{len('~ ❯ ')*CH+40}"><animate attributeName="width" from="{len('~ ❯ ')*CH+40}" to="{width+40}" begin="{t:.2f}s" dur="{dur:.2f}s" fill="freeze" calcMode="discrete" values="{';'.join(str(len('~ ❯ ')*CH+40 + k*CH) for k in range(len(text)+1))}"/></rect></clipPath>
<g opacity="0"><set attributeName="opacity" to="1" begin="{t-0.3:.2f}s" fill="freeze"/><text x="40" y="{y}" clip-path="url(#c{i})"><tspan fill="#a855f7">~</tspan><tspan fill="#22d3ee"> ❯ </tspan><tspan fill="#f8fafc">{html.escape(text)}</tspan></text></g>''')
        t += dur + 0.35
    else:
        spans = "".join(f'<tspan fill="{c}">{html.escape(s)}</tspan>' for c, s in val)
        body.append(f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{t:.2f}s" dur=".25s" fill="freeze"/><text x="40" y="{y}">{spans}</text></g>')
        t += 0.25
cy = top + len(lines) * LH
body.append(f'''<g opacity="0"><set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/><text x="40" y="{cy}"><tspan fill="#a855f7">~</tspan><tspan fill="#22d3ee"> ❯ </tspan></text>
<rect x="{40+len('~ ❯ ')*CH+4}" y="{cy-17}" width="10" height="21" fill="#22d3ee"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect></g>''')

term = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
 <linearGradient id="bd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22d3ee"/><stop offset=".5" stop-color="#a855f7"/><stop offset="1" stop-color="#f472b6"/></linearGradient>
</defs>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16" fill="#0a0e17" stroke="url(#bd)" stroke-width="2"/>
<path d="M1 17a16 16 0 0 1 16-16h{W-34}a16 16 0 0 1 16 16v25H1z" fill="#111827"/>
<circle cx="28" cy="22" r="7" fill="#ff5f57"/><circle cx="52" cy="22" r="7" fill="#febc2e"/><circle cx="76" cy="22" r="7" fill="#28c840"/>
<text x="{W/2}" y="27" text-anchor="middle" font-family="{MONO}" font-size="14" fill="#64748b">venkat@github: ~/profile</text>
<g font-family="{MONO}" font-size="17">
{chr(10).join(body)}
</g></svg>'''
open("assets/terminal.svg", "w").write(term)

# ---------------- Tech marquee ----------------
techs = ["React", "TypeScript", "JavaScript", "Redux", "Tailwind CSS", "Material UI", "HTML5", "CSS3", "Node.js", "Jest", "Git", "Figma", "Postman", "Vite"]
colors = ["#22d3ee", "#a855f7", "#f472b6", "#a3e635", "#fbbf24"]
x, pills = 0, []
for i, name in enumerate(techs):
    pw = len(name) * 11.2 + 50
    c = colors[i % len(colors)]
    pills.append(f'<g transform="translate({x:.0f},12)"><rect width="{pw:.0f}" height="40" rx="20" fill="#0f1422" stroke="{c}" stroke-opacity=".7"/><circle cx="20" cy="20" r="5" fill="{c}"/><text x="34" y="26" font-family="{FONT}" font-size="17" font-weight="600" fill="#e2e8f0">{name}</text></g>')
    x += pw + 16
row = "".join(pills)
mq = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="64" viewBox="0 0 1200 64">
<defs><linearGradient id="f" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".08" stop-color="#fff"/><stop offset=".92" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient><mask id="m"><rect width="1200" height="64" fill="url(#f)"/></mask></defs>
<g mask="url(#m)"><g><g>{row}</g><g transform="translate({x:.0f},0)">{row}</g>
<animateTransform attributeName="transform" type="translate" values="0 0;-{x:.0f} 0" dur="28s" repeatCount="indefinite"/></g></g></svg>'''
open("assets/tech-marquee.svg", "w").write(mq)

# ---------------- OSS cards ----------------
def card(path, name, accent, prs, items):
    w, h = 390, 210
    per = 2 * (w - 4) + 2 * (h - 4)
    its = "".join(f'<text x="24" y="{108 + k*26}" font-family="{FONT}" font-size="15" fill="#cbd5e1"><tspan fill="{accent}">▸ </tspan>{html.escape(s)}</text>' for k, s in enumerate(items))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs><radialGradient id="g" cx="1" cy="0" r="1"><stop offset="0" stop-color="{accent}" stop-opacity=".28"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient></defs>
<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="18" fill="#0a0e17" stroke="#1e293b" stroke-width="2"/>
<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="18" fill="url(#g)"/>
<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="18" fill="none" stroke="{accent}" stroke-width="3" stroke-linecap="round" stroke-dasharray="140 {per-140:.0f}">
 <animate attributeName="stroke-dashoffset" from="0" to="-{per:.0f}" dur="4s" repeatCount="indefinite"/></rect>
<circle cx="32" cy="40" r="7" fill="{accent}"><animate attributeName="r" values="6;9;6" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;.5;1" dur="2s" repeatCount="indefinite"/></circle>
<text x="50" y="47" font-family="{FONT}" font-size="22" font-weight="800" fill="#f8fafc">{html.escape(name)}</text>
<text x="24" y="78" font-family="{MONO}" font-size="13" fill="{accent}">{prs} PULL REQUEST{"S" if prs > 1 else ""}</text>
{its}
</svg>'''
    open(path, "w").write(svg)

card("assets/oss-freecodecamp.svg", "freeCodeCamp", "#a3e635", 3, ["Facebook share feature", "Mobile search placeholder fix", "Documentation improvements"])
card("assets/oss-mdn.svg", "MDN Web Docs", "#22d3ee", 2, ["Fixed Django documentation", "Improved content clarity"])
card("assets/oss-nodejs.svg", "Node.js Website", "#f472b6", 1, ["Docs readability", "Formatting & command examples"])
print("ok")
