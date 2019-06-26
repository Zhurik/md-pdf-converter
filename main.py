from markdown import markdown
from xhtml2pdf import pisa
from os import path
from typing import Optional, List
from pathlib import Path
import argparse
import sys

# Должна быть в файле, на месте пути к шрифтам
PLACEHOLDER = "<--!-->"

DEFAULT_FONT = "Roboto-Regular.ttf"


def convert_md_to_pdf(
    md_path: str,
    style_path: str,
    pdf_path: str,
    font_path: str,
    pdf_name: Optional[str]=None
) -> str:
    """
    Функция для создания pdf из MD файла
    """

    style_file = Path(style_path)

    if style_file.exists():
        with open(style_file, "r") as file:
            style = file.read()
    else:
        return "Не найден файл стилей!"

    font_file = Path(font_path)

    if font_file.exists():
        style = style.replace(PLACEHOLDER, str(font_file.absolute()))
    else:
        return "Не найден файл шрифтов!"

    md_file = Path(md_path)

    if md_file.exists():
        with open(md_file, "r", encoding="utf-8") as file:
            html = style + markdown(file.read())
    else:
        return "Не найден файл для конвертации!"

    if pdf_name is None:
        # Получаем название файла
        pdf_name = md_file.parts[-1].split(".")[0]
        pdf_file = Path(pdf_path + pdf_name + ".pdf")
    else:
        pdf_file = Path(pdf_path + pdf_name)

    with open(pdf_file, "w+b") as file:
        pisa.CreatePDF(
            html.encode("utf-8"),
            encoding="utf-8",
            dest=file
        )

    return ""


def parse_args(
    args: List[str]
) -> argparse.Namespace:
    """
    Функция для парсинга аргументов командной строки
    """

    parser = argparse.ArgumentParser(
        description="Инструмент конвертации MD в PDF"
    )

    parser.add_argument(
        "-m",
        "--md",
        help="Файл MD",
        required=False,
        dest="md_path",
        type=str,
        metavar="file",
        default="README.MD"
    )

    parser.add_argument(
        "-s",
        "--style",
        help="Файл стилей",
        required=False,
        dest="style_path",
        type=str,
        metavar="file",
        default="style.html"
    )

    parser.add_argument(
        "-p",
        "--pdf",
        help="Файл PDF",
        required=False,
        dest="pdf_name",
        type=str,
        metavar="name",
        default=None
    )

    parser.add_argument(
        "-d",
        "--directory",
        help="Директория для PDF",
        required=False,
        dest="pdf_path",
        type=str,
        metavar="dir",
        default=""
    )

    parser.add_argument(
        "-f",
        "--font",
        help="Шрифт с кириллицей для PDF",
        required=False,
        dest="font_path",
        type=str,
        metavar="file",
        default=DEFAULT_FONT
    )

    return parser.parse_args(args)


def main():
    # Парсим аргументы командной строки
    args = parse_args(sys.argv[1:])

    result = convert_md_to_pdf(
        args.md_path,
        args.style_path,
        args.pdf_path,
        args.font_path,
        pdf_name=args.pdf_name
    )

    if not result:
        print("Конвертация прошла успешно!")
    else:
        print(result)


if __name__ == "__main__":
    main()
