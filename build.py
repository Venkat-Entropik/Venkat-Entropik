"""
build.py — Award-Winning GitHub Profile Asset Generator v2.0
Generates all SVG assets for Venkat's GitHub profile README.
Run: python3 build.py
"""

import os, html, math
os.makedirs("assets", exist_ok=True)

FONT = "'Segoe UI', Inter, 'Helvetica Neue', Arial, sans-serif"
MONO = "'JetBrains Mono', 'Fira Code', Consolas, 'Courier New', monospace"

# ─── DESIGN TOKENS ──────────────────────────────────────────────────────────
CYAN   = "#22d3ee"
PURPLE = "#a855f7"
PINK   = "#f472b6"
GREEN  = "#4ade80"
AMBER  = "#fbbf24"
INDIGO = "#818cf8"
BG     = "#060a12"
BORDER = "#1e2d3d"


# ════════════════════════════════════════════════════════════════════════════
# SHARED DEFS (reused across SVGs)
# ════════════════════════════════════════════════════════════════════════════
def shared_defs(W, H, extra=""):
    return f"""<defs>
  <!-- Dark bg gradient -->
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0"   stop-color="#020408"/>
    <stop offset="0.5" stop-color="#0a0618"/>
    <stop offset="1"   stop-color="#060d1a"/>
  </linearGradient>

  <!-- Animated gradient text fill -->
  <linearGradient id="gtext" x1="0%" y1="0%" x2="100%" y2="0%" gradientUnits="userSpaceOnUse" x2="{W}">
    <stop offset="0%"   stop-color="{CYAN}">
      <animate attributeName="stop-color" values="{CYAN};{PURPLE};{PINK};{CYAN}" dur="5s" repeatCount="indefinite"/>
    </stop>
    <stop offset="50%"  stop-color="{PURPLE}">
      <animate attributeName="stop-color" values="{PURPLE};{PINK};{CYAN};{PURPLE}" dur="5s" repeatCount="indefinite"/>
    </stop>
    <stop offset="100%" stop-color="{PINK}">
      <animate attributeName="stop-color" values="{PINK};{CYAN};{PURPLE};{PINK}" dur="5s" repeatCount="indefinite"/>
    </stop>
  </linearGradient>

  <!-- Animated border gradient -->
  <linearGradient id="borderG" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%"   stop-color="{CYAN}"   stop-opacity="0.9">
      <animate attributeName="stop-color" values="{CYAN};{PURPLE};{PINK};{CYAN}" dur="6s" repeatCount="indefinite"/>
    </stop>
    <stop offset="100%" stop-color="{PINK}"   stop-opacity="0.9">
      <animate attributeName="stop-color" values="{PINK};{CYAN};{PURPLE};{PINK}" dur="6s" repeatCount="indefinite"/>
    </stop>
  </linearGradient>

  <!-- Atmospheric blur -->
  <filter id="atmos" x="-60%" y="-60%" width="220%" height="220%">
    <feGaussianBlur stdDeviation="55"/>
  </filter>

  <!-- Glow: large -->
  <filter id="glow-lg" x="-30%" y="-80%" width="160%" height="260%">
    <feGaussianBlur stdDeviation="14" result="b1"/>
    <feGaussianBlur stdDeviation="5"  result="b2"/>
    <feMerge><feMergeNode in="b1"/><feMergeNode in="b2"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>

  <!-- Glow: small -->
  <filter id="glow-sm" x="-20%" y="-60%" width="140%" height="220%">
    <feGaussianBlur stdDeviation="4" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>

  <!-- Grid pattern -->
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="rgba(99,102,241,0.10)" stroke-width="0.5"/>
  </pattern>

  <!-- Grid fade mask (top bright → bottom fade) -->
  <linearGradient id="gridFade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"   stop-color="#fff"/>
    <stop offset="0.6" stop-color="#fff" stop-opacity="0.5"/>
    <stop offset="1"   stop-color="#fff" stop-opacity="0"/>
  </linearGradient>
  <mask id="gridMask">
    <rect width="{W}" height="{H}" fill="url(#gridFade)"/>
  </mask>

  <!-- Scanlines -->
  <pattern id="scan" width="1" height="3" patternUnits="userSpaceOnUse">
    <rect width="1" height="1" y="0" fill="rgba(34,211,238,0.025)"/>
  </pattern>

  <!-- Edge fade mask for marquee -->
  <linearGradient id="edgeFade" x1="0" x2="1">
    <stop offset="0"    stop-color="#060a12"/>
    <stop offset="0.08" stop-color="#060a12" stop-opacity="0"/>
    <stop offset="0.92" stop-color="#060a12" stop-opacity="0"/>
    <stop offset="1"    stop-color="#060a12"/>
  </linearGradient>

  <!-- Clip rounded rect -->
  <clipPath id="rr"><rect width="{W}" height="{H}" rx="20"/></clipPath>

  {extra}
</defs>"""


