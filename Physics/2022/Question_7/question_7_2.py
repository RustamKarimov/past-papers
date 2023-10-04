from manim import *

from utilitites import stage_setup as stage
from utilitites.box_alignments import get_box_details
from utilitites.latex_utilities import get_the_question, display_paragraphs
from utilitites import latex_utilities as lu

from settings.class_settings import QuestionScene
from settings import stage_settings as ss
from settings.tex_settings import tick

from diagram_for_q7 import diagram, diagram_dict, SCALE


class Question_7_2(QuestionScene):
    def construct(self):
        titles = ("Question:", "Diagram:", "Solution:")
        box_sizes = ((0.4, 1), (0.58, 0.56), (0.58, 0.40))
        box_details = get_box_details(box_structure="crr", titles=titles, box_sizes=box_sizes)

        titles, boxes = stage.set_the_stage(
            scene=self,
            title=self.get_the_title(),
            box_details=box_details,
        )

        question_title = titles[0]
        question_kwargs = {
            "tex_environment": lu.get_tabular_environment(p_size=6),
            "font_size": ss.MEDIUM_TEX_SIZE
        }
        _ = get_the_question(self, question_title, self.question, **question_kwargs)

        diagram_box = boxes[1]
        diagram.move_to(diagram_box)
        self.play(FadeIn(diagram[:8]))
        self.wait()

        charge_n = diagram_dict["charge_n"]
        self.play(FadeIn(charge_n))
        self.wait()

        force_g = diagram_dict["force_g"]

        label_g = diagram_dict["label_g"]

        self.play(GrowArrow(force_g))
        self.play(FadeIn(label_g))
        self.wait()

        force_e = diagram_dict["force_e"]

        label_e = diagram_dict["label_e"]

        self.play(GrowArrow(force_e))
        self.play(FadeIn(label_e))
        self.wait()

        solution_title = titles[-1]
        responses = display_paragraphs(self, solution_title, ["Negative"], **question_kwargs)

        tick_1 = tick.copy()
        tick_1.font_size = ss.MEDIUM_TEX_SIZE
        tick_1.next_to(responses[0], RIGHT, buff=0.2)

        self.play(Write(tick_1))
        self.wait()
