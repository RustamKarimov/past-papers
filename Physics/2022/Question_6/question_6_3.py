from manim import *

from utilitites import stage_setup as stage
from utilitites.box_alignments import get_box_details
from utilitites.latex_utilities import get_the_question, display_paragraphs
from utilitites import latex_utilities as lu
from utilitites import graph_utilities as gu

from settings.class_settings import QuestionScene
from settings.stage_settings import MEDIUM_TEX_SIZE
from settings.tex_settings import tick
from settings.graph_settings import PlotSettings


class Question_6_3(QuestionScene):
    def construct(self):
        titles = ("Question:", "Graph:", "Solution:")
        box_sizes = ((1, 0.4), (0.49, 0.58), (0.49, 0.58))
        box_details = get_box_details(box_structure="rcc", titles=titles, box_sizes=box_sizes)

        titles, boxes = stage.set_the_stage(
            scene=self,
            title=self.get_the_title(),
            box_details=box_details,
        )

        question_title = titles[0]
        question_kwargs = {"tex_environment": lu.get_tabular_environment(p_size=16)}
        _ = get_the_question(self, question_title, self.question, **question_kwargs)

        graph_box = boxes[1]
        plot_settings = PlotSettings()
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
            "plot_kwargs": plot_settings
        }

        graph, graph_dict = gu.get_the_graph(graph_kwargs)
        graph.move_to(graph_box)
        self.play(FadeIn(graph))
        self.wait()

        solution_title = titles[2]
        response_options = [
            "$f_L \\propto F_s$", "OR",
            "Directly proportional."
        ]

        responses = display_paragraphs(self, solution_title, response_options, **question_kwargs)

        brace = Brace(responses, RIGHT)

        tick_1 = tick.copy()
        tick_1.font_size = MEDIUM_TEX_SIZE
        tick_1.next_to(brace, RIGHT, buff=0.2)

        underline = Underline(responses[-1][:8])

        self.play(Create(underline))
        self.wait()

        self.play(GrowFromCenter(brace))
        self.wait()

        self.play(Write(tick_1))
        self.wait()