# ════════════════════════════════════════════════════════════════════════════
# 1. HEADER — Holographic Hero Banner
# ════════════════════════════════════════════════════════════════════════════
def make_header():
    W, H = 1200, 340

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{shared_defs(W, H)}

<g clip-path="url(#rr)">
  <!-- Base background -->
  <rect width="{W}" height="{H}" fill="url(#bg)"/>

  <!-- Aurora blobs -->
  <g filter="url(#atmos)" opacity="0.75">
    <circle r="190" fill="#4f07b4" opacity="0.9">
      <animate attributeName="cx" values="180;360;170;180" dur="18s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="90;230;290;90"  dur="14s" repeatCount="indefinite"/>
    </circle>
    <circle r="170" fill="#0e5f8a" opacity="0.8">
      <animate attributeName="cx" values="1060;880;1010;1060" dur="16s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="75;210;110;75"      dur="12s" repeatCount="indefinite"/>
    </circle>
    <circle r="140" fill="#831843" opacity="0.65">
      <animate attributeName="cx" values="610;720;490;610" dur="20s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="290;150;330;290" dur="15s" repeatCount="indefinite"/>
    </circle>
    <circle r="100" fill="#064e3b" opacity="0.45">
      <animate attributeName="cx" values="400;620;350;400" dur="22s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="330;190;80;330"  dur="17s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Grid -->
  <rect width="{W}" height="{H}" fill="url(#grid)" mask="url(#gridMask)"/>

  <!-- Scanlines -->
  <rect width="{W}" height="{H}" fill="url(#scan)" opacity="0.7"/>

  <!-- Horizontal scan beam -->
  <rect width="{W}" height="1.5" fill="white" opacity="0">
    <animate attributeName="y"       values="-2;{H+2}"    dur="5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0;0.25;0.25;0" keyTimes="0;0.05;0.95;1" dur="5s" repeatCount="indefinite"/>
  </rect>

  <!-- HUD corner brackets -->
  <g stroke-width="1.8" fill="none" opacity="0.75">
    <path d="M22,22 L62,22 M22,22 L22,62"  stroke="{CYAN}"/>
    <path d="M{W-22},22 L{W-62},22 M{W-22},22 L{W-22},62" stroke="{PINK}"/>
    <path d="M22,{H-22} L62,{H-22} M22,{H-22} L22,{H-62}" stroke="{PURPLE}"/>
    <path d="M{W-22},{H-22} L{W-62},{H-22} M{W-22},{H-22} L{W-22},{H-62}" stroke="{AMBER}"/>
  </g>

  <!-- Floating orbs -->
  <circle cx="100" cy="55" r="3" fill="{CYAN}">
    <animate attributeName="opacity" values="0.9;0.2;0.9" dur="2.8s" repeatCount="indefinite"/>
    <animate attributeName="r"       values="3;5.5;3"     dur="2.8s" repeatCount="indefinite"/>
  </circle>
  <circle cx="1100" cy="75" r="2.5" fill="{PINK}">
    <animate attributeName="opacity" values="0.8;0.15;0.8" dur="3.2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="55" cy="285" r="2.5" fill="{PURPLE}">
    <animate attributeName="opacity" values="0.8;0.25;0.8" dur="4.0s" repeatCount="indefinite"/>
  </circle>
  <circle cx="1145" cy="270" r="3" fill="{GREEN}">
    <animate attributeName="opacity" values="0.7;0.1;0.7" dur="3.5s" repeatCount="indefinite"/>
  </circle>

  <!-- HUD data fragments -->
  <g font-family="{MONO}" font-size="10" fill="{CYAN}" opacity="0.28">
    <text x="35" y="52">SYS:ONLINE</text>
    <text x="35" y="65">BUILD:3.0</text>
    <text x="{W-95}" y="52">FE_DEV</text>
    <text x="{W-95}" y="65">ORG:ETP</text>
  </g>

  <!-- Glitch cyan layer -->
  <g opacity="0">
    <animate attributeName="opacity"
      values="0;0;0;0;0;0;0;0;0;0.55;0;0.35;0;0;0;0;0;0;0;0"
      dur="8s" repeatCount="indefinite"/>
    <text x="600" y="192" text-anchor="middle"
      font-family="{FONT}" font-weight="900" font-size="110"
      fill="none" stroke="{CYAN}" stroke-width="0.6"
      letter-spacing="16" transform="translate(-4,0)">VENKAT</text>
  </g>

  <!-- Glitch pink layer -->
  <g opacity="0">
    <animate attributeName="opacity"
      values="0;0;0;0;0;0;0;0;0;0;0;0.45;0;0.25;0;0;0;0;0;0"
      dur="8s" repeatCount="indefinite"/>
    <text x="600" y="192" text-anchor="middle"
      font-family="{FONT}" font-weight="900" font-size="110"
      fill="none" stroke="{PINK}" stroke-width="0.6"
      letter-spacing="16" transform="translate(4,0)">VENKAT</text>
  </g>

  <!-- Hero name (animated in) -->
  <g opacity="0">
    <animate attributeName="opacity" from="0" to="1"
      dur="1.2s" begin="0.1s" fill="freeze"
      calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
    <text x="600" y="192" text-anchor="middle"
      font-family="{FONT}" font-weight="900" font-size="110"
      fill="url(#gtext)" filter="url(#glow-lg)" letter-spacing="16">
      <animateTransform attributeName="transform" type="translate"
        from="0 32" to="0 0" dur="1.2s" begin="0.1s" fill="freeze"
        calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
      VENKAT
    </text>
  </g>

  <!-- Role tagline -->
  <g opacity="0">
    <animate attributeName="opacity" from="0" to="1"
      dur="0.8s" begin="1.0s" fill="freeze"/>
    <text x="600" y="244" text-anchor="middle"
      font-family="{MONO}" font-size="17" fill="{INDIGO}" letter-spacing="4">
      &lt;/&gt;  FRONTEND DEVELOPER  ·  REACT  ·  TYPESCRIPT  ·  OPEN SOURCE
    </text>
  </g>

  <!-- "Open to work" pulse badge -->
  <g opacity="0">
    <animate attributeName="opacity" from="0" to="1"
      dur="0.6s" begin="1.6s" fill="freeze"/>
    <g transform="translate(490,274)">
      <rect width="220" height="32" rx="16"
        fill="rgba(74,222,128,0.07)"
        stroke="{GREEN}" stroke-width="1" stroke-opacity="0.65"/>
      <!-- Pulse ring -->
      <circle cx="18" cy="16" r="5" fill="{GREEN}" opacity="0.25">
        <animate attributeName="r"       values="5;13;5"   dur="2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.25;0;0.25" dur="2s" repeatCount="indefinite"/>
      </circle>
      <!-- Solid dot -->
      <circle cx="18" cy="16" r="5" fill="{GREEN}">
        <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="34" y="21" font-family="{MONO}" font-size="12.5"
        fill="{GREEN}" letter-spacing="1">OPEN TO OPPORTUNITIES</text>
    </g>
  </g>

  <!-- Border frame -->
  <rect width="{W}" height="{H}" rx="20"
    fill="none" stroke="url(#borderG)" stroke-width="1.5" opacity="0.9"/>
