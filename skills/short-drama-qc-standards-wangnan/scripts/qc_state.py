#!/usr/bin/env python3
"""项目质检状态：题材必选、当前阶段、风险台账。

**题材必选**：不传 --genre / 传入不在 15 项里的题材，一律报错退出并回显选项表，
不使用「上次用过的那套」顶替，也不许猜。

用法：
  python qc_state.py --project <项目目录> genres                     # 打印 15 项选项
  python qc_state.py --project <项目目录> init --genre 古装古风 --episode 3
  python qc_state.py --project <项目目录> set-genre 末世废土
  python qc_state.py --project <项目目录> get
  python qc_state.py --project <项目目录> resolve-genre              # 本项目已选题材则回显，否则报错列选项
  python qc_state.py --project <项目目录> stage 3
  python qc_state.py --project <项目目录> todo-add --item "第9条 队形" --level 阻断 --stage 3
  python qc_state.py --project <项目目录> todo-done --id 1 --sign wangnan
  python qc_state.py --project <项目目录> todo-list

只用标准库；状态文件 <项目目录>/.qc-state.json。
"""
import argparse
import datetime
import json
import os
import sys

STATE_NAME = ".qc-state.json"
LEVELS = ("阻断", "一般", "优化")

# 15 项：0 号是常驻层，1~14 是专项题材。名字与 SKILL.md「调用前置：先选题材」完全一致。
GENRES = [
    "全链路通用（常驻）",
    "修仙玄幻",
    "写实军事",
    "现实情感",
    "现实职场",
    "末世废土",
    "无限流规则怪谈",
    "古装古风",
    "年代重生",
    "悬疑刑侦谍战",
    "科幻未来",
    "校园青春",
    "沙雕反套路脑洞",
    "游戏穿越系统流",
    "国风神话志怪",
]


def state_path(project):
    return os.path.join(project, STATE_NAME)


def load(project):
    p = state_path(project)
    if not os.path.exists(p):
        return {
            "genre": None,
            "model": None,
            "genre_history": [],
            "stage": 1,
            "episode": None,
            "todos": [],
            "updated": None,
        }
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def save(project, st):
    st["updated"] = datetime.datetime.now().isoformat(timespec="seconds")
    with open(state_path(project), "w", encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False, indent=2)
    emit(st, "ok")


def emit(st, status):
    open_todos = [t for t in st.get("todos", []) if t.get("status") == "open"]
    blocking_open = [t for t in open_todos if t.get("level") == "阻断"]
    print(json.dumps({
        "status": status,
        "state_file": state_path_global,
        "genre": st.get("genre"),
        "model": st.get("model"),
        "stage": st.get("stage"),
        "episode": st.get("episode"),
        "todos_open": len(open_todos),
        "todos_blocking_open": len(blocking_open),
        "updated": st.get("updated"),
    }, ensure_ascii=False))


state_path_global = ""


def need_genre(st, raw, where):
    """题材必须显式选且必须是 15 项之一；不合规则报错并回显选项表。"""
    if not raw:
        print(json.dumps({
            "status": "genre_required",
            "msg": "%s 未选题材：本质检不允许直接使用，请从 15 项里选一项后重跑" % where,
            "options": GENRES,
        }, ensure_ascii=False, indent=2))
        return None
    g = raw.strip()
    if g not in GENRES:
        print(json.dumps({
            "status": "genre_invalid",
            "msg": "%s 题材「%s」不在 15 项清单里；请照选项表原样传名" % (where, g),
            "options": GENRES,
        }, ensure_ascii=False, indent=2))
        return None
    return g


def main():
    global state_path_global
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init")
    p_init.add_argument("--genre", required=False)
    p_init.add_argument("--episode", type=int)
    p_init.add_argument("--stage", type=int, default=1)
    p_init.add_argument("--model", choices=["h3", "2.5", "2.0", "seedream", "other"])

    p_set = sub.add_parser("set-genre")
    p_set.add_argument("genre")

    sub.add_parser("get")
    sub.add_parser("genres")
    sub.add_parser("resolve-genre")

    p_stage = sub.add_parser("stage")
    p_stage.add_argument("stage", type=int)

    p_add = sub.add_parser("todo-add")
    p_add.add_argument("--item", required=True)
    p_add.add_argument("--level", required=True, choices=LEVELS)
    p_add.add_argument("--stage", type=int, required=True)

    p_done = sub.add_parser("todo-done")
    p_done.add_argument("--id", type=int, required=True)
    p_done.add_argument("--sign", required=True)

    sub.add_parser("todo-list")

    args = ap.parse_args()
    project = os.path.abspath(args.project)
    if not os.path.isdir(project):
        print(json.dumps({"status": "error", "msg": "项目目录不存在: " + project}, ensure_ascii=False))
        return 2
    state_path_global = state_path(project)
    st = load(project)

    if args.cmd == "init":
        g = need_genre(st, getattr(args, "genre", None), "init")
        if g is None:
            return 2
        st["genre"] = g
        st["stage"] = args.stage
        st["episode"] = args.episode
        if getattr(args, "model", None):
            st["model"] = args.model
        if g not in st.get("genre_history", []):
            st.setdefault("genre_history", []).insert(0, g)
        save(project, st)

    elif args.cmd == "set-genre":
        g = need_genre(st, args.genre, "set-genre")
        if g is None:
            return 2
        st["genre"] = g
        hist = st.setdefault("genre_history", [])
        if g in hist:
            hist.remove(g)
        hist.insert(0, g)
        del hist[5:]
        save(project, st)

    elif args.cmd == "genres":
        print(json.dumps({"status": "ok", "count": len(GENRES), "options": GENRES},
                         ensure_ascii=False, indent=2))

    elif args.cmd == "get":
        emit(st, "ok")

    elif args.cmd == "resolve-genre":
        g = st.get("genre")
        if not g:
            print(json.dumps({
                "status": "genre_required",
                "msg": "本项目还没选题材；不许用上次那套顶替，请从 15 项里选一项",
                "options": GENRES,
                "hint_history_ignored": st.get("genre_history", []),
            }, ensure_ascii=False, indent=2))
            return 1
        print(json.dumps({"status": "ok", "genre": g, "source": "project_chosen"}, ensure_ascii=False))

    elif args.cmd == "stage":
        st["stage"] = args.stage
        save(project, st)

    elif args.cmd == "todo-add":
        todos = st.setdefault("todos", [])
        new_id = (max([t["id"] for t in todos]) + 1) if todos else 1
        todos.append({
            "id": new_id,
            "item": args.item,
            "level": args.level,
            "stage": args.stage,
            "status": "open",
            "sign": None,
            "closed_at": None,
        })
        save(project, st)

    elif args.cmd == "todo-done":
        hit = None
        for t in st.get("todos", []):
            if t.get("id") == args.id:
                hit = t
                break
        if hit is None:
            print(json.dumps({"status": "error", "msg": "台账无此 id: %d" % args.id}, ensure_ascii=False))
            return 1
        hit["status"] = "done"
        hit["sign"] = args.sign
        hit["closed_at"] = datetime.datetime.now().isoformat(timespec="seconds")
        save(project, st)

    elif args.cmd == "todo-list":
        print(json.dumps({"status": "ok", "todos": st.get("todos", [])}, ensure_ascii=False, indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
