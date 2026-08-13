# Fat Loss Coach

一个可持续减脂与体重管理 skill，把个人减重经验整理成可复用的评估、计划、记录和长期跟进流程。

## 我的减重记录

我的减重视频：[Bilibili 减重视频](https://www.bilibili.com/video/BV1SyxSejEBn/?spm_id_from=333.1387.homepage.video_card.click&vd_source=33b2ad8a522d5164764c5bf6720bbb69)

## 能做什么

- 根据年龄、性别、身高、体重和活动量生成代谢计划。
- 生成 7 天饮食、断食窗口和预算购物清单。
- 生成居家或健身房训练计划，并区分大体重和小体重。
- 提供每日体重、体脂、睡眠、饮水和训练记录。
- 用离线看板查看体重和体脂趋势。
- 通过目标页和每日跟进支持长期坚持。
- 处理平台期，并提供安全的短时液体重置建议。

## 目录

```text
fat-loss-coach/
├── SKILL.md
├── agents/openai.yaml
├── assets/
├── references/
└── scripts/
```

## 快速使用

```bash
python3 scripts/metabolic_plan.py --sex male --age 29 --height-cm 165 --weight-kg 60 --activity 1.375 --goal fat_loss
```

```bash
python3 scripts/track.py init tracking.json
python3 scripts/track.py append tracking.json --date 2026-08-14 --weight-kg 59.2
```

打开 `assets/dashboard.html` 查看跟踪看板。

## 安全说明

本项目提供的是健康习惯和体重管理建议，不构成医疗诊断或治疗。孕期、未成年、进食障碍、糖尿病、肝肾疾病、心脏疾病或存在不明原因体重快速变化者，应在专业人士指导下使用。