</g>
</svg>"""
    open("assets/header.svg", "w").write(svg)
    print("✓ assets/header.svg")


# ════════════════════════════════════════════════════════════════════════════
# 2. TERMINAL — Typewriter animated terminal
# ════════════════════════════════════════════════════════════════════════════
def make_terminal():
    lines = [
        ("cmd", "whoami"),
        ("out", [("#e2e8f0", "Venkat"), ("#64748b", "  —  "), (CYAN, "Frontend Developer"), ("#64748b", "  ·  3+ yrs @ Entropik")]),
        ("cmd", "cat stack.json"),
        ("out", [(PINK, '"core"'), ("#94a3b8", " : "), ("#a3e635", '["React 18", "TypeScript", "Redux Toolkit"]')]),
        ("out", [(PINK, '"ui"'),   ("#94a3b8", "   : "), ("#a3e635", '["Tailwind CSS", "Material UI", "Framer Motion"]')]),
        ("out", [(PINK, '"test"'), ("#94a3b8", " : "), ("#a3e635", '["Jest", "React Testing Library", "Playwright"]')]),
        ("cmd", "cat philosophy.txt"),
        ("out", [("#c4b5fd", "Clean code  ·  Performance-first  ·  Pixel-perfect  ·  DX matters")]),
        ("cmd", "git log --oss --oneline"),
        ("out", [(AMBER, "a1f3c9e "), ("#e2e8f0", "freeCodeCamp   "), ("#64748b", "3 PRs merged ✓")]),
        ("out", [(AMBER, "7d02b4a "), ("#e2e8f0", "mdn/content    "), ("#64748b", "2 PRs merged ✓")]),
        ("out", [(AMBER, "e95c118 "), ("#e2e8f0", "nodejs.org     "), ("#64748b", "1 PR  merged ✓")]),
        ("cmd", "echo $CURRENTLY_BUILDING"),
        ("out", [(GREEN, "Scalable, accessible, blazing-fast React applications 🚀")]),
    ]

    W, LH, TOP = 1000, 32, 72
    H = TOP + LH * (len(lines) + 1) + 32
    CH = 10.45  # approx char width at 17px mono
    body, t = [], 0.5

    for i, (kind, val) in enumerate(lines):
        y = TOP + i * LH
        if kind == "cmd":
            text = val
            prompt = "~/profile ❯ "
            pw = len(prompt) * CH
            fw = pw + len(text) * CH + 16
            dur = max(0.35, len(text) * 0.045)
            steps = ";".join(str(int(pw + 16 + k * CH)) for k in range(len(text) + 1))
            body.append(
                f'<clipPath id="c{i}"><rect x="36" y="{y-25}" height="34" width="8">'
                f'<animate attributeName="width" from="{int(pw+16)}" to="{int(fw)}"'
                f' begin="{t:.2f}s" dur="{dur:.2f}s" fill="freeze" calcMode="discrete" values="{steps}"/>'
                f'</rect></clipPath>\n'
                f'<g opacity="0"><set attributeName="opacity" to="1" begin="{max(0,t-0.3):.2f}s" fill="freeze"/>'
                f'<text x="36" y="{y}" clip-path="url(#c{i})">'
                f'<tspan fill="{INDIGO}">~/profile</tspan>'
                f'<tspan fill="#475569"> </tspan>'
                f'<tspan fill="{CYAN}">❯</tspan>'
                f'<tspan fill="#f8fafc"> {html.escape(text)}</tspan>'
                f'</text></g>'
            )
            t += dur + 0.42
        else:
            spans = "".join(f'<tspan fill="{c}">{html.escape(s)}</tspan>' for c, s in val)
            body.append(
                f'<g opacity="0"><animate attributeName="opacity" from="0" to="1"'
                f' begin="{t:.2f}s" dur=".2s" fill="freeze"/>'
                f'<text x="52" y="{y}">{spans}</text></g>'
            )
            t += 0.22

    # cursor
    cy = TOP + len(lines) * LH
    cx_px = int(36 + len("~/profile ❯ ") * CH + 4)
    body.append(
        f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/>'
        f'<text x="36" y="{cy}">'
        f'<tspan fill="{INDIGO}">~/profile</tspan>'
        f'<tspan fill="#475569"> </tspan>'
        f'<tspan fill="{CYAN}">❯</tspan>'
        f'<tspan fill="#f8fafc"> </tspan></text>'
        f'<rect x="{cx_px}" y="{cy-21}" width="10" height="22" fill="{CYAN}">'
        f'<animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/>'
        f'</rect></g>'
    )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="tbg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0a0e17"/>
    <stop offset="1" stop-color="#070b13"/>
  </linearGradient>
  <linearGradient id="tbd" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%"   stop-color="{CYAN}"   stop-opacity="0.9"/>
    <stop offset="50%"  stop-color="{PURPLE}" stop-opacity="0.7"/>
    <stop offset="100%" stop-color="{PINK}"   stop-opacity="0.9"/>
  </linearGradient>
</defs>

<!-- Window frame -->
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18"
  fill="url(#tbg)" stroke="url(#tbd)" stroke-width="1.5"/>

<!-- Title bar -->
<path d="M1 20 a18 18 0 0 1 18-18 h{W-38} a18 18 0 0 1 18 18 v28 H1 Z"
  fill="#0e1421"/>
<rect x="1" y="47" width="{W-2}" height="1" fill="url(#tbd)" opacity="0.4"/>

<!-- Traffic lights -->
<circle cx="30"  cy="33" r="7" fill="#ff5f57"/>
<circle cx="56"  cy="33" r="7" fill="#febc2e"/>
<circle cx="82"  cy="33" r="7" fill="#28c840"/>

<!-- Tab title -->
<text x="{W//2}" y="38" text-anchor="middle"
  font-family="{MONO}" font-size="13" fill="#475569">
  venkat@github — ~/profile — zsh
</text>

<!-- Left gutter accent -->
<rect x="114" y="48" width="1.5" height="{H-50}" rx="0.75" fill="{CYAN}" opacity="0.12"/>

<!-- Code body -->
<g font-family="{MONO}" font-size="17">
{chr(10).join(body)}
</g>
</svg>"""
    open("assets/terminal.svg", "w").write(svg)
    print("✓ assets/terminal.svg")


