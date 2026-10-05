#!/usr/bin/env python3
"""Build a client demo page from template.html.

Usage:
  python3 generate.py clients/<slug>.json      -> writes <slug>/index.html
  python3 generate.py --all                    -> rebuilds every client + index

JSON fields: slug, clinic_name, agent_id, first_message, chips[], questions[]
"""
import html, json, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent

def build(cfg_path: pathlib.Path) -> pathlib.Path:
    c = json.loads(cfg_path.read_text(encoding="utf-8"))
    e = html.escape
    page = (ROOT / "template.html").read_text(encoding="utf-8")
    page = (page.replace("{{CLINIC_NAME}}", e(c["clinic_name"]))
                .replace("{{AGENT_ID}}", c["agent_id"])
                .replace("{{FIRST_MESSAGE}}", e(c["first_message"]))
                .replace("{{CHIPS}}", "".join(f'<span class="chip">{e(x)}</span>' for x in c.get("chips", [])))
                .replace("{{QUESTIONS}}", "".join(f"<li>{e(q)}</li>" for q in c.get("questions", []))))
    out = ROOT / c["slug"] / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return out

if __name__ == "__main__":
    targets = sorted((ROOT / "clients").glob("*.json")) if sys.argv[1:] == ["--all"] else [pathlib.Path(a) for a in sys.argv[1:]]
    if not targets:
        sys.exit(__doc__)
    for t in targets:
        print("built", build(t).relative_to(ROOT))
