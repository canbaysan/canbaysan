"""Wrap the generated snake SVG in a card that matches the profile's other cards."""
import re, sys

src, dst = sys.argv[1], sys.argv[2]
svg = open(src, encoding="utf-8").read()
svg = re.sub(r"<\?xml[^>]*\?>", "", svg).strip()
open_tag = re.match(r"<svg[^>]*>", svg).group(0)
vb = re.search(r'viewBox="([^"]+)"', open_tag)
if vb:
    viewbox = vb.group(1)
else:
    w = re.search(r'width="([\d.]+)', open_tag).group(1)
    h = re.search(r'height="([\d.]+)', open_tag).group(1)
    viewbox = f"0 0 {w} {h}"
vx, vy, vw, vh = map(float, viewbox.split())
inner_w = 800
inner_h = round(inner_w * vh / vw)
top = 80
H = top + inner_h + 30
body = svg[len(open_tag):].rsplit("</svg>", 1)[0]

out = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="{H}" viewBox="0 0 860 {H}" role="img" aria-label="Contribution graph snake">
  <title>Contribution graph snake</title>
  <rect width="860" height="{H}" rx="16" fill="#0d1117"/>
  <rect x="1" y="1" width="858" height="{H-2}" rx="15" fill="none" stroke="#30363d" stroke-width="2"/>
  <text x="430" y="50" text-anchor="middle" font-family="'Fira Code', Consolas, monospace" font-size="14" letter-spacing="4" fill="#8b949e">CONTRIBUTIONS</text>
  <svg x="30" y="{top}" width="{inner_w}" height="{inner_h}" viewBox="{viewbox}">{body}</svg>
</svg>
'''
open(dst, "w", encoding="utf-8").write(out)