# ════════════════════════════════════════════════════════════════════════════
# 3. TECH MARQUEE — Scrolling icon-pill ticker
# ════════════════════════════════════════════════════════════════════════════
def make_marquee():
    techs = [
        ("React",          CYAN,    "⚛"),
        ("TypeScript",     INDIGO,  "TS"),
        ("JavaScript",     AMBER,   "JS"),
        ("Redux",          PURPLE,  "◈"),
        ("Tailwind CSS",   CYAN,    "✦"),
        ("Material UI",    INDIGO,  "▣"),
        ("Vite",           PINK,    "⚡"),
        ("Jest",           GREEN,   "✔"),
        ("Playwright",     PURPLE,  "▶"),
        ("Node.js",        GREEN,   "◉"),
        ("Git",            AMBER,   "⎇"),
        ("Figma",          PINK,    "✦"),
        ("HTML5",          "#f97316","⬡"),
        ("CSS3",           INDIGO,  "#"),
        ("GraphQL",        PINK,    "⬡"),
        ("Postman",        "#f97316","✉"),
    ]

    x, pills = 0, []
    for name, color, icon in techs:
        pw = len(name) * 10.5 + 72
        pills.append(
            f'<g transform="translate({x:.0f},8)">'
            f'<rect width="{pw:.0f}" height="44" rx="22"'
            f' fill="#0c1220" stroke="{color}" stroke-width="1.2" stroke-opacity="0.7"/>'
            f'<rect width="{pw:.0f}" height="44" rx="22" fill="{color}" opacity="0.05"/>'
            f'<text x="18" y="29" font-family="{FONT}" font-size="15" fill="{color}" opacity="0.95">{icon}</text>'
            f'<text x="38" y="29" font-family="{FONT}" font-size="15" font-weight="600" fill="#e2e8f0">{name}</text>'
            f'</g>'
        )
        x += pw + 14

    row = "".join(pills)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="60" viewBox="0 0 1200 60">
