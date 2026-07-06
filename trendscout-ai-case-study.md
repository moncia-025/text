# TrendScout AI - AI Product Case Study

## 1. Business Problem（业务问题）

- 跨境卖家依赖经验选品
- TikTok 等内容平台趋势变化快
- 缺少量化决策标准

## 2. Product Solution（产品方案）

TrendScout AI 是一个 AI 趋势分析系统。

用户输入选品需求，系统输出：

- 趋势分析
- Trend Score
- AI Report

## 3. Product Flow（产品流程图）

```text
用户输入选品需求
        ↓
AI识别品类/趋势方向
        ↓
Trend Score评分
        ↓
风险/机会判断
        ↓
AI选品报告输出
```

## 4. Core Design（核心设计）

- 设计 Trend Score，而不是直接让 AI 自由回答，是为了让商品机会判断有结构化依据。
- 设计结构化输出，是为了减少 AI 自由发挥，提升结果稳定性和可复用性。

## 5. Demo

Demo: https://trendscout-ai-pied.vercel.app

可在线体验 AI 趋势分析流程与选品报告生成。

## 6. What I Built（你的贡献）

- Designed product workflow for AI trend discovery
- Built Trend Score system for product ranking
- Defined structured AI output format (JSON/report)
- Implemented MVP using Dify + Web Demo
- Deployed working product on Vercel

## 7. Future Iteration（加分）

- 接入 TikTok / Amazon 数据源
- 增加竞品分析模块
- 引入用户反馈优化评分系统
