#!/usr/bin/env python3
"""质检自检：清单完整性、校验器存在性、报告必备件。

用法：
  python qc_lint.py checklists --dir <skill>/references
  python qc_lint.py validators --skill <skill目录> --roots <skills根目录> [--roots ...]
  python qc_lint.py skill --skill <skill目录>
  python qc_lint.py report --file <报告.md>

有问题时退出码 1；全通过退出码 0。只用标准库。
"""
import argparse
import json
import os
import re
import sys

LEVELS = ("🔴", "🟡", "🟢")
SKIP_TOKENS = ("theme-", "pipeline-", "report-template", "stage-gate-map", "example")


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def cmd_checklists(args):
    problems = []
    files = sorted(f for f in os.listdir(args.dir) if f.endswith(".md"))
    theme_files = [f for f in files if f.startswith("theme-")]
    pipeline = [f for f in files if f.startswith("pipeline-")]
    for f in theme_files + pipeline:
        path = os.path.join(args.dir, f)
        txt = read(path)
        need = ["## 加载文本", "## 口令"]
        if f.startswith("theme-"):
            need.insert(0, "## 质检清单 V1")
        for n in need:
            if n not in txt:
                problems.append("%s 缺章节: %s" % (f, n))
        rows = [l for l in txt.splitlines() if l.startswith("| ") and ("🔴" in l or "🟡" in l or "🟢" in l)]
        if not rows:
            problems.append("%s 未找到带等级标记的清单行" % f)
        bad = [l for l in rows if not any(x in l for x in LEVELS)]
        if bad:
            problems.append("%s 有 %d 行缺等级" % (f, len(bad)))
        if f.startswith("theme-") and "技能池" not in txt:
            problems.append("%s 缺技能池" % f)
    print(json.dumps({"mode": "checklists", "files": len(theme_files + pipeline),
                      "problems": problems, "ok": not problems}, ensure_ascii=False, indent=2))
    return 0 if not problems else 1


def collect_tokens(txt):
    """只从表格行里认校验器名，避免把脚本命令（如 todo-add）当成技能名。"""
    toks = set()
    for line in txt.splitlines():
        if not line.startswith("| "):
            continue
        if "scripts/" in line or ".py" in line:
            continue
        for m in re.finditer(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)+", line):
            t = m.group(0)
            tail = line[m.end():]
            if tail[:1] in (".", "/", "*") or tail[:2] == "-*" or tail[:6].lower() in (".json", ".py", ".md"):
                continue
            if any(t.startswith(s) for s in SKIP_TOKENS):
                continue
            toks.add(t)
    return toks


def cmd_validators(args):
    have = set()
    for r in args.roots:
        if os.path.isdir(r):
            have |= {d for d in os.listdir(r) if os.path.isdir(os.path.join(r, d))}
    txt = ""
    for root, _dirs, fs in os.walk(args.skill):
        for f in fs:
            if f.endswith(".md"):
                txt += read(os.path.join(root, f)) + "\n"
    toks = collect_tokens(txt)
    missing = sorted(t for t in toks if t not in have)
    print(json.dumps({"mode": "validators", "referenced": len(toks), "available": len(have),
                      "missing": missing,
                      "install_hint": ["需安装: " + m for m in missing],
                      "ok": True}, ensure_ascii=False, indent=2))
    return 0