<defs>
  <mask id="edgeMask">
    <rect width="1200" height="60" fill="white"/>
    <rect width="80"   height="60" fill="url(#leftFade)"/>
    <rect x="1120" width="80" height="60" fill="url(#rightFade)"/>
  </mask>
  <linearGradient id="leftFade"  x1="0" x2="1"><stop offset="0" stop-color="black"/><stop offset="1" stop-color="black" stop-opacity="0"/></linearGradient>
  <linearGradient id="rightFade" x1="0" x2="1"><stop offset="0" stop-color="black" stop-opacity="0"/><stop offset="1" stop-color="black"/></linearGradient>
</defs>
<g mask="url(#edgeMask)">
  <g>
    <g>{row}</g>
    <g transform="translate({x:.0f},0)">{row}</g>
    <animateTransform attributeName="transform" type="translate"
      values="0 0;-{x:.0f} 0" dur="34s" repeatCount="indefinite"/>
  </g>
</g>
</svg>"""
    open("assets/tech-marquee.svg", "w").write(svg)
    print("✓ assets/tech-marquee.svg")


# ════════════════════════════════════════════════════════════════════════════
# 4. OSS CONTRIBUTION CARDS
# ════════════════════════════════════════════════════════════════════════════
def make_oss_card(path, name, accent, prs, items, badge):
    W, H = 390, 220
    per = 2 * (W - 6) + 2 * (H - 6)
    its = "".join(
        f'<text x="22" y="{106 + k*26}"'
        f' font-family="{FONT}" font-size="14.5" fill="#cbd5e1">'
        f'<tspan fill="{accent}" font-size="12">▸ </tspan>'
        f'{html.escape(s)}</text>'
        for k, s in enumerate(items)
    )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <radialGradient id="cg" cx="0.85" cy="0.1" r="0.8">
    <stop offset="0" stop-color="{accent}" stop-opacity="0.2"/>
    <stop offset="1" stop-color="{accent}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="cbg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0c1220"/>
    <stop offset="1" stop-color="#08101c"/>
  </linearGradient>
  <filter id="cglow" x="-10%" y="-20%" width="120%" height="140%">
    <feGaussianBlur stdDeviation="3" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>

<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="18"
  fill="url(#cbg)" stroke="#1e2d3d" stroke-width="1.5"/>
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="18" fill="url(#cg)"/>

<!-- Animated dashed border -->
<rect x="3" y="3" width="{W-6}" height="{H-6}" rx="17" fill="none"
  stroke="{accent}" stroke-width="2.5" stroke-linecap="round" opacity="0.85"
  stroke-dasharray="100 {per-100:.0f}">
  <animate attributeName="stroke-dashoffset" from="0" to="-{per:.0f}"
    dur="5s" repeatCount="indefinite"/>
</rect>

<!-- Ghost border -->
<rect x="3" y="3" width="{W-6}" height="{H-6}" rx="17" fill="none"
  stroke="{accent}" stroke-width="0.5" opacity="0.12"/>

<!-- Logo badge -->
<circle cx="34" cy="43" r="16" fill="{accent}" opacity="0.12"/>
<circle cx="34" cy="43" r="11" fill="{accent}" opacity="0.2">
  <animate attributeName="r"       values="10;14;10" dur="3s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="0.2;0.07;0.2" dur="3s" repeatCount="indefinite"/>
</circle>
<text x="34" y="49" text-anchor="middle"
  font-family="{MONO}" font-size="11" font-weight="800"
  fill="{accent}" filter="url(#cglow)">{html.escape(badge)}</text>

<!-- Name -->
<text x="60" y="38" font-family="{FONT}" font-size="20"
  font-weight="800" fill="#f1f5f9">{html.escape(name)}</text>

<!-- PR count pill -->
<rect x="60" y="46" width="{int(prs*9+118)}" height="22" rx="11"
  fill="{accent}" opacity="0.1" stroke="{accent}" stroke-width="0.8" stroke-opacity="0.5"/>
<text x="70" y="61" font-family="{MONO}" font-size="12"
  fill="{accent}" letter-spacing="0.8">{prs} PULL REQUEST{'S' if prs > 1 else ''} MERGED</text>

{its}
</svg>"""
    open(path, "w").write(svg)
    print(f"✓ {path}")


