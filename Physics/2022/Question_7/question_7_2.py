from manim import *

from utilitites import stage_setup as stage
from utilitites.box_alignments import get_box_details
from utilitites.latex_utilities import get_the_question
from utilitites import latex_utilities as lu

from settings.class_settings import QuestionScene
from settings import stage_settings as ss
# from settings.tex_settings import tick

from diagram_for_q7 import diagram


class Question_7_2(QuestionScene):
    def construct(self):
        titles = ("Question:", "Diagram:", "Solution:")
        box_sizes = ((0.4, 1), (0.58, 0.48), (0.58, 0.48))
        box_details = get_box_details(box_structure="crr", titles=titles, box_sizes=box_sizes)

        titles, boxes = stage.set_the_stage(
            scene=self,
            title=self.get_the_title(),
            box_details=box_details,
        )

        # question_title = titles[0]
        # question_kwargs = {
        #     "tex_environment": lu.get_tabular_environment(p_size=6),
        #     "font_size": ss.MEDIUM_TEX_SIZE
        # }
        # _ = get_the_question(self, question_title, self.question, **question_kwargs)

        diagram_box = boxes[1]
        diagram.move_to(diagram_box)
        self.play(FadeIn(diagram))
        self.wait()

        Tex()