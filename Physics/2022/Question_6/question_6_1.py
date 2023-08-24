from manim import *

from pathlib import Path


from utilitites import stage_setup as stage
from utilitites.box_alignments import get_box_details
from utilitites.latex_utilities import get_the_question
from utilitites import latex_utilities as lu

from settings.file_settings import BASE_DIR

class Question_6_1(Scene):
    def __init__(self):
        self.question = BASE_DIR / "Physics" / "2022" / "Question_6" / "question_6_1.txt"
        super().__init__()

    def construct(self):
        titles = ("Question:", "Diagram:", "Solution:")
        box_details = get_box_details(box_structure="rcc", titles=titles)

        titles, boxes = stage.set_the_stage(
            scene=self,
            title="PS - 2022 November P1 - Question 6.1",
            box_details=box_details
        )

        question_title = titles[0]
        question_kwargs = {"tex_environment": lu.get_tabular_environment(p_size=16)}
        get_the_question(self, question_title, self.question, **question_kwargs)
