from manim import *

from pathlib import Path


from utilitites import stage_setup as stage
from utilitites.box_alignments import get_box_details
from utilitites.latex_utilities import get_the_question, display_paragraphs
from utilitites import latex_utilities as lu
from utilitites import graph_utilities as gu

from settings.file_settings import BASE_DIR
from settings.tex_settings import tick
from settings.stage_settings import MEDIUM_TEX_SIZE


class Question_6_1(Scene):
    def __init__(self):
        self.question = BASE_DIR / "Physics" / "2022" / "Question_6" / "question_6_1.txt"
        super().__init__()

    def construct(self):
        titles = ("Question:", "Graph:", "Solution:")
        box_sizes = ((1, 0.4), (0.49, 0.58), (0.49, 0.58))
        box_details = get_box_details(box_structure="rcc", titles=titles, box_sizes=box_sizes)

        for detail in box_details:
            print(detail)

        titles, boxes = stage.set_the_stage(
            scene=self,
            title="PS - 2022 November P1 - Question 6.1",
            box_details=box_details
        )

        question_title = titles[0]
        question_kwargs = {"tex_environment": lu.get_tabular_environment(p_size=16)}
        _ = get_the_question(self, question_title, self.question, **question_kwargs)

        graph_box = boxes[1]
        graph_kwargs = {
            "graph_kwargs": {},
            "x_label_kwargs": {
                "x_label": "f_s (Hz)",
                "x_label_edge": DOWN,
                "x_label_direction": DOWN,
            },
            "y_label_kwargs": {
                "y_label": "f_L (Hz)",
                "y_label_edge": LEFT,
                "y_label_direction": LEFT,
                "y_label_rotation": PI / 2,
                "y_label_buff": 0.05
            },
            "plot_kwargs": {}
        }

        graph, graph_dict = gu.get_the_graph(graph_kwargs)
        graph.move_to(graph_box)
        self.play(FadeIn(graph))
        self.wait()

        solution_title = titles[2]
        response = "Doppler effect"
        solution_kwargs = {"tex_environment": lu.get_tabular_environment(p_size=7)}
        responses = display_paragraphs(self, solution_title, [response], **solution_kwargs)

        tick_1 = tick.copy()
        tick_1.font_size = MEDIUM_TEX_SIZE
        tick_1.next_to(responses[0], RIGHT, buff=0.2)

        self.play(Write(tick_1))
        self.wait()
        