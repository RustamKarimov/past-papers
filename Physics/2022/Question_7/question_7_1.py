from manim import *

from utilitites import stage_setup as stage
from utilitites.box_alignments import get_box_details
from utilitites.latex_utilities import get_the_question, display_paragraphs
from utilitites import latex_utilities as lu

from physics_packages.definitions import COULOMBS_LAW

from settings.class_settings import QuestionScene
from settings import stage_settings as ss
from settings.tex_settings import tick


class Question_7_1(QuestionScene):
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
        question_kwargs = {
            "tex_environment": lu.get_tabular_environment(p_size=13),
            "font_size": ss.TEX_SIZE
        }
        _ = get_the_question(self, question_title, self.question, **question_kwargs)

        solution_title = titles[1]
        response = display_paragraphs(self, solution_title, [COULOMBS_LAW], **question_kwargs)[0]

        self.play(FadeToColor(response[17:35], YELLOW))
        self.wait()
        self.play(
            FadeToColor(response[69:101], YELLOW),
            FadeToColor(response[116:128], YELLOW),
        )
        self.wait()
        self.play(FadeToColor(response[-57:-1], YELLOW))
        self.wait()

        tick_1 = tick.copy()
        tick_1.font_size = ss.MEDIUM_TEX_SIZE
        tick_1.next_to(response[-1], RIGHT, buff=0.2).shift(UP * 0.1)
        tick_2 = tick_1.copy()
        tick_2.next_to(tick_1, RIGHT, buff=0.05)

        self.play(Write(tick_1), Write(tick_2))
        self.wait()
