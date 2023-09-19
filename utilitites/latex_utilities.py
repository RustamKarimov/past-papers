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


def get_tabular_environment(p_size: int = 18, alignment: str = "flushleft") -> str:
    """
    Generates a tabular environment with a respective paragraph size.
    :param p_size: the size of the paragraph line
    :param alignment: Alignment style of the text in the paragraph.
    :return: String containing the tex_environment
    """
    tex_environment = f"\\begin{{tabular}}{{p{{{p_size} cm}}}}{{\\{alignment}}}"
    return tex_environment


def read_the_text_file(question: Path = None) -> list:
    """
    Reads the contents of a text file and splits it into paragraphs
    :param question: The question file where all the text is stored
    :return: list of paragraphs
    """
    if question is None:
        raise ValueError("Question path is not defined")

    with open(question) as file:
        lines = file.read().splitlines()
        return lines


def display_a_paragraph(scene: Scene, tex_mobject: Tex) -> None:
    """
    Calculates the length of a paragraph and then average time it takes to read the paragraph.
    The number of characters which can be read in 1 second is stored in READING_SPEED variable.
    This variable can be adjusted in the tex_settings.py.
    :param scene: A scene where the paragraph will be displayed
    :param tex_mobject: A mobject which  will be displayed
    :return: None
    """
    length_of_tex = len(tex_mobject)
    run_time = length_of_tex // READING_SPEED + 1

    scene.play(Create(tex_mobject), run_time=run_time)
    scene.wait()


def display_paragraphs(scene: Scene, align_to: Tex, paragraphs: list, **kwargs) -> VGroup:
    """
    Animates and displays the tex paragraphs on the scene.
    :param scene: The scene where paragraphs will be displayed
    :param align_to: A reference mobject for the alignment of paragraphs
    :param paragraphs: A list of paragraph texts
    :param kwargs: extra parameters
    :return: Vgroup consisting of paragraph mobjects
    """
    alignment = align_to
    tex_kwargs = {**default_kwargs, **kwargs}
    paragraph_group = VGroup()
    for paragraph in paragraphs:
        print(paragraph)
        paragraph_tex = Tex(paragraph, **tex_kwargs)[0]
        paragraph_tex.next_to(alignment, DOWN, buff=0.3, aligned_edge=LEFT)
        alignment = paragraph_tex
        display_a_paragraph(scene, paragraph_tex)
        paragraph_group.add(paragraph_tex)

    return paragraph_group


def get_the_question(scene: Scene, align_to: Tex, question: Path = None, **kwargs) -> VGroup:
    """
    Reads the question text from the provided path and then
    animates and displays them on the provided scene. provided text
    is aligned to the mobject provided as the align_to.
    :param scene: Scene on which the question will be displayed
    :param align_to: A reference object for the alignment
    :param question: The path to the question containing the text
    :param kwargs: any extra parameters
    :return: Vgroup() consisting of paragraph mobjects
    """
    paragraphs = read_the_text_file(question)
    return display_paragraphs(scene, align_to, paragraphs, **kwargs)
