from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Spacer


OUTPUT = "/workspace/陈子恒_AI产品_AI提效_两项目版简历.pdf"
FONT_PATH = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"


def register_font():
    pdfmetrics.registerFont(TTFont("WQY", FONT_PATH))
    pdfmetrics.registerFont(TTFont("WQY-Bold", FONT_PATH))


def para(text, style):
    return Paragraph(text, style)


def bullet(text, style):
    return Paragraph(f"• {text}", style)


def section(title, styles):
    return [
        Spacer(1, 4),
        Paragraph(title, styles["section"]),
        HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#2F5597"), spaceBefore=1.5, spaceAfter=4),
    ]


def main():
    register_font()
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=11.5 * mm,
        rightMargin=11.5 * mm,
        topMargin=8.5 * mm,
        bottomMargin=8.5 * mm,
    )

    base = getSampleStyleSheet()
    styles = {
        "name": ParagraphStyle(
            "name",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=16.5,
            leading=20,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#111111"),
            spaceAfter=1,
        ),
        "contact": ParagraphStyle(
            "contact",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=7.9,
            leading=9.8,
            textColor=colors.HexColor("#333333"),
            spaceAfter=1.6,
        ),
        "section": ParagraphStyle(
            "section",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=10.3,
            leading=12,
            textColor=colors.HexColor("#2F5597"),
            spaceBefore=1,
            spaceAfter=0,
        ),
        "normal": ParagraphStyle(
            "normal",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=7.75,
            leading=9.5,
            textColor=colors.HexColor("#202020"),
            spaceAfter=1.4,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=7.35,
            leading=9.05,
            textColor=colors.HexColor("#202020"),
            spaceAfter=1.0,
        ),
        "project_title": ParagraphStyle(
            "project_title",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=8.75,
            leading=10.4,
            textColor=colors.HexColor("#111111"),
            spaceBefore=1.4,
            spaceAfter=1.2,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=7.18,
            leading=8.85,
            leftIndent=7,
            firstLineIndent=-6,
            textColor=colors.HexColor("#202020"),
            spaceAfter=0.8,
        ),
    }

    story = []

    story.append(para("陈子恒", styles["name"]))
    story.append(para("151-3734-2002 ｜ xigua050205@163.com ｜ GitHub: github.com/moncia-25 ｜ 期望城市：不限 ｜ 到岗：随时", styles["contact"]))

    story += section("教育背景", styles)
    story.append(para("<b>新乡工程学院｜计算机科学与技术｜本科在读</b>（2023.09 - 2027.06）", styles["normal"]))
    story.append(para("GPA 3.6/4.0｜英语四级｜国家励志奖学金｜相关课程：软件工程、数据库、计算机网络、Web 开发、数据结构", styles["small"]))

    story += section("专业技能", styles)
    skills = [
        "<b>AI 工具 / Agent：</b>Dify Workflow、RAG 知识库、AI Agent 流程设计、Prompt Engineering、JSON 结构化输出、LLM 应用设计、Cursor 辅助开发、MCP 了解",
        "<b>产品能力：</b>PRD、用户场景拆解、业务流程图、字段设计、指标体系、异常流程设计、产品 Demo 验证、飞书文档",
        "<b>数据分析：</b>SQL 基础查询、Python 基础数据处理、Excel 透视表、数据看板、分类分布分析、人工介入率分析、指标拆解",
        "<b>自动化工具：</b>影刀 RPA、Dify API 调用、Excel 自动读取与回写、自动化流程设计",
        "<b>前端 / 工程基础：</b>Vue3、Next.js、React 了解、TypeScript 了解、Axios、ECharts、SSE 流式响应、GitHub、Vercel 部署",
    ]
    for item in skills:
        story.append(para(item, styles["small"]))

    story += section("项目经历", styles)

    story.append(
        KeepTogether(
            [
                para("企业客服工具自动分派与回复助手｜Dify + RAG + 影刀 RPA + Excel 数据分析", styles["project_title"]),
                bullet("针对客服工单分类耗时、回复口径不统一和高优先级投诉易遗漏的问题，使用飞书文档完成项目 PRD，梳理目标用户、业务流程、输入输出字段、分类规则、优先级规则、异常处理和验收标准。", styles["bullet"]),
                bullet("基于 Dify Workflow + RAG 知识库搭建工单处理流程，实现工单分类、知识库检索、优先级判断、人工介入识别、客服回复生成与结构化 JSON 输出。", styles["bullet"]),
                bullet("使用影刀 RPA 读取 Excel 工单数据，调用 Dify Workflow API，并将分类、优先级、分派部门、回复建议和处理状态自动回写表格，跑通工单处理自动化闭环。", styles["bullet"]),
                bullet("将工单处理结果结构化为 category、priority、need_human、assigned_team、status 等字段，并基于 Excel 透视表分析工单分类分布、优先级占比、人工介入率和部门分派量。", styles["bullet"]),
                bullet("通过 Code 节点替代优先级判断、人工介入判断等确定性逻辑，降低 LLM 调用耗时并提升流程稳定性；基于数据分析结果沉淀知识库优化和客服策略迭代方向。", styles["bullet"]),
            ]
        )
    )

    story.append(Spacer(1, 2.0))
    story.append(
        KeepTogether(
            [
                para("Y2A-Auto 视频自动化搬运与分发系统｜AI 内容自动化工具", styles["project_title"]),
                para("2026.07｜Docker / Y2A-Auto / Python / 影刀 RPA / REST API", styles["small"]),
                bullet("面向海外视频内容翻译、字幕生成与多平台分发流程重复、耗时的问题，部署并验证 Y2A-Auto 开源 AI 自动化工具，跑通 YouTube → AI 翻译字幕 → B站 / AcFun 上传链路。", styles["bullet"]),
                bullet("拆解内容分发任务流程，将“视频链接准备 → API 批量提交 → 任务队列执行 → 平台自动上传”设计为可复用的自动化提交流程。", styles["bullet"]),
                bullet("通过浏览器开发者工具分析 Web 表单请求链路，封装 /tasks/add API，使任务创建从人工表单提交升级为接口化批量调用。", styles["bullet"]),
                bullet("结合 Python 脚本与影刀 RPA，打通 Excel 链接列表读取、API 请求提交、任务队列生成流程，形成批量内容任务自动化处理方案。", styles["bullet"]),
                bullet("解决 Docker 部署、Cookie 认证、端口占用、日志报错等实际问题，沉淀开源 AI 工具部署、接口集成与 RPA 提效经验。", styles["bullet"]),
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
    for item in advantages:
        story.append(bullet(item, styles["bullet"]))

    story += section("自我评价", styles)
    story.append(
        para(
            "计算机科学与技术本科在读，具备 AI 产品设计、Agent Workflow 搭建和 Demo 落地经验。熟悉 Dify Workflow、RAG 知识库、Prompt Engineering、Cursor 辅助开发、影刀 RPA、Excel 透视表，并掌握 SQL 基础查询与 Python 基础数据处理能力。能够将业务问题拆解为字段、流程、规则、指标和可验证 Demo，更关注 AI 工具如何解决具体业务场景。",
            styles["small"],
        )
    )

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    main()