def cmd_skill(args):
    problems = []
    skill_md = os.path.join(args.skill, "SKILL.md")
    if not os.path.exists(skill_md):
        print(json.dumps({"mode": "skill", "problems": ["缺 SKILL.md"], "ok": False}, ensure_ascii=False, indent=2))
        return 1
    txt = read(skill_md)
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if not m:
        problems.append("frontmatter 缺失")
    else:
        fm = m.group(1)
        name = re.search(r"^name:\s*(.+)$", fm, re.M)
        desc = re.search(r"^description:\s*(.+)$", fm, re.M)
        if not name:
            problems.append("frontmatter 缺 name")
        elif name.group(1).strip() != os.path.basename(args.skill.rstrip("\\/")):
            problems.append("name 与目录名不一致: %s" % name.group(1).strip())
        if not desc:
            problems.append("frontmatter 缺 description")
        extra = [l.split(":")[0] for l in fm.splitlines() if l.strip() and not re.match(r"^(name|description):", l)]
        if extra:
            problems.append("frontmatter 多出字段: %s" % ", ".join(extra))
    for rel in re.findall(r"references/[A-Za-z0-9._-]+\.md", txt):
        if not os.path.exists(os.path.join(args.skill, rel.replace("/", os.sep))):
            problems.append("引用了不存在的文件: %s" % rel)
    edit_lines = len(txt.splitlines())
    if edit_lines > 500:
        problems.append("SKILL.md 超 500 行: %d" % edit_lines)
    print(json.dumps({"mode": "skill", "lines": edit_lines, "problems": problems, "ok": not problems}, ensure_ascii=False, indent=2))
    return 0 if not problems else 1


NEED_SECTIONS = [
    "技能调用审计栏",
    "放行前置待办",
    "准入凭证缺口",
    "风险台账未销项",
    "下一关前置预告",
]


def cmd_report(args):
    txt = read(args.file)
    problems = [("缺必备件: " + s) for s in NEED_SECTIONS if s not in txt]
    if "未完成" not in txt:
        problems.append("缺「未完成」口径说明，无法判断缺口是否被写成通过")
    if txt.count("签字") < 2:
        problems.append("签字栏不足两处，疑未落实签字")
    print(json.dumps({"mode": "report", "file": os.path.abspath(args.file),
                      "problems": problems, "ok": not problems}, ensure_ascii=False, indent=2))
    return 0 if not problems else 1


H3_MARKS = ["<d>", "</d>", "soundscape", "[Shot ", "Hailuo", "MiniMax"]
SEED_MARKS = ["[SFX:]", "seedance", "Seedance"]


def cmd_models(args):
    """检查投喂稿结构与声明模型是否匹配（跨模型套用最常见的废稿原因）。"""
    txt = read(args.file)
    h3 = {m: txt.count(m) for m in H3_MARKS if txt.count(m)}
    sd = {m: txt.count(m) for m in SEED_MARKS if txt.count(m)}
    problems = []
    model = args.model.lower()
    if model == "h3":
        if sd:
            problems.append("声明 H3，但稿内出现 Seedance 标记: %s" % ", ".join(sd))
        if not h3:
            problems.append("声明 H3，但未检出任何 H3 结构标记（<d> / soundscape / [Shot k]），疑似非 H3 稿")
    else:
        if any(k in h3 for k in ("<d>", "</d>", "[Shot ")):
            problems.append("声明 Seedance %s，但稿内出现 H3 六段式标记: %s（失效条款：H3 六段式台词块）" % (args.model, ", ".join(h3)))
        if args.model == "2.0" and "[SFX:]" in sd:
            problems.append("[SFX:] 在 Seedance 2.0 上禁用（失效条款：[SFX:] 音效标记开关）")
        if not sd:
            problems.append("声明 Seedance，但未检出 Seedance 标记（[SFX:] / seedance），请确认稿式")
    print(json.dumps({"mode": "models", "file": os.path.abspath(args.file), "model": args.model,
                      "h3_markers": h3, "seedance_markers": sd,
                      "problems": problems, "ok": not problems}, ensure_ascii=False, indent=2))
    return 0 if not problems else 1


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("checklists")
    a.add_argument("--dir", required=True)
    b = sub.add_parser("validators")
    b.add_argument("--skill", required=True)
    b.add_argument("--roots", action="append", required=True)
    c = sub.add_parser("skill")
    c.add_argument("--skill", required=True)
    d = sub.add_parser("report")
    d.add_argument("--file", required=True)
    e = sub.add_parser("models")
    e.add_argument("--file", required=True)
    e.add_argument("--model", required=True, choices=["h3", "2.5", "2.0"])
    args = ap.parse_args()
    return {"checklists": cmd_checklists, "validators": cmd_validators,
            "skill": cmd_skill, "report": cmd_report, "models": cmd_models}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
