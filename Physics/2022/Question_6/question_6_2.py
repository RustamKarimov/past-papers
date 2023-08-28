from manim import *

from pathlib import Path

from utilitites import stage_setup as stage
from utilitites.box_alignments import get_box_details
from utilitites.latex_utilities import get_the_question, display_paragraphs
from utilitites import latex_utilities as lu
from settings.tex_settings import tick

from settings.class_settings import QuestionScene
from settings.stage_settings import MEDIUM_TEX_SIZE


class Question_6_2(QuestionScene):
    def construct(self):
        titles = ("Question:", "Solution:")
        box_sizes = ((1, 0.3), (1, 0.68))
        box_details = get_box_details(box_structure="rr", titles=titles, box_sizes=box_sizes)

        titles, boxes = stage.set_the_stage(
            scene=self,
            title=self.get_the_title(),
            box_details=box_details,
        )

        question_title = titles[0]
        question_kwargs = {"tex_environment": lu.get_tabular_environment(p_size=16)}
        _ = get_the_question(self, question_title, self.question, **question_kwargs)

        solution_title = titles[1]
        response_options = [
            "Measurement of foetal heartbeat.", "OR",
            "Measurement of blood flow.", "OR",
            "Doppler flow meter."
        ]

        responses = display_paragraphs(self, solution_title, response_options, **question_kwargs)

        brace = Brace(responses, RIGHT)

        tick_1 = tick.copy()
        tick_1.font_size = MEDIUM_TEX_SIZE
        tick_1.next_to(brace, RIGHT, buff=0.2)

        self.play(GrowFromCenter(brace))
        self.wait()

        self.play(Write(tick_1))
        self.wait()