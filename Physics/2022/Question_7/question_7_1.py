from manim import *

from utilitites import stage_setup as stage
from utilitites.box_alignments import get_box_details
from utilitites.latex_utilities import get_the_question, display_paragraphs
from utilitites import latex_utilities as lu
from utilitites import graph_utilities as gu
from utilitites import animations as anim

from settings.class_settings import QuestionScene
from settings import stage_settings as ss
from settings.tex_settings import tick


class Question_7_1(QuestionScene):
    def construct(self):
        titles = ("Question:", "Solution:")
        box_details = get_box_details(box_structure="rr", titles=titles)

        titles, boxes = stage.set_the_stage(
            scene=self,
            title=self.get_the_title(),
            box_details=box_details,
        )

        question_title = titles[0]
        question_kwargs = {
            "tex_environment": lu.get_tabular_environment(p_size=16),
            "font_size": ss.TEX_SIZE
        }
        _ = get_the_question(self, question_title, self.question, **question_kwargs)

