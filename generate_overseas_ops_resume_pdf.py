from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Spacer


OUTPUT = "/workspace/陈子恒_海外运营实习_简历.pdf"
FONT_PATH = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"


def register_font():
    pdfmetrics.registerFont(TTFont("WQY", FONT_PATH))
    pdfmetrics.registerFont(TTFont("WQY-Bold", FONT_PATH))


def section(title, styles):
    return [
        Spacer(1, 3),
        Paragraph(title, styles["section"]),
        HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#2F5597"), spaceBefore=1, spaceAfter=3),
    ]


def p(text, style):
    return Paragraph(text, style)


def bullet(text, style):
    return Paragraph(f"• {text}", style)


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
            textColor=colors.HexColor("#111111"),
            alignment=TA_LEFT,
            spaceAfter=1,
        ),
        "contact": ParagraphStyle(
            "contact",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=8.1,
            leading=9.8,
            textColor=colors.HexColor("#333333"),
            spaceAfter=1.2,
        ),
        "section": ParagraphStyle(
            "section",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=10.6,
            leading=12,
            textColor=colors.HexColor("#2F5597"),
        ),
        "normal": ParagraphStyle(
            "normal",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=7.85,
            leading=9.5,
            textColor=colors.HexColor("#202020"),
            spaceAfter=1.2,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=7.45,
            leading=9.0,
            textColor=colors.HexColor("#202020"),
            spaceAfter=1.0,
        ),
        "project_title": ParagraphStyle(
            "project_title",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=8.9,
            leading=10.5,
            textColor=colors.HexColor("#111111"),
            spaceBefore=1.2,
            spaceAfter=0.8,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=7.45,
            leading=8.9,
            leftIndent=7,
            firstLineIndent=-6,
            textColor=colors.HexColor("#202020"),
            spaceAfter=0.45,
        ),
    }

    story = []
    story.append(p("陈子恒", styles["name"]))
    story.append(p("151-3734-2002 ｜ xigua050205@163.com ｜ GitHub：github.com/moncia-025", styles["contact"]))
    story.append(p("2027届本科｜计算机科学与技术｜求职方向：海外市场运营 / 海外运营实习生 / 海外用户运营", styles["contact"]))

    story += section("教育背景", styles)
    story.append(p("<b>新乡工程学院｜计算机科学与技术｜本科</b>　2023.09 - 2027.06", styles["normal"]))
    story.append(p("GPA：3.6/4.0｜CET-4｜国家励志奖学金｜主修课程：软件工程、数据库、计算机网络、Web开发、数据结构", styles["small"]))

    story += section("专业技能", styles)
    skills = [
        "<b>海外平台与内容观察：</b>关注 TikTok、X（Twitter）、Reddit、Instagram、Facebook 等海外社媒平台，了解内容传播、热点趋势和社区互动特点。",
        "<b>AI 办公与运营提效：</b>熟悉 ChatGPT、Claude、Gemini、Cursor、Dify 等 AI 工具，可用于市场信息检索、内容整理、运营文案生成、知识库整理和竞品资料分析。",
        "<b>数据与表格分析：</b>熟悉 Excel 函数、数据透视表，掌握 SQL 基础查询和 Python 基础数据处理，能够完成基础数据清洗、分类统计和趋势整理。",
        "<b>文档与流程整理：</b>熟悉 Markdown、飞书文档，可完成调研记录、项目文档、流程说明、SOP 和复盘总结。",
    ]
    for item in skills:
        story.append(p(item, styles["small"]))

    story += section("项目经历", styles)
    story.append(
        KeepTogether(
            [
                p("TrendScout AI｜跨境商品趋势分析平台", styles["project_title"]),
                p("个人项目｜2025.05 - 至今", styles["small"]),
                p("<b>项目简介：</b>围绕跨境卖家选品依赖经验、海外趋势变化快的问题，结合 Google Trends、TikTok 热门趋势和 AI 工具，搭建商品趋势分析与选品参考流程。", styles["small"]),
                bullet("收集 Google Trends、TikTok 等公开趋势信息，整理不同国家和地区的热门关键词、品类方向和潜在商品机会。", styles["bullet"]),
                bullet("梳理跨境商品趋势分析流程，将“关键词输入 → 趋势观察 → 商品机会判断 → 选品建议输出”整理为标准化分析路径。", styles["bullet"]),
                bullet("使用 AI 工具辅助完成趋势资料整理、商品方向归纳和选品报告生成，提高信息整理和分析效率。", styles["bullet"]),
                bullet("设计商品趋势分析报告结构，包含趋势背景、目标市场、潜在人群、商品机会、风险点和运营建议。", styles["bullet"]),
                bullet("通过 Web Demo 展示趋势分析结果，沉淀跨境选品场景下的数据整理、趋势判断和内容输出经验。", styles["bullet"]),
            ]
        )
    )

    story.append(Spacer(1, 1.2))
    story.append(
        KeepTogether(
            [
                p("AI 客服工单自动化系统", styles["project_title"]),
                p("个人项目｜2025.06 - 至今", styles["small"]),
                p("<b>项目简介：</b>基于 Dify + RAG + 影刀搭建客服工单自动处理流程，用于模拟物流查询、售后咨询、投诉升级等场景下的自动分类和回复生成。", styles["small"]),
                bullet("梳理客服业务流程，将用户问题拆解为物流问题、售后咨询、产品咨询、投诉升级等工单类型。", styles["bullet"]),
                bullet("整理物流、售后、产品 FAQ 和客服话术规范，搭建基础知识库，提高回复内容的一致性。", styles["bullet"]),
                bullet("设计工单分类、优先级判断和人工介入规则，形成标准化客服处理流程。", styles["bullet"]),
                bullet("搭建 Workflow，实现工单自动分类、知识库检索、回复生成和表格回写。", styles["bullet"]),
                bullet("使用 Excel 透视表分析工单分类分布、优先级占比和人工介入情况，沉淀运营数据分析思路。", styles["bullet"]),
            ]
        )
    )

    story += section("校园项目", styles)
    story.append(
        KeepTogether(
            [
                p("软件工程课程项目｜智能客服系统需求分析", styles["project_title"]),
                p("2025.03 - 2025.06", styles["small"]),
                bullet("负责智能客服系统的需求分析和功能规划，梳理用户咨询、问题分类、回复生成和后台管理等核心模块。", styles["bullet"]),
                bullet("绘制业务流程图、用例图和功能流程图，整理课程项目文档。", styles["bullet"]),
                bullet("参与课程展示与答辩，配合团队完成项目设计说明和展示材料。", styles["bullet"]),
                bullet("在项目中训练需求拆解、文档整理、流程表达和团队协作能力。", styles["bullet"]),
            ]
        )
    )

    story += section("自我评价", styles)
    story.append(
        p(
            "关注海外互联网、跨境电商和社交媒体运营，持续观察 TikTok、Reddit、X 等平台内容趋势。具备较强的信息收集、数据整理和学习能力，能够利用 AI 工具提升市场调研、内容整理和运营分析效率。希望在海外运营岗位中参与市场调研、内容运营、用户运营和数据整理相关工作。",
            styles["small"],
        )
    )

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    main()
