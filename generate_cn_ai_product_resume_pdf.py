from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Spacer


OUTPUT = "/workspace/陈子恒_AI产品_Workflow_Agent_国内版简历.pdf"
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
        Spacer(1, 3),
        Paragraph(title, styles["section"]),
        HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#2F5597"), spaceBefore=1, spaceAfter=3),
    ]


def main():
    register_font()
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=12 * mm,
        rightMargin=12 * mm,
        topMargin=9 * mm,
        bottomMargin=9 * mm,
    )

    base = getSampleStyleSheet()
    styles = {
        "name": ParagraphStyle(
            "name",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=17,
            leading=20,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#111111"),
            spaceAfter=1,
        ),
        "contact": ParagraphStyle(
            "contact",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=8.2,
            leading=10,
            textColor=colors.HexColor("#333333"),
            spaceAfter=2,
        ),
        "section": ParagraphStyle(
            "section",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=10.6,
            leading=12,
            textColor=colors.HexColor("#2F5597"),
            spaceBefore=1,
            spaceAfter=0,
        ),
        "normal": ParagraphStyle(
            "normal",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=8.0,
            leading=9.7,
            textColor=colors.HexColor("#202020"),
            spaceAfter=1.5,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=7.7,
            leading=9.4,
            textColor=colors.HexColor("#202020"),
            spaceAfter=1.2,
        ),
        "project_title": ParagraphStyle(
            "project_title",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=8.9,
            leading=10.5,
            textColor=colors.HexColor("#111111"),
            spaceBefore=1,
            spaceAfter=1,
        ),
        "subhead": ParagraphStyle(
            "subhead",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=7.8,
            leading=9.4,
            textColor=colors.HexColor("#333333"),
            spaceBefore=1,
            spaceAfter=0.5,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=7.5,
            leading=9.1,
            leftIndent=7,
            firstLineIndent=-6,
            textColor=colors.HexColor("#202020"),
            spaceAfter=0.7,
        ),
    }

    story = []

    story.append(para("陈子恒", styles["name"]))
    story.append(para("151-3734-2002 ｜ xigua050205@163.com ｜ GitHub：github.com/moncia-25", styles["contact"]))
    story.append(para("2027届｜计算机科学与技术｜AI产品 / Workflow / Agent / AI SaaS方向", styles["contact"]))

    story += section("教育背景", styles)
    story.append(para("<b>新乡工程学院｜计算机科学与技术｜本科在读</b>　2023.09 - 2027.06", styles["normal"]))
    story.append(para("GPA 3.6/4.0｜英语四级｜国家励志奖学金｜相关课程：软件工程、数据库、计算机网络、Web开发、数据结构", styles["small"]))

    story += section("专业技能", styles)
    skills = [
        "<b>产品能力：</b>需求分析、PRD、用户场景拆解、业务流程设计、字段设计、指标体系设计、异常流程设计、产品Demo验证",
        "<b>AI产品能力：</b>Workflow设计、Agent流程设计、RAG知识库、Prompt Engineering、LLM应用、JSON结构化输出、Knowledge Base设计",
        "<b>自动化与数据：</b>影刀RPA、Dify API调用、Excel自动读取与回写、Excel透视表、SQL基础查询、Python基础数据处理",
        "<b>工程基础：</b>Vue3、Next.js、React了解、TypeScript了解、ECharts、SSE、GitHub、Vercel、Cursor",
    ]
    for item in skills:
        story.append(para(item, styles["small"]))

    story += section("项目经历", styles)

    story.append(
        KeepTogether(
            [
                para("TrendScout AI｜跨境电商 AI 趋势分析与选品辅助系统", styles["project_title"]),
                para("Demo：trendscout-ai-pied.vercel.app ｜ GitHub：github.com/moncia-25/trendscout-ai", styles["small"]),
                para("<b>项目背景：</b>跨境卖家在选品时依赖经验判断，缺少趋势量化标准，容易错过TikTok等内容平台的商品机会窗口。", styles["small"]),
                para("<b>产品方案：</b>设计AI趋势分析工具，将用户选品需求转化为趋势分析、商品评分、优先级排序和AI报告输出。", styles["small"]),
                para("我的工作：", styles["subhead"]),
                bullet("梳理跨境卖家选品流程，将用户输入拆解为需求识别、趋势判断、商品评分、风险提示和报告生成。", styles["bullet"]),
                bullet("设计Trend Score评分逻辑，从增长速度、社交热度、市场扩散度、生命周期阶段等维度辅助判断商品机会。", styles["bullet"]),
                bullet("规划AI Workflow，将「选品需求 → 趋势分析 → 商品评分 → 选品建议 → AI报告」串成可验证流程。", styles["bullet"]),
                bullet("设计AI报告结构，围绕趋势阶段、机会判断、风险提示和选品建议组织结果，提升分析内容的可读性。", styles["bullet"]),
                bullet("搭建Web Demo，展示趋势榜单、商品分析结果和AI报告输出，并通过Vercel完成在线部署。", styles["bullet"]),
                bullet("通过Demo验证AI在跨境选品场景中的产品可行性，沉淀后续可扩展为选品SaaS工具的产品方向。", styles["bullet"]),
                para("<b>产品思考：</b>为了避免AI只给开放式建议，采用Trend Score + AI报告的组合设计，让趋势判断既有结构化依据，也有运营解释。", styles["small"]),
            ]
        )
    )

    story.append(Spacer(1, 1.5))
    story.append(
        KeepTogether(
            [
                para("SmartTicket AI｜企业智能客服工单自动化平台", styles["project_title"]),
                para("<b>项目背景：</b>企业客服工单存在分类依赖人工、回复口径不统一、高优先级投诉易遗漏、处理结果难以沉淀分析等问题。", styles["small"]),
                para("<b>产品方案：</b>设计AI客服自动化工具，将原始工单转化为分类、优先级、人工介入判断、回复建议和数据分析结果。", styles["small"]),
                para("我的工作：", styles["subhead"]),
                bullet("使用飞书文档完成项目PRD，梳理目标用户、业务流程、输入输出字段、分类规则、优先级规则、异常流程和验收标准。", styles["bullet"]),
                bullet("拆解客服工单处理链路，将流程规划为「工单输入 → 信息校验 → 分类 → RAG检索 → 优先级判断 → 人工介入 → 回复生成 → JSON输出」。", styles["bullet"]),
                bullet("定义工单分类规则，覆盖物流问题、退款售后、产品咨询、技术故障、投诉升级和其他问题。", styles["bullet"]),
                bullet("设计P0/P1/P2/P3优先级规则与人工介入规则，用于识别投诉、退款、故障等高风险工单。", styles["bullet"]),
                bullet("设计RAG知识库结构，沉淀物流规则、退款售后规则、投诉升级规则、产品FAQ和客服话术规范。", styles["bullet"]),
                bullet("设计结构化输出字段，包括category、priority、need_human、assigned_team、status、failure_reason，便于后续分析和流程追踪。", styles["bullet"]),
                bullet("跑通Excel工单读取、Dify Workflow调用和结果回写流程，实现从工单输入、AI分析到表格回写的自动化闭环。", styles["bullet"]),
                bullet("基于Excel透视表分析工单分类分布、优先级占比、人工介入率和部门分派量，沉淀知识库优化方向。", styles["bullet"]),
                para("<b>产品思考：</b>为了降低模型输出波动，将优先级判断和人工介入判断设计为规则化节点，将LLM主要用于语义理解和回复生成，提升Workflow稳定性。", styles["small"]),
            ]
        )
    )

    story += section("自我评价", styles)
    story.append(
        para(
            "计算机科学与技术本科在读，关注AI产品、Workflow、Agent与AI自动化方向。具备需求分析、产品方案设计、Workflow设计和Demo验证经验，能够将业务问题拆解为流程、规则、字段、指标和可验证MVP。",
            styles["small"],
        )
    )

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    main()
