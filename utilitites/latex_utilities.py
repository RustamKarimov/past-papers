from manim import *

from pathlib import Path

from settings import stage_settings as ss
from settings import tex_settings as ts
from settings.tex_settings import READING_SPEED

default_kwargs = {
    "font_size": ss.MEDIUM_TEX_SIZE,
    "color": ss.TEXT_COLOR,
    "tex_environment": ts.tex_environment
}


def get_tabular_environment(p_size=18, alignment="flushleft"):
    tex_environment = f"\\begin{{tabular}}{{p{{{p_size} cm}}}}{{\\{alignment}}}"
    return tex_environment


def read_the_text_file(question: Path = None):
    if question is None:
        raise ValueError("Question path is not defined")

    with open(question) as file:
        lines = file.read().splitlines()
        return lines


def display_a_paragraph(scene: Scene, tex_mobject):
    length_of_tex = len(tex_mobject)
    run_time = length_of_tex // READING_SPEED

    scene.play(Create(tex_mobject), run_time=run_time)
    scene.wait()


def display_paragraphs(scene: Scene, align_to: Tex, paragraphs, **kwargs):
    alignment = align_to
    tex_kwargs = {**default_kwargs, **kwargs}
    for paragraph in paragraphs:
        paragraph_tex = Tex(paragraph, **tex_kwargs)[0]
        paragraph_tex.next_to(alignment, DOWN, buff=0.3, aligned_edge=LEFT)
        alignment = paragraph_tex
        display_a_paragraph(scene, paragraph_tex)


def get_the_question(scene: Scene, align_to: Tex, question: Path = None, **kwargs):
    paragraphs = read_the_text_file(question)
    display_paragraphs(scene, align_to, paragraphs, **kwargs)
