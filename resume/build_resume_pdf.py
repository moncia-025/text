from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "chenziheng_pm_intern_resume.md"
OUTPUT = ROOT / "chenziheng_project_management_intern_resume.pdf"
FONT_PATHS = [
    Path("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"),
    Path("/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf"),
]


def register_font() -> str:
    for font_path in FONT_PATHS:
        if font_path.exists():
            pdfmetrics.registerFont(TTFont("ResumeFont", str(font_path)))
            return "ResumeFont"
    return "Helvetica"


FONT = register_font()
PAGE_WIDTH, PAGE_HEIGHT = A4
LEFT = 36
RIGHT = 36
TOP = 30
BOTTOM = 30
MAX_WIDTH = PAGE_WIDTH - LEFT - RIGHT


def text_width(text: str, size: float) -> float:
    return pdfmetrics.stringWidth(text, FONT, size)


def wrap_text(text: str, size: float, max_width: float) -> list[str]:
    if not text:
        return [""]

    wrapped: list[str] = []
    current = ""
    for char in text:
        candidate = current + char
        if text_width(candidate, size) <= max_width:
            current = candidate
            continue

        if current:
            wrapped.append(current)
        current = char

    if current:
        wrapped.append(current)
    return wrapped


class ResumePDF:
    def __init__(self, output: Path):
        self.canvas = canvas.Canvas(str(output), pagesize=A4)
        self.y = PAGE_HEIGHT - TOP
        self.page_number = 1

    def ensure_space(self, needed: float) -> None:
        if self.y - needed >= BOTTOM:
            return
        self.canvas.showPage()
        self.page_number += 1
        self.y = PAGE_HEIGHT - TOP

    def draw_text(
        self,
        text: str,
        x: float = LEFT,
        size: float = 9.2,
        leading: float = 12.2,
        color=colors.HexColor("#222222"),
        center: bool = False,
    ) -> None:
        self.ensure_space(leading)
        self.canvas.setFont(FONT, size)
        self.canvas.setFillColor(color)
        draw_x = x
        if center:
            draw_x = (PAGE_WIDTH - text_width(text, size)) / 2
        self.canvas.drawString(draw_x, self.y, text)
        self.y -= leading

    def draw_wrapped(
        self,
        text: str,
        x: float = LEFT,
        size: float = 9.1,
        leading: float = 12.1,
        first_prefix: str = "",
        next_prefix: str = "",
        max_width: float | None = None,
    ) -> None:
        width = max_width if max_width is not None else PAGE_WIDTH - x - RIGHT
        prefix_width = text_width(first_prefix, size)
        next_prefix_width = text_width(next_prefix, size)

        first_lines = wrap_text(text, size, width - prefix_width)
        lines: list[tuple[str, str]] = []
        for index, line in enumerate(first_lines):
            prefix = first_prefix if index == 0 else next_prefix
            lines.append((prefix, line))

        self.ensure_space(leading * len(lines))
        self.canvas.setFont(FONT, size)
        self.canvas.setFillColor(colors.HexColor("#222222"))
        for prefix, line in lines:
            self.canvas.drawString(x, self.y, prefix + line)
            self.y -= leading

    def draw_section(self, title: str) -> None:
        self.ensure_space(18)
        self.y -= 2
        self.canvas.setStrokeColor(colors.HexColor("#2CB8B8"))
        self.canvas.setLineWidth(0.9)
        self.canvas.line(LEFT, self.y + 2, PAGE_WIDTH - RIGHT, self.y + 2)
        self.draw_text(title, size=10.5, leading=15, color=colors.HexColor("#111111"))

    def draw_subsection(self, title: str) -> None:
        self.y -= 1
        self.draw_text(title, size=9.7, leading=13, color=colors.HexColor("#111111"))

    def save(self) -> None:
        self.canvas.save()


def clean_line(line: str) -> str:
    return line.replace("**", "").strip()


def render_markdown(source: Path, output: Path) -> None:
    pdf = ResumePDF(output)
    lines = source.read_text(encoding="utf-8").splitlines()

    for raw in lines:
        line = clean_line(raw)
        if not line:
            pdf.y -= 3
            continue

        if line.startswith("# "):
            pdf.draw_text(line[2:], size=17, leading=20, center=True, color=colors.HexColor("#111111"))
            continue

        if line.startswith("## "):
            pdf.draw_section(line[3:])
            continue

        if line.startswith("### "):
            pdf.draw_subsection(line[4:])
            continue

        if line.startswith("- "):
            pdf.draw_wrapped(line[2:], size=8.9, leading=11.7, first_prefix="- ", next_prefix="  ")
            continue

        pdf.draw_wrapped(line.rstrip("  "), size=8.9, leading=11.7)

    pdf.save()


if __name__ == "__main__":
    render_markdown(SOURCE, OUTPUT)
    print(f"Wrote {OUTPUT}")
