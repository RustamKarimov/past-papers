from manim import *

from utilitites import stage_setup as stage
from utilitites.box_alignments import get_box_details


class Question_1_1(Scene):
    def construct(self):
        titles = ("Question", "Diagram", "Solution")
        box_details = get_box_details(box_structure="rcc", titles=titles)

        titles, boxes = stage.set_the_stage(
            scene=self,
            title="PS - 2022 November P1 - Question 1.1",
            box_details=box_details
        )