# ════════════════════════════════════════════════════════════════════════════
# 5. SKILLS RADAR — Hexagon radar + animated bars
# ════════════════════════════════════════════════════════════════════════════
def make_skills_radar():
    W, H = 1200, 320
    CX, CY, R = 200, 162, 128

    skills = [
        ("React / Next.js", 0.95, CYAN),
        ("TypeScript",      0.90, INDIGO),
        ("UI / UX",         0.88, PINK),
        ("Performance",     0.82, AMBER),
        ("Testing",         0.78, GREEN),
        ("Node / APIs",     0.72, PURPLE),
    ]
    N = len(skills)

    def pt(frac, val, r=R):
        a = math.radians(-90 + frac * 360)
        return CX + r * val * math.cos(a), CY + r * val * math.sin(a)

    rings = ""
    for ring in [0.25, 0.5, 0.75, 1.0]:
        pts = " ".join(f"{pt(i/N,ring)[0]:.1f},{pt(i/N,ring)[1]:.1f}" for i in range(N))
        rings += f'<polygon points="{pts}" fill="none" stroke="rgba(99,102,241,0.18)" stroke-width="0.8"/>\n'

    axes = "".join(
        f'<line x1="{CX}" y1="{CY}" x2="{pt(i/N,1)[0]:.1f}" y2="{pt(i/N,1)[1]:.1f}"'
        f' stroke="rgba(99,102,241,0.28)" stroke-width="0.8"/>'
        for i in range(N)
    )

    data_pts = " ".join(f"{pt(i/N,s[1])[0]:.1f},{pt(i/N,s[1])[1]:.1f}" for i,s in enumerate(skills))
    zero_pts  = " ".join(f"{CX},{CY}" for _ in skills)

    labels = ""
    dots   = ""
    for i, (name, val, color) in enumerate(skills):
        lx, ly = pt(i/N, 1.22)
        dx, dy = pt(i/N, val)
        labels += (
            f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" dominant-baseline="middle"'
            f' font-family="{FONT}" font-size="12.5" font-weight="600" fill="{color}">{html.escape(name)}</text>\n'
        )
        dots += (
            f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="5" fill="{color}" opacity="0.9">'
            f'<animate attributeName="r"       values="4;7.5;4"   dur="3s" begin="{i*0.3:.1f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0.9;0.4;0.9" dur="3s" begin="{i*0.3:.1f}s" repeatCount="indefinite"/>'
            f'</circle>\n'
        )

    # Skill bars (right panel)
    bars = ""
    BX, BY0, BW, BH, GAP = 460, 38, 690, 34, 12
    for i, (name, val, color) in enumerate(skills):
        by = BY0 + i * (BH + GAP)
        fw = int(BW * val)
        pct = int(val * 100)
        bars += f"""
<text x="{BX}" y="{by+20}"
  font-family="{FONT}" font-size="14" font-weight="600" fill="#e2e8f0">{html.escape(name)}</text>
<text x="{BX+BW}" y="{by+20}" text-anchor="end"
  font-family="{MONO}" font-size="12" fill="{color}">{pct}%</text>
<rect x="{BX}" y="{by+24}" width="{BW}" height="7" rx="3.5"
  fill="rgba(255,255,255,0.05)"/>
<rect x="{BX}" y="{by+24}" width="0" height="7" rx="3.5" fill="{color}" opacity="0.8">
  <animate attributeName="width" from="0" to="{fw}"
    dur="1.4s" begin="{0.2+i*0.16:.2f}s" fill="freeze"
    calcMode="spline" keySplines="0.4 0 0.2 1"/>
</rect>
<circle cx="{BX}" cy="{by+27}" r="4.5" fill="{color}">
  <animate attributeName="cx" from="{BX}" to="{BX+fw}"
    dur="1.4s" begin="{0.2+i*0.16:.2f}s" fill="freeze"
    calcMode="spline" keySplines="0.4 0 0.2 1"/>
  <animate attributeName="opacity" values="1;0.4;1" dur="2s"
    begin="{1.6+i*0.16:.2f}s" repeatCount="indefinite"/>
</circle>
"""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="rbg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0a0e17"/>
    <stop offset="1" stop-color="#070b13"/>
  </linearGradient>
  <linearGradient id="rpoly" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{CYAN}"   stop-opacity="0.3"/>
    <stop offset="1" stop-color="{PURPLE}" stop-opacity="0.2"/>
  </linearGradient>
  <linearGradient id="rpborder" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{CYAN}"   stop-opacity="0.8"/>
    <stop offset="1" stop-color="{PURPLE}" stop-opacity="0.6"/>
  </linearGradient>
  <filter id="rglow" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur stdDeviation="5" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <linearGradient id="sborder" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0"   stop-color="{CYAN}"   stop-opacity="0.7"/>
    <stop offset="0.5" stop-color="{PURPLE}" stop-opacity="0.5"/>
    <stop offset="1"   stop-color="{PINK}"   stop-opacity="0.7"/>
  </linearGradient>
