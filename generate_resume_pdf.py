from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


OUTPUT = "/workspace/陈子恒_AI产品_AIWorkflow_简历.pdf"
FONT_PATH = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"


def register_fonts():
    pdfmetrics.registerFont(TTFont("WQY", FONT_PATH))
    pdfmetrics.registerFont(TTFont("WQY-Bold", FONT_PATH))


def p(text, style):
    return Paragraph(text, style)


def bullet(text, style):
    return Paragraph(f"• {text}", style)


def section(title, styles):
    return [
        Spacer(1, 4),
        Paragraph(title, styles["section"]),
        HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#2F5597"), spaceBefore=1, spaceAfter=4),
    ]


def main():
    register_fonts()
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=13 * mm,
        rightMargin=13 * mm,
        topMargin=10 * mm,
        bottomMargin=10 * mm,
    )

    base = getSampleStyleSheet()
    styles = {
        "name": ParagraphStyle(
            "name",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=18,
            leading=21,
            textColor=colors.HexColor("#1F1F1F"),
            alignment=TA_LEFT,
            spaceAfter=2,
        ),
        "contact": ParagraphStyle(
            "contact",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#333333"),
            spaceAfter=4,
        ),
        "section": ParagraphStyle(
            "section",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=11,
            leading=13,
            textColor=colors.HexColor("#2F5597"),
            spaceBefore=2,
            spaceAfter=0,
        ),
        "normal": ParagraphStyle(
            "normal",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=8.3,
            leading=10.8,
            textColor=colors.HexColor("#202020"),
            spaceAfter=2,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=7.8,
            leading=10,
            textColor=colors.HexColor("#333333"),
            spaceAfter=2,
        ),
        "item_title": ParagraphStyle(
            "item_title",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=9.3,
            leading=12,
            textColor=colors.HexColor("#111111"),
            spaceBefore=1,
            spaceAfter=1,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=8.0,
            leading=10.5,
            leftIndent=8,
            firstLineIndent=-7,
            textColor=colors.HexColor("#202020"),
            spaceAfter=1.4,
        ),
    }

    story = []

    story.append(p("陈子恒", styles["name"]))
    story.append(
        p(
            "151-3734-2002 ｜ xigua050205@163.com ｜ GitHub: github.com/moncia-25 ｜ 期望城市：不限 ｜ 到岗：随时",
            styles["contact"],
        )
    )

    story += section("教育背景", styles)
    story.append(
        p(
            "<b>新乡工程学院｜计算机科学与技术｜本科在读</b>（2023.09 - 2027.06）",
            styles["normal"],
        )
    )
    story.append(
        p(
            "GPA 3.6/4.0｜英语四级｜国家励志奖学金｜相关课程：软件工程、数据库、计算机网络、Web 开发、数据结构",
            styles["small"],
        )
    )

    story += section("专业技能", styles)
    skills = [
        "<b>AI 工具 / Agent：</b>Dify Workflow、RAG 知识库、AI Agent 流程设计、Prompt Engineering、JSON 结构化输出、LLM 应用设计、Cursor 辅助开发、MCP 了解",
        "<b>产品能力：</b>PRD、用户场景拆解、业务流程图、字段设计、指标体系、异常流程设计、产品 Demo 验证、飞书文档",
        "<b>数据分析：</b>SQL 基础查询、Python 基础数据处理、Excel 透视表、数据看板、分类分布分析、人工介入率分析、指标拆解",
        "<b>自动化工具：</b>影刀 RPA、Dify API 调用、Excel 自动读取与回写、自动化流程设计",
        "<b>前端 / 工程基础：</b>Vue3、Next.js、React 了解、TypeScript 了解、Axios、ECharts、SSE 流式响应、GitHub、Vercel 部署",
    ]
    for s in skills:
        story.append(p(s, styles["small"]))

    story += section("项目经历", styles)

    story.append(
        KeepTogether(
            [
                p("TrendScout AI｜跨境电商 AI 趋势分析与选品辅助系统", styles["item_title"]),
                p(
                    "Demo: trendscout-ai-pied.vercel.app ｜ GitHub: github.com/moncia-25/trendscout-ai",
                    styles["small"],
                ),
                bullet(
                    "围绕跨境卖家“选品依赖经验、趋势判断缺少量化标准、进入时机滞后”的问题，设计 AI 趋势分析产品方案，拆解用户输入、趋势识别、产品评分、优先级排序和报告输出流程。",
                    styles["bullet"],
                ),
                bullet(
                    "基于 Dify Workflow 设计“需求输入 → 趋势分析 → 产品评分 → 选品建议 → 报告生成”AI 工作流，结合 Prompt 调优与结构化输出提升趋势分析结果的可读性和稳定性。",
                    styles["bullet"],
                ),
                bullet(
                    "设计 Trend Score 评分逻辑，从增长速度、社交热度、市场扩散度、生命周期阶段等维度辅助判断产品机会，用于支持选品优先级排序。",
                    styles["bullet"],
                ),
                bullet(
                    "使用 Cursor 辅助完成前端 Demo 搭建，并通过 Vercel 部署 Web 可视化页面，展示趋势榜单、产品分析结果和 AI 报告输出效果。",
                    styles["bullet"],
                ),
                bullet(
                    "通过 GitHub 管理项目代码与迭代过程，沉淀跨境电商 AI 选品场景下的需求分析、Workflow 设计和 Demo 验证经验。",
                    styles["bullet"],
                ),
            ]
        )
    )

    story.append(Spacer(1, 2))
    story.append(
        KeepTogether(
            [
                p("企业客服工单自动分派与回复助手｜Dify + RAG + 影刀 RPA + Excel 数据分析", styles["item_title"]),
                bullet(
                    "针对客服工单分类耗时、回复口径不统一和高优先级投诉易遗漏的问题，使用飞书文档完成项目 PRD，梳理目标用户、业务流程、输入输出字段、分类规则、优先级规则、异常处理和验收标准。",
                    styles["bullet"],
                ),
                bullet(
                    "基于 Dify Workflow + RAG 知识库搭建工单处理流程，实现工单分类、知识库检索、优先级判断、人工介入识别、客服回复生成与结构化 JSON 输出。",
                    styles["bullet"],
                ),
                bullet(
                    "使用影刀 RPA 读取 Excel 工单数据，调用 Dify Workflow API，并将分类、优先级、分派部门、回复建议和处理状态自动回写表格，跑通工单处理自动化闭环。",
                    styles["bullet"],
                ),
                bullet(
                    "将工单处理结果结构化为 category、priority、need_human、assigned_team、status 等字段，并基于 Excel 透视表分析工单分类分布、优先级占比、人工介入率和部门分派量。",
                    styles["bullet"],
                ),
                bullet(
                    "通过 Code 节点替代优先级判断、人工介入判断等确定性逻辑，降低 LLM 调用耗时并提升流程稳定性；基于数据分析结果沉淀知识库优化和客服策略迭代方向。",
                    styles["bullet"],
                ),
            ]
        )
    )

    story += section("岗位匹配优势", styles)
    advantages = [
        "具备计算机专业背景，能理解基础技术实现逻辑，并将业务问题拆解为字段、流程、规则、指标和可验证 Demo。",
        "有 Dify Workflow、RAG 知识库、Prompt 调优、影刀 RPA 和 Excel 数据分析的完整实践，能独立完成 AI 产品原型和自动化流程验证。",
        "相比传统开发，更关注 AI 工具在具体业务场景中的落地价值，能够通过 PRD、流程图、数据表和 Demo 展示产品方案。",
        "关注 AI SaaS、跨境电商 AI、Agent Workflow 和自动化工具方向，适合 AI 产品助理、AI Workflow、AI SaaS 产品运营、DevRel 和 AI 增长运营相关岗位。",
    ]
    for a in advantages:
        story.append(bullet(a, styles["bullet"]))

    story += section("自我评价", styles)
    story.append(
        p(
            "计算机科学与技术本科在读，具备 AI 产品设计、Agent Workflow 搭建和 Demo 落地经验。熟悉 Dify Workflow、RAG 知识库、Prompt Engineering、Cursor 辅助开发、影刀 RPA、Excel 透视表，并掌握 SQL 基础查询与 Python 基础数据处理能力。能够将业务问题拆解为字段、流程、规则、指标和可验证 Demo，更关注 AI 工具如何解决具体业务场景。",
            styles["small"],
        )
    )

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    main()
