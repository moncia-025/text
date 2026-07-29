from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


OUT_FILE = Path("chen-ziheng-tutor-resume-final.pdf")
FONT_PATH = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
FONT_NAME = "WenQuanYiMicroHei"


def width(text: str, size: float) -> float:
    return pdfmetrics.stringWidth(text, FONT_NAME, size)


def wrap_text(text: str, max_width: float, size: float) -> list[str]:
    lines: list[str] = []
    current = ""
    for char in text:
        candidate = current + char
        if width(candidate, size) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = char
    if current:
        lines.append(current)
    return lines


def draw_section(c: canvas.Canvas, title: str, y: float, page_width: float) -> float:
    x = 24
    label_w = max(88, width(title, 13) + 34)
    label_h = 21
    c.setFillColorRGB(0, 0, 0)
    c.setStrokeColorRGB(0, 0, 0)
    c.line(x, y - label_h - 3, page_width - 26, y - label_h - 3)
    c.saveState()
    c.translate(x, y - label_h)
    c.beginPath()
    path = c.beginPath()
    path.moveTo(0, 0)
    path.lineTo(label_w, 0)
    path.lineTo(label_w - 14, label_h)
    path.lineTo(0, label_h)
    path.close()
    c.drawPath(path, stroke=0, fill=1)
    c.restoreState()
    c.setFillColorRGB(1, 1, 1)
    c.setFont(FONT_NAME, 13)
    c.drawString(x + 18, y - 15, title)
    c.setFillColorRGB(0, 0, 0)
    return y - label_h - 16


def draw_wrapped(c: canvas.Canvas, text: str, x: float, y: float, max_width: float, size: float, leading: float) -> float:
    for line in wrap_text(text, max_width, size):
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_bullet(c: canvas.Canvas, text: str, x: float, y: float, max_width: float, size: float = 8.6) -> float:
    c.setFont(FONT_NAME, size)
    c.drawString(x, y, "•")
    return draw_wrapped(c, text, x + 13, y, max_width - 13, size, 12.2)


def main() -> None:
    pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))

    c = canvas.Canvas(str(OUT_FILE), pagesize=A4)
    page_width, page_height = A4

    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(0, 0, 0)

    # Header.
    c.setLineWidth(2.6)
    c.line(0, page_height - 5, page_width, page_height - 5)
    c.line(0, page_height - 63, page_width, page_height - 63)
    c.setFont(FONT_NAME, 25)
    c.drawString(52, page_height - 43, "个人简历")
    c.setFont(FONT_NAME, 11.8)
    c.drawString(176, page_height - 39, "求职意向：小学 / 初中数学家教老师")
    for cx in (512, 530, 548):
        c.circle(cx, page_height - 30, 10.5, stroke=1, fill=0)

    y = page_height - 82

    # Personal information.
    y = draw_section(c, "个人信息", y, page_width)
    c.setFont(FONT_NAME, 9.8)
    left_x, right_x = 42, 300
    row_gap = 20
    rows = [
        ("姓名：陈子恒", "求职方向：数学家教老师"),
        ("手机号码：151-3734-2002", "可辅导：小学数学 / 初中数学 / 英语基础 / 初中化学基础"),
        ("邮箱：xigua050205@163.com", "年级：本科在读，2027届"),
        ("学校：新乡工程学院", "专业：计算机科学与技术"),
    ]
    for left, right in rows:
        c.drawString(left_x, y, left)
        c.drawString(right_x, y, right)
        y -= row_gap
    y += 3

    # Education.
    y = draw_section(c, "教育背景", y, page_width)
    c.setFont(FONT_NAME, 10)
    c.drawString(42, y, "2023.09 - 2027.06")
    c.drawString(188, y, "新乡工程学院")
    c.drawString(330, y, "计算机科学与技术")
    c.drawString(488, y, "本科在读")
    y -= 12

    # Strengths.
    y = draw_section(c, "核心优势", y, page_width)
    strengths = [
        "教学耐心细致：能根据学生接受能力调整讲解方式，遇到基础薄弱或理解较慢的学生，会拆分知识点、反复举例，帮助学生逐步建立信心。",
        "熟悉小学、初中学习重点：了解小学计算、应用题、基础概念，以及初中数学方程、函数、几何等常见重难点；也能辅导初中化学基础内容。",
        "注重基础巩固：不单纯追求刷题数量，更重视学生是否真正理解知识点，帮助学生整理错题、发现薄弱环节。",
        "沟通积极，家长满意度较高：课后及时反馈学习情况、课堂表现和后续建议，家长普遍认可教学态度认真、沟通负责。",
        "成绩提升稳扎稳打：辅导过程中重视小幅、持续的进步，帮助学生减少低级错误，提高作业完成质量和考试稳定性。",
    ]
    for item in strengths:
        y = draw_bullet(c, item, 42, y, page_width - 78)
        y -= 1.2

    # Teaching experience.
    y = draw_section(c, "教学经历", y, page_width)
    experiences = [
        (
            "线上英语辅导｜小学五年级学生｜基础巩固与作业辅导",
            "辅导单词记忆、课文朗读、基础语法和日常作业。学生前期单词记忆不稳定、兴趣不高，后通过分模块记忆、课前复习和简单口语互动，作业错误率有所下降，课堂参与度有一定提升。",
        ),
        (
            "线下数学辅导｜小学四年级学生｜计算能力与应用题提升",
            "针对计算不细心、应用题读题困难的问题，重点辅导四则运算、单位换算和常见应用题。辅导后学生计算步骤更规范，能主动圈画关键词，阶段测试成绩有小幅提升。",
        ),
        (
            "线下数学辅导｜初一学生｜基础知识与几何入门",
            "围绕有理数运算、一元一次方程、几何初步等内容展开。通过知识点拆解、例题讲解和错题复盘，帮助学生理清解题步骤，作业完成速度和正确率有所改善。",
        ),
        (
            "初中化学基础辅导｜初二学生｜化学兴趣与基础入门",
            "讲解物质变化、常见元素、化学符号、简单化学式等入门内容。通过生活例子结合课本知识，帮助学生理解基础概念，降低对化学新学科的陌生感。",
        ),
        (
            "初中化学基础辅导｜初二学生｜实验现象与基础题训练",
            "针对实验现象和基础判断题掌握不稳定的问题，重点讲解常见物质性质、简单实验现象描述和基础题。辅导后学生基础题正确率有小幅提升，学习主动性有所增强。",
        ),
    ]
    for title, body in experiences:
        c.setFont(FONT_NAME, 9)
        c.drawString(42, y, "• " + title)
        y -= 12.3
        c.setFont(FONT_NAME, 8.3)
        y = draw_wrapped(c, body, 55, y, page_width - 92, 8.3, 11.2)
        y -= 2.2

    # Self evaluation.
    y = draw_section(c, "自我评价", y, page_width)
    c.setFont(FONT_NAME, 8.3)
    evaluation = (
        "本人性格耐心、责任心较强，能够认真对待每一次辅导。教学过程中注重因材施教，会根据学生基础和接受能力调整讲解方式，"
        "帮助学生从基础知识开始逐步提升。熟悉小学、初中阶段常见学习重点和易错点，能够通过错题整理、知识点回顾和针对性练习，"
        "帮助学生稳步提高学习状态。与学生相处较亲和，能够引导学生主动思考；与家长沟通及时，愿意根据反馈调整教学安排。"
        "整体教学风格踏实、细致，重视学生的持续进步。"
    )
    draw_wrapped(c, evaluation, 42, y, page_width - 78, 8.3, 11.2)

    c.showPage()
    c.save()


if __name__ == "__main__":
    main()