</defs>

<rect width="{W}" height="{H}" rx="18"
  fill="url(#rbg)" stroke="url(#sborder)" stroke-width="1.5"/>

<!-- Section header -->
<text x="32" y="36" font-family="{FONT}" font-size="17" font-weight="800" fill="#f1f5f9">⚡ Skills &amp; Expertise</text>
<rect x="32" y="43" width="76" height="2" rx="1" fill="{CYAN}" opacity="0.7"/>

<!-- Radar grid -->
{rings}
{axes}

<!-- Data polygon — fill -->
<polygon points="{data_pts}" fill="url(#rpoly)" opacity="0.75" filter="url(#rglow)">
  <animate attributeName="points" from="{zero_pts}" to="{data_pts}"
    dur="1.2s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1"/>
</polygon>

<!-- Data polygon — border -->
<polygon points="{data_pts}" fill="none"
  stroke="url(#rpborder)" stroke-width="2" filter="url(#rglow)">
  <animate attributeName="points" from="{zero_pts}" to="{data_pts}"
    dur="1.2s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1"/>
</polygon>

{labels}
{dots}

<!-- Divider -->
<line x1="388" y1="26" x2="388" y2="{H-26}"
  stroke="{BORDER}" stroke-width="1" opacity="0.8"/>

<!-- Skill bars -->
{bars}
</svg>"""
    open("assets/skills-radar.svg", "w").write(svg)
    print("✓ assets/skills-radar.svg")


# ════════════════════════════════════════════════════════════════════════════
# 6. STATS BAR — Animated highlight numbers
# ════════════════════════════════════════════════════════════════════════════
def make_stats():
    W, H = 1200, 100
    stats = [
        ("3+",   "Years Experience",    CYAN),
        ("6",    "OSS PRs Merged",      GREEN),
        ("100%", "TypeScript Advocate", PINK),
        ("∞",    "Coffee Consumed",     AMBER),
        ("1",    "Goal: Ship Fast",     PURPLE),
    ]
    seg = W // len(stats)

    items = ""
    for i, (val, label, color) in enumerate(stats):
        cx = i * seg + seg // 2
        items += f"""
<text x="{cx}" y="52" text-anchor="middle"
  font-family="{FONT}" font-weight="900" font-size="30" fill="{color}"
  opacity="0">
  <animate attributeName="opacity" from="0" to="1"
    dur="0.6s" begin="{0.1*i:.1f}s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate"
    from="0 10" to="0 0" dur="0.6s" begin="{0.1*i:.1f}s" fill="freeze"
    calcMode="spline" keySplines="0.4 0 0.2 1"/>
  {html.escape(val)}
