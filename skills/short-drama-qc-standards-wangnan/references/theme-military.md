# 题材 2：写实军事

适用子类：现代班组战术、装甲车队、阵地攻防、无人机与侦察、撤离护送。
红线：拦截涉密装备编号、真实涉密单位与阵地、真实作战口令；过度血腥与违规导向一律阻断。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`costume-consistency-checker`（装具）、`shot-continuity-inspector`、`subtitle-timing-checker`、`audio-sync-checker`
- 补强：`fx-logic-checker`（弹道、爆炸、夜视、激光）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本·战术 | 1 | 术语与呼号 | 术语符合常规战术表达，无悬浮军迷黑话，无错字 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本·战术 | 2 | 班组分工与流程 | 突击、警戒、掩护分工清楚，流程不违背常识 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本·战术 | 3 | 装备型号文字 | 同一装备全文一个型号，不出现自相矛盾或虚构型号 | 🔴 | sd-qc-engine | 人工复核位 |
| 脚本·战术 | 4 | 任务因果 | 指令来源、目标、撤离条件成立 | 🟡 | sd-qc-engine | novel-worldbuilding-validator |
| 资产 | 5 | 单兵装具 | 头盔、护具、背包、标识同角色跨镜一致 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 6 | 枪械与配件 | 型号、瞄具、消音前后统一，配件不乱搭 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 资产 | 7 | 载具与设备 | 车辆构型、涂装、外挂设备跨镜稳定 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 分镜·动作 | 8 | 据枪与换弹 | 持枪、依托、换弹动作成立，无畸形姿势 | 🔴 | sd-qc-engine | shot-continuity-inspector |
| 分镜·队形 | 9 | 车队与阵地排布 | 间距、朝向、警戒点位合理，不杂乱堆叠 | 🟡 | sd-qc-engine | 【替代校验】shot-continuity-inspector + 人工复核位 |
| 分镜·空间 | 10 | 机位与车内视角 | 空间自洽，车内与车外关系对得上 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 特效 | 11 | 枪口焰与弹道 | 焰口位置、弹壳抛出方向、轨迹成立 | 🔴 | sd-qc-engine | fx-logic-checker |
| 特效 | 12 | 爆炸与烟尘 | 有冲击波与烟尘扩散，不反重力漂浮 | 🟡 | sd-qc-engine | fx-logic-checker |
| 特效 | 13 | 夜视与激光 | 夜视噪点、激光光斑像设备，不做成玄幻光效 | 🔴 | sd-qc-engine | fx-logic-checker |
| 画面 | 14 | 画风统一 | 全程写实质感，不跳二次元 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 15 | 人体结构 | 无畸形、穿模、多指 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 16 | 环境光照天气 | 同场景光照、雨雾沙尘氛围稳定 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 成片 | 17 | 镜头接续 | 顺序对分镜，队形能承接上一镜 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 音频 | 18 | 人声与电台 | 台词、电台语音与动作时序匹配 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 19 | 枪炮与环境音 | 分层清楚，枪声不过爆，环境音匹配场景 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 20 | 字幕与术语 | 逐字一致，战术术语与型号写法正确 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 21 | 字幕不遮挡 | 不挡仪表、瞄具、标识 | 🟡 | sd-qc-engine | subtitle-timing-checker |
| 合规 | 22 | 涉密与导向 | 无涉密编号、涉密单位、违规导向、过度血腥 | 🔴 | sd-qc-engine | 人工复核位（必过） |
| 交付 | 23 | 物料归档 | 剧本、分镜、装备参考卡、报告、审计齐全 | 🟡 | sd-qc-engine | — |

## 加载文本

```text
【写实军事质检基线V1】
1.术语与呼号：术语规范无涉密口令；阻断；强制 sd-qc-engine；补强 short-drama-review
2.班组分工流程：分工清楚不违常识；阻断；强制 sd-qc-engine；补强 short-drama-review
3.装备型号文字：全文一个型号无虚构；阻断；强制 sd-qc-engine；补强 人工复核位
4.任务因果：指令目标撤离成立；一般；强制 sd-qc-engine；补强 novel-worldbuilding-validator
5.单兵装具：跨镜一致；阻断；强制 sd-qc-engine；补强 costume-consistency-checker
6.枪械与配件：型号配件统一；阻断；强制 sd-qc-engine；补强 frame-consistency-checker
7.载具与设备：构型涂装稳定；阻断；强制 sd-qc-engine；补强 frame-consistency-checker
8.据枪与换弹：动作成立无畸形；阻断；强制 sd-qc-engine；补强 shot-continuity-inspector
9.车队阵地排布：间距朝向警戒合理；一般；强制 sd-qc-engine；补强 shot-continuity-inspector + 人工复核位
10.机位与车内视角：空间自洽；一般；强制 sd-qc-engine；补强 shot-continuity-inspector
11.枪口焰与弹道：位置方向成立；阻断；强制 sd-qc-engine；补强 fx-logic-checker
12.爆炸与烟尘：有冲击波不反重力；一般；强制 sd-qc-engine；补强 fx-logic-checker
13.夜视与激光：符合设备特征；阻断；强制 sd-qc-engine；补强 fx-logic-checker
14.画风统一：全程写实；阻断；强制 sd-qc-engine；补强 frame-consistency-checker
15.人体结构：无畸形穿模；阻断；强制 sd-qc-engine；补强 frame-consistency-checker
16.环境光照天气：同场景稳定；一般；强制 sd-qc-engine；补强 frame-consistency-checker
17.镜头接续：顺序对分镜队形可承接；一般；强制 sd-qc-engine；补强 shot-continuity-inspector
18.人声与电台：时序匹配；阻断；强制 sd-qc-engine；补强 audio-sync-checker
19.枪炮环境音：分层清楚不过爆；一般；强制 sd-qc-engine；补强 audio-sync-checker
20.字幕与术语：逐字一致术语正确；阻断；强制 sd-qc-engine；补强 subtitle-timing-checker
21.字幕不遮挡：不挡仪表瞄具标识；一般；强制 sd-qc-engine；补强 subtitle-timing-checker
22.涉密与导向：无涉密无违规无过度血腥；阻断；强制 sd-qc-engine；补强 人工复核位
23.物料归档：五件齐全；一般；强制 sd-qc-engine；补强 无
```

## 口令

- **初始化**：`sd-qc-engine，加载《写实军事质检清单V1》+绑定表，冻结为基线；前置盘点只确认清单内校验器可执行，缺失项已替换为可执行项 + 人工复核位；解绑修仙类校验器。`
- **单集终审**：`sd-qc-engine，加载军事基线，逐段逐句逐镜过 23 条；第9条按替代校验执行并标缺口；特效条调 fx-logic-checker；合规条必须人工复核签字；出报告+审计栏。`
- **脚本前置**：`sd-qc-engine，仅跑脚本·战术 4 条 + 合规 1 条，调 short-drama-review；装备型号条列人工复核位。`
- **单点抽检**：`fx-logic-checker，单点抽检本集弹道与爆炸，仅内部参考。`
