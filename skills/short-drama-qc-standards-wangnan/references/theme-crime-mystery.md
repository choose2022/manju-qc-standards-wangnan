# 题材 9：悬疑刑侦 / 谍战

适用子类：现代刑侦破案、本格推理、民间奇案、民国探案、谍战。
红线：不得出现错误执法程序与法医常识；不得美化犯罪与刑讯；不暴露侦查手段细节。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`costume-consistency-checker`（制服/年代装）、`shot-continuity-inspector`、`subtitle-timing-checker`、`audio-sync-checker`
- 补强：`novel-worldbuilding-validator`（证据链、时间线、动机）、`short-drama-review`（审讯话术、人物动机）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本·推理 | 1 | 证据链闭环 | 每个结论都有已出示的证据支撑，无天降证据 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·推理 | 2 | 时间线可复算 | 案发、报案、勘查、抓捕时间算得平 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·推理 | 3 | 动机成立 | 凶手/嫌疑人动机有前置铺垫 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本·推理 | 4 | 推理不越权 | 主角不能凭猜测定案，须有程序支撑 | 🔴 | sd-qc-engine | 人工复核位 |
| 脚本·推理 | 5 | 谍战暗号与情报 | 暗号、接头、传递方式自洽且不泄露真实手法 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·推理 | 6 | 审讯话术 | 讯问逻辑递进，不靠吼叫压供 | 🟡 | sd-qc-engine | short-drama-review |
| 资产 | 7 | 制服与标识 | 警衔、徽章、职务标识同场一致 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 8 | 证物一致性 | 现场凶器、血迹、指纹卡、证物袋编号跨镜一致 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 资产 | 9 | 现场陈设 | 尸位、家具、门窗状态在勘查前后不无故改变 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 分镜 | 10 | 现场空间关系 | 尸体、门窗、凶器方位与俯视图能对上 | 🔴 | sd-qc-engine | shot-continuity-inspector |
| 分镜 | 11 | 视线与偷窥 | 跟踪、监视、躲藏的空间关系成立 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 分镜 | 12 | 勘查动作 | 戴手套、拍照、提取证物动作规范 | 🔴 | sd-qc-engine | 人工复核位 |
| 画面 | 13 | 画风与氛围 | 全片冷调悬疑质感统一，不跳亮调 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 14 | 人体与尸体表现 | 无畸形崩坏，尸体表现克制不猎奇 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 音频 | 15 | 台词与心跳呼吸 | 时序对齐，紧张段落气息同步 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 16 | 环境音与悬念音 | 雨声、脚步、钟表音匹配，不硬炸 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 17 | 卷宗与代号字幕 | 人名、编号、案卷号逐字正确且全文一致 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 18 | 字幕不遮挡 | 不挡证物细节与关键文字 | 🟡 | sd-qc-engine | subtitle-timing-checker |
| 合规 | 19 | 执法与犯罪导向 | 不美化犯罪、不渲染刑讯、不泄露侦查手段 | 🔴 | sd-qc-engine | 人工复核位 |
| 交付 | 20 | 物料归档 | 剧本、时间线表、证据清单、审计齐全 | 🟡 | sd-qc-engine | — |

## 加载文本

```text
【悬疑刑侦谍战质检基线V1】
1.证据链闭环：结论有已出示证据支撑；阻断；sd-qc-engine；novel-worldbuilding-validator
2.时间线可复算：各节点算得平；阻断；sd-qc-engine；novel-worldbuilding-validator
3.动机成立：有前置铺垫；阻断；sd-qc-engine；short-drama-review
4.推理不越权：须有程序支撑；阻断；sd-qc-engine；人工复核位
5.谍战暗号情报：自洽不泄真实手法；阻断；sd-qc-engine；novel-worldbuilding-validator
6.审讯话术：逻辑递进不压供；一般；sd-qc-engine；short-drama-review
7.制服与标识：警衔徽章职务一致；阻断；sd-qc-engine；costume-consistency-checker
8.证物一致性：凶器血迹证物袋编号一致；阻断；sd-qc-engine；frame-consistency-checker
9.现场陈设：勘查前后不无故改变；阻断；sd-qc-engine；frame-consistency-checker
10.现场空间关系：方位与俯视图对上；阻断；sd-qc-engine；shot-continuity-inspector
11.视线与偷窥：跟踪监视关系成立；一般；sd-qc-engine；shot-continuity-inspector
12.勘查动作：手套拍照提取规范；阻断；sd-qc-engine；人工复核位
13.画风氛围：冷调悬疑统一；阻断；sd-qc-engine；frame-consistency-checker
14.人体与尸体表现：克制不猎奇；阻断；sd-qc-engine；frame-consistency-checker
15.台词与气息：时序对齐气息同步；阻断；sd-qc-engine；audio-sync-checker
16.环境与悬念音：匹配不硬炸；一般；sd-qc-engine；audio-sync-checker
17.卷宗代号字幕：逐字正确全文一致；阻断；sd-qc-engine；subtitle-timing-checker
18.字幕不遮挡：不挡证物文字；一般；sd-qc-engine；subtitle-timing-checker
19.执法与犯罪导向：不美化犯罪不泄手段；阻断；sd-qc-engine；人工复核位
20.物料归档：四件齐全；一般；sd-qc-engine；无
```

## 口令

- **初始化**：`sd-qc-engine，加载《悬疑刑侦谍战质检清单V1》+绑定表，冻结为基线；清单内校验器均为本机可执行项。`
- **单集终审**：`sd-qc-engine，加载刑侦基线，逐段逐句逐镜过 20 条；证据链与时间线走 novel-worldbuilding-validator；现场空间走 shot-continuity-inspector；出报告+审计栏。`
- **剧本前置**：`sd-qc-engine，仅跑脚本·推理 6 条，调 novel-worldbuilding-validator、short-drama-review；程序条列人工复核。`
- **单点抽检**：`frame-consistency-checker，单点抽检证物与现场陈设，仅内部参考。`
