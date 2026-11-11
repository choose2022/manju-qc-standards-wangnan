# 题材 5：末世废土

适用子类：囤货基建、房车移动堡垒、废土机甲改造、天灾末日（极寒/洪水/沙暴）、异种畸变生存。
红线：禁止过度血腥猎奇、无差别暴力、把畸变生物做成封建鬼神。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`costume-consistency-checker`、`shot-continuity-inspector`、`subtitle-timing-checker`、`audio-sync-checker`
- 补强：`fx-logic-checker`（爆炸、冰冻、烟尘、畸变光影）、`novel-worldbuilding-validator`（资源与生存逻辑）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本·设定 | 1 | 资源消耗逻辑 | 食物水燃料药品有出入账，不凭空刷物资 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·设定 | 2 | 怪物/异种设定 | 能力、弱点、族群规则前后统一 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·设定 | 3 | 基地与载具功能 | 房车改装、防御工事、房间功能描述合理 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·设定 | 4 | 危机与避险动机 | 每场危机有起因，不强行凑险 | 🟢 | sd-qc-engine | short-drama-review |
| 资产 | 5 | 护具与武器 | 同角色装具跨镜一致，增减需剧本标注 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 6 | 避难所与车辆构型 | 建筑结构、改装部件造型稳定 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 资产 | 7 | 物资道具 | 罐头、油桶、工具箱外观与品类匹配 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 分镜 | 8 | 生存动作 | 警戒、搜刮、掩体利用符合常识 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 分镜 | 9 | 集群场面 | 怪物潮、车队排布不杂乱堆叠 | 🟡 | sd-qc-engine | 【替代校验】shot-continuity-inspector + 人工复核位 |
| 分镜 | 10 | 空间动线 | 避难所通道、出入口关系自洽 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 特效 | 11 | 爆炸沙尘雨雪冰冻 | 冲击波、烟尘、冰冻有物理表现 | 🟡 | sd-qc-engine | fx-logic-checker |
| 特效 | 12 | 畸变与辐射光影 | 贴合废土写实，不做玄幻神光 | 🔴 | sd-qc-engine | fx-logic-checker |
| 画面 | 13 | 画风统一 | 全程废土质感，不跳甜宠亮调 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 14 | 人体与生物结构 | 无畸形穿模，畸变有设计感不糊 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 音频 | 15 | 对讲机与人声 | 杂音、距离感匹配，台词时序对齐 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 16 | 环境音效 | 风雪、引擎、嘶吼不压人声 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 17 | 物资与面板字幕 | 名称、数量与脚本一致，无错写 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 18 | 字幕不遮挡 | 不挡关键道具与武器面板 | 🟡 | sd-qc-engine | subtitle-timing-checker |
| 合规 | 19 | 内容合规 | 无过度血腥、猎奇导向、无序暴力 | 🔴 | sd-qc-engine | 人工复核位 |
| 交付 | 20 | 物料归档 | 剧本、分镜、基地参考图、审计日志齐全 | 🟡 | sd-qc-engine | — |

## 加载文本

```text
【末世废土质检基线V1】
1.资源消耗逻辑：出入账自洽不凭空刷物资；阻断；sd-qc-engine；novel-worldbuilding-validator
2.怪物异种设定：能力弱点规则统一；阻断；sd-qc-engine；novel-worldbuilding-validator
3.基地载具功能：改装防御工事合理；阻断；sd-qc-engine；novel-worldbuilding-validator
4.危机避险动机：每场危机有起因；优化；sd-qc-engine；short-drama-review
5.护具武器：跨镜一致增减须标注；阻断；sd-qc-engine；costume-consistency-checker
6.避难所车辆构型：结构造型稳定；阻断；sd-qc-engine；frame-consistency-checker
7.物资道具：外观品类匹配；一般；sd-qc-engine；frame-consistency-checker
8.生存动作：警戒搜刮掩体符合常识；一般；sd-qc-engine；shot-continuity-inspector
9.集群场面：排布不杂乱；一般；sd-qc-engine；shot-continuity-inspector + 人工复核位
10.空间动线：通道出入口自洽；一般；sd-qc-engine；shot-continuity-inspector
11.爆炸沙尘冰雪特效：有物理表现；一般；sd-qc-engine；fx-logic-checker
12.畸变辐射光影：废土写实不做神光；阻断；sd-qc-engine；fx-logic-checker
13.画风统一：废土质感；阻断；sd-qc-engine；frame-consistency-checker
14.人体生物结构：无畸形穿模；阻断；sd-qc-engine；frame-consistency-checker
15.对讲机人声：杂音距离匹配时序对齐；阻断；sd-qc-engine；audio-sync-checker
16.环境音效：不压人声；一般；sd-qc-engine；audio-sync-checker
17.物资面板字幕：名称数量一致；阻断；sd-qc-engine；subtitle-timing-checker
18.字幕不遮挡：不挡道具面板；一般；sd-qc-engine；subtitle-timing-checker
19.内容合规：无血腥猎奇无序暴力；阻断；sd-qc-engine；人工复核位
20.物料归档：四件齐全；一般；sd-qc-engine；无
```

## 口令

- **初始化**：`sd-qc-engine，加载《末世废土质检清单V1》+绑定表，冻结为基线；前置盘点只确认清单内校验器可执行；解绑其他题材。`
- **单集终审**：`sd-qc-engine，加载废土基线，逐段逐句逐镜过 20 条；集群镜头按替代校验并标缺口；特效条调 fx-logic-checker；出报告+审计栏。`
- **脚本前置**：`sd-qc-engine，仅跑脚本·设定 4 条，调 novel-worldbuilding-validator、short-drama-review。`
- **单点抽检**：`fx-logic-checker，单点抽检本集爆炸与畸变光影，仅内部参考。`