</text>
<text x="{cx}" y="76" text-anchor="middle"
  font-family="{MONO}" font-size="11.5" fill="#475569" letter-spacing="0.8">
  {html.escape(label.upper())}
</text>
"""
        if i < len(stats) - 1:
            items += f'<line x1="{(i+1)*seg}" y1="18" x2="{(i+1)*seg}" y2="{H-18}" stroke="{BORDER}" stroke-width="1" opacity="0.7"/>'

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="stbg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0a0e17"/>
    <stop offset="1" stop-color="#070b13"/>
  </linearGradient>
  <linearGradient id="stbd" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0"   stop-color="{CYAN}"   stop-opacity="0.65"/>
    <stop offset="0.5" stop-color="{PURPLE}" stop-opacity="0.45"/>
    <stop offset="1"   stop-color="{PINK}"   stop-opacity="0.65"/>
  </linearGradient>
</defs>
<rect width="{W}" height="{H}" rx="18"
  fill="url(#stbg)" stroke="url(#stbd)" stroke-width="1.5"/>
{items}
</svg>"""
    open("assets/stats.svg", "w").write(svg)
    print("✓ assets/stats.svg")


# ════════════════════════════════════════════════════════════════════════════
# 7. FOOTER — Neon tagline
# ════════════════════════════════════════════════════════════════════════════
def make_footer():
    W, H = 1200, 120

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="fbg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#020408"/>
    <stop offset="1" stop-color="#060a12"/>
  </linearGradient>
  <linearGradient id="ftext" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%"   stop-color="{CYAN}">
      <animate attributeName="stop-color" values="{CYAN};{PURPLE};{PINK};{CYAN}" dur="4s" repeatCount="indefinite"/>
    </stop>
    <stop offset="100%" stop-color="{PINK}">
      <animate attributeName="stop-color" values="{PINK};{CYAN};{PURPLE};{PINK}" dur="4s" repeatCount="indefinite"/>
    </stop>
  </linearGradient>
  <filter id="fglow" x="-20%" y="-60%" width="140%" height="220%">
    <feGaussianBlur stdDeviation="7" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <linearGradient id="fborder" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0"   stop-color="{CYAN}"   stop-opacity="0.7"/>
    <stop offset="0.5" stop-color="{PURPLE}" stop-opacity="0.5"/>
    <stop offset="1"   stop-color="{PINK}"   stop-opacity="0.7"/>
    <animate attributeName="x1" values="0;1;0" dur="5s" repeatCount="indefinite"/>
  </linearGradient>
  <clipPath id="fclip"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>

<g clip-path="url(#fclip)">
  <rect width="{W}" height="{H}" fill="url(#fbg)"/>
  <ellipse cx="{W//2}" cy="{H//2}" rx="360" ry="65"
    fill="{PURPLE}" opacity="0.06" filter="url(#fglow)"/>

  <text x="{W//2}" y="58" text-anchor="middle"
    font-family="{FONT}" font-weight="900" font-size="38"
    fill="url(#ftext)" filter="url(#fglow)" letter-spacing="2">
    Let's build something fast &amp; beautiful
  </text>
  <text x="{W//2}" y="90" text-anchor="middle"
    font-family="{MONO}" font-size="13.5" fill="#475569" letter-spacing="2">
    venkat@github  ·  react &amp; typescript specialist  ·  open to collaborations
  </text>

  <rect width="{W}" height="{H}" rx="18"
    fill="none" stroke="url(#fborder)" stroke-width="1.5"/>
</g>
</svg>"""
    open("assets/footer.svg", "w").write(svg)
    print("✓ assets/footer.svg")


# ════════════════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    make_header()
    make_terminal()
    make_marquee()

    make_oss_card(
        "assets/oss-freecodecamp.svg", "freeCodeCamp", "#a3e635", 3,
        ["Facebook share feature", "Mobile search placeholder fix", "Documentation improvements"],
        "fCC"
    )
    make_oss_card(
        "assets/oss-mdn.svg", "MDN Web Docs", CYAN, 2,
        ["Fixed Django documentation", "Improved content clarity"],
        "MDN"
    )
    make_oss_card(
        "assets/oss-nodejs.svg", "Node.js Website", PINK, 1,
        ["Docs readability", "Formatting & command examples"],
        "NJS"
    )

    make_skills_radar()
    make_stats()
    make_footer()

    print("\n✅ All assets generated successfully!")
