from manim import *

from utilitites import stage_setup as stage
from settings.box_alignments import get_box_details


class Question_1_1(Scene):
    def construct(self):
        titles = ("Question", "Diagram", "Solution")
        box_details = get_box_details("rcc", titles)

        titles, boxes = stage.set_the_stage(
            self,
            "PS - 2022 November P1 - Question 1.1",
            box_details
        )