from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer


OUTPUT = "/workspace/陈子恒_AI产品与自动化工具作品集_精简版.pdf"
FONT_PATH = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"


def register_font():
    pdfmetrics.registerFont(TTFont("WQY", FONT_PATH))
    pdfmetrics.registerFont(TTFont("WQY-Bold", FONT_PATH))


def section(title, styles):
    return [
        Spacer(1, 2.5),
        Paragraph(title, styles["section"]),
        HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#2F5597"), spaceBefore=1, spaceAfter=2.2),
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
        leftMargin=11 * mm,
        rightMargin=11 * mm,
        topMargin=8 * mm,
        bottomMargin=8 * mm,
    )

    base = getSampleStyleSheet()
    styles = {
        "title": ParagraphStyle(
            "title",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=15.5,
            leading=18,
            textColor=colors.HexColor("#111111"),
            alignment=TA_LEFT,
            spaceAfter=2,
        ),
        "section": ParagraphStyle(
            "section",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=10.2,
            leading=11.5,
            textColor=colors.HexColor("#2F5597"),
        ),
        "subsection": ParagraphStyle(
            "subsection",
            parent=base["Normal"],
            fontName="WQY-Bold",
            fontSize=8.6,
            leading=9.7,
            textColor=colors.HexColor("#111111"),
            spaceBefore=1.5,
            spaceAfter=0.8,
        ),
        "normal": ParagraphStyle(
            "normal",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=7.8,
            leading=9.3,
            textColor=colors.HexColor("#202020"),
            spaceAfter=1.3,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            parent=base["Normal"],
            fontName="WQY",
            fontSize=7.4,
            leading=8.7,
            leftIndent=10,
            firstLineIndent=-8,
            textColor=colors.HexColor("#202020"),
            spaceAfter=0.35,
        ),
        "code": ParagraphStyle(
            "code",
            parent=base["Code"],
            fontName="WQY",
            fontSize=7.1,
            leading=8.3,
            textColor=colors.HexColor("#333333"),
            backColor=colors.HexColor("#F6F8FA"),
            leftIndent=8,
            rightIndent=8,
            spaceBefore=1.5,
            spaceAfter=2,
        ),
    }

    story = []
    story.append(p("陈子恒｜AI 产品与自动化工具作品集", styles["title"]))

    story += section("个人定位", styles)
    story.append(p("2027届计算机本科，关注 AI 产品、Workflow、RAG 和 AI 自动化。", styles["normal"]))
    story.append(p("能完成需求拆解、产品流程设计、Demo 搭建和自动化闭环验证。", styles["normal"]))

    story += section("项目 1：企业客服工单自动分派与回复助手", styles)
    story.append(p("项目背景", styles["subsection"]))
    story.append(p("客服工单分类慢、回复口径不统一，高优先级投诉容易遗漏。", styles["normal"]))
    story.append(p("解决方案", styles["subsection"]))
    story.append(p("基于 Dify Workflow + RAG + 影刀 RPA，搭建客服工单自动处理流程。", styles["normal"]))
    story.append(p("核心流程", styles["subsection"]))
    story.append(p("Excel工单 → 影刀读取 → Dify分析 → 分类 / 优先级 / 回复生成 → Excel回写 → 透视表分析", styles["normal"]))
    story.append(p("我的工作", styles["subsection"]))
    for item in [
        "设计 PRD、字段、分类规则、优先级规则和异常流程",
        "搭建 Dify Workflow 和 RAG 知识库",
        "用影刀读取 Excel、调用 Dify API 并回写结果",
        "设计结构化输出字段，便于后续数据分析",
        "用 Excel 透视表分析分类分布、优先级和人工介入率",
    ]:
        story.append(bullet(item, styles["bullet"]))
    story.append(p("截图", styles["subsection"]))
    for item in ["PRD 截图", "Dify Workflow 截图", "影刀流程截图", "Excel 回写截图", "透视表截图"]:
        story.append(bullet(item, styles["bullet"]))

    story += section("项目 2：Y2A-Auto 视频自动化搬运与分发系统", styles)
    story.append(p("项目背景", styles["subsection"]))
    story.append(p("海外视频翻译、字幕生成和多平台分发流程重复、耗时。", styles["normal"]))
    story.append(p("解决方案", styles["subsection"]))
    story.append(p("基于 Y2A-Auto + Python + 影刀 RPA，搭建视频任务批量提交和自动分发流程。", styles["normal"]))
    story.append(p("核心流程", styles["subsection"]))
    story.append(p("Excel视频链接 → 影刀读取 → Python调用API → 生成任务队列 → 自动下载 / 翻译 / 字幕 / 上传", styles["normal"]))
    story.append(p("我的工作", styles["subsection"]))
    for item in [
        "完成 Y2A-Auto Docker 部署和 Cookie 认证配置",
        "分析 Web 表单请求，封装 /tasks/add API",
        "编写 Python 脚本提交视频任务",
        "用影刀打通 Excel → API → 任务队列流程",
        "解决认证、端口、日志报错等部署问题",
    ]:
        story.append(bullet(item, styles["bullet"]))
    story.append(p("截图", styles["subsection"]))
    for item in ["Docker 运行截图", "API 请求截图", "Python 脚本截图", "影刀流程截图", "任务队列截图"]:
        story.append(bullet(item, styles["bullet"]))

    story += section("附录：TrendScout AI", styles)
    story.append(p("简介", styles["subsection"]))
    story.append(p("跨境电商 AI 趋势分析与选品辅助系统。", styles["normal"]))
    story.append(p("核心流程", styles["subsection"]))
    story.append(p("用户输入选品需求 → AI趋势分析 → Trend Score评分 → AI选品报告", styles["normal"]))
    story.append(p("Demo", styles["subsection"]))
    story.append(p("https://trendscout-ai-pied.vercel.app", styles["normal"]))

    story += section("总结", styles)
    story.append(
        p(
            "我关注 AI 产品和自动化工具落地，能把业务问题拆解成流程、字段、规则和 Demo，并用 Dify、RAG、影刀、Python、Excel 等工具跑通 AI 自动化闭环。",
            styles["normal"],
        )
    )

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    main()
