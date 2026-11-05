"""Junta as telas .dc.html de project/ em um único index.html autônomo."""
import json, re, html
from pathlib import Path

ROOT = Path(__file__).parent
canvas = json.loads((ROOT / "project/canvas.json").read_text(encoding="utf-8"))

screens = []
for name in canvas["order"]:
    src = (ROOT / "project" / name).read_text(encoding="utf-8")
    board = canvas["boards"][name]
    body = re.search(r"<x-dc>(.*?)</x-dc>", src, re.S).group(1)
    helmet = re.search(r"<helmet>(.*?)</helmet>", body, re.S)
    styles = "".join(re.findall(r"<style>.*?</style>", helmet.group(1), re.S)) if helmet else ""
    markup = body.replace(helmet.group(0), "") if helmet else body
    m = re.search(r"<script type=\"text/x-dc\" data-dc-script data-props='(.*?)'>(.*?)</script>", src, re.S)
    props = {k: v.get("default") for k, v in json.loads(m.group(1)).items() if not k.startswith("$")}
    screens.append({
        "id": name.replace(".dc.html", ""),
        "title": board.get("title", name),
        "w": board["w"], "h": board["h"],
        "fluid": board.get("expand") == "fill",
        "radius": board.get("radius", 0),
        "styles": styles, "markup": markup, "code": m.group(2), "props": props,
    })

templates = "\n".join(
    f'<template id="tpl-{s["id"]}">{s["styles"]}{s["markup"]}</template>' for s in screens
)
meta = json.dumps([{k: s[k] for k in ("id", "title", "w", "h", "fluid", "radius", "props", "code")} for s in screens],
                  ensure_ascii=False).replace("</", "<\\/")

shell = (ROOT / "shell.html").read_text(encoding="utf-8")
out = shell.replace("<!--TEMPLATES-->", templates).replace("/*SCREENS*/", meta).replace("<!--TITLE-->", html.escape(canvas["title"]))
(ROOT / "index.html").write_text(out, encoding="utf-8")
print("index.html gerado com", len(screens), "telas")
