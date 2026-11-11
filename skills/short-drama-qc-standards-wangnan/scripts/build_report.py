#!/usr/bin/env python3
"""生成质检报告骨架（含审计栏、签字栏、放行前置待办四表）。

用法：
  python build_report.py --project <项目目录> --episode 3 [--genre 古装古风] [--mode 正式] [--out 报告.md]

未传 --genre 时只认 .qc-state.json 里「使用人显式选过」的题材；项目还没选就报错退出（退出码 2，回显 15 项），不猜、不回落。
台账里 status=open 的条目自动填进「风险台账未销项」表。
只用标准库。
"""
import argparse
import datetime
import json
import os
import sys

STATE_NAME = ".qc-state.json"
GENRE_FILES = {
    "全链路通用（常驻）": "pipeline-10stage.md",
    "修仙玄幻": "theme-xiuxian.md",
    "写实军事": "theme-military.md",
    "现实情感": "theme-emotion.md",
    "现实职场": "theme-workplace.md",
    "末世废土": "theme-apocalypse.md",
    "无限流规则怪谈": "theme-infinite-rule-horror.md",
    "古装古风": "theme-ancient-costume.md",
    "年代重生": "theme-retro-era.md",
    "悬疑刑侦谍战": "theme-crime-mystery.md",
    "科幻未来": "theme-scifi.md",
    "校园青春": "theme-campus.md",
    "沙雕反套路脑洞": "theme-comedy-brainhole.md",
    "游戏穿越系统流": "theme-game-transmigration.md",
    "国风神话志怪": "theme-mythology.md",
}


def load_state(project):
    p = os.path.join(project, STATE_NAME)
    if not os.path.exists(p):
        return {}
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--episode", type=int)
    ap.add_argument("--genre")
    ap.add_argument("--mode", default="正式验收")
    ap.add_argument("--out")
    args = ap.parse_args()

    project = os.path.abspath(args.project)
    if not os.path.isdir(project):
        print("项目目录不存在: " + project)
        return 2
    st = load_state(project)
    genre = args.genre or st.get("genre")
    if not genre:
        print(json.dumps({"status": "genre_required",
                          "msg": "未选题材不许出报告；请带 --genre，或先让使用人从 15 项里选一项再 init",
                          "options": list(GENRE_FILES.keys())}, ensure_ascii=False, indent=2))
        return 2
    if genre not in GENRE_FILES:
        print(json.dumps({"status": "genre_invalid", "msg": "题材不在 15 项里: " + genre,
                          "options": list(GENRE_FILES.keys())}, ensure_ascii=False, indent=2))
        return 2
    episode = args.episode if args.episode is not None else st.get("episode")
    stage = st.get("stage", 1)
    todos = [t for t in st.get("todos", []) if t.get("status") == "open"]
    today = datetime.date.today().isoformat()
    name = os.path.basename(project)

    lines = []
    add = lines.append
    add("# %s 第 %s 集 质检报告" % (name, episode if episode is not None else "<未填>"))
    add("")
    add("- 题材基线：%s 清单V1（`references/%s`）" % (genre, GENRE_FILES[genre]))
    add("- 质检模式：%s" % args.mode)
    add("- 当前卡点阶段：第 %s 阶段（见 references/stage-gate-map.md）" % stage)
    add("- 质检时间：%s    质检人：<签字>" % today)
    add("- 物料范围：脚本 / 分镜 / 图片 / 视频 / 成片（按阶段勾选）")
    add("")
    add("## 一、前置技能盘点")
    add("| 校验器 | 状态 | 说明 |")
    add("|---|---|---|")
    add("| sd-qc-engine | 待填 | 主引擎 |")
    add("| 其余按清单逐条填 | 待填 | 缺的标【需安装】 |")
    add("")
    add("## 二、逐条明细")
    add("| 序 | 检查项 | 结论 | 证据（段/镜） | 等级 | 执行校验器 | 签字 |")
    add("|---|---|---|---|---|---|---|")
    add("| 1 | | 通过/不通过/未完成 | 第X段·镜Y | 🔴/🟡/🟢 | | |")
    add("")
    add("## 三、逐段小结")
    add("| 段号 | 过门禁条数 | 阻断 | 一般 | 可否流转 |")
    add("|---|---|---|---|---|")
    add("")
    add("## 四、缺陷汇总")
    add("- 🔴 阻断：")
    add("- 🟡 一般：")
    add("- 🟢 优化：")
    add("")
    add("## 五、结论")
    add("- 可验收 / 不可验收（原因）")
    add("- 需返工环节：")
    add("")
    add("## 六、技能调用审计栏")
    add("| 应调用 | 已调用 | 未调用 | 未调用原因 |")
    add("|---|---|---|---|")
    add("")
    add("## 七、缺口与人工复核位")
    add("| 条目 | 缺口 | 处理 | 复核人/状态 |")
    add("|---|---|---|---|")
    add("")
    add("## 八、放行前置待办（自动生成，不可手填省略）")
    add("")
    add("① 准入凭证缺口")
    add("| 需要的凭证 | 状态 | 谁提供 | 补交后是否重跑 |")
    add("|---|---|---|---|")
    add("")
    add("② 风险台账未销项")
    add("| 台账号 | 条目 | 等级 | 阶段 | 修复状态 | 销项签字 | 影响上线 |")
    add("|---|---|---|---|---|---|---|")
    for t in todos:
        add("| %d | %s | %s | %d | %s | %s | %s |" % (
            t["id"], t["item"], t["level"], t["stage"],
            "未修复" if t.get("status") == "open" else "已修复",
            t.get("sign") or "待签",
            "是（阻断不销项不得上线）" if t.get("level") == "阻断" else "视终审"))
    if not todos:
        add("| 无 | 无 | 无 | 无 | 无 | 无 | 无 |")
    add("")
    add("③ 因缺校验器而未完成的条目")
    add("| 清单序 | 缺哪个校验器 | 替代方式 | 补齐后补跑范围 |")
    add("|---|---|---|---|")
    add("")
    add("④ 进入下一关前置预告")
    add("| 下一阶段 | 必须带什么 | 谁签字 | 缺了卡在哪条 |")
    add("|---|---|---|---|")
    add("")
    add("> 待办四表任一非「无」，结论只能是**不可放行**。")
    add("")

    text = "\n".join(lines)
    out = args.out or os.path.join(project, "质检报告_第%s集.md" % (episode if episode is not None else "X"))
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print(json.dumps({"status": "ok", "report": os.path.abspath(out), "genre": genre,
                      "genre_source": "arg" if args.genre else "state_chosen",
                      "episode": episode, "todos_open": len(todos)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
