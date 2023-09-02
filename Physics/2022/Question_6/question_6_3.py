from manim import *

from utilitites import stage_setup as stage
from utilitites.box_alignments import get_box_details
from utilitites.latex_utilities import get_the_question, display_paragraphs
from utilitites import latex_utilities as lu
from utilitites import graph_utilities as gu

from settings.class_settings import QuestionScene
from settings.stage_settings import MEDIUM_TEX_SIZE
from settings.tex_settings import tick
from settings import graph_settings as gs


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

        plot_settings = gs.PlotSettings()
        x_label_settings = gs.AxisLabelSettings(
            axis="x",
            label="f_s (Hz)",
            edge=DOWN,
            direction=DOWN
        )
        y_label_settings = gs.AxisLabelSettings(
            axis="y",
            label="f_L (Hz)",
            edge=LEFT,
            direction=LEFT,
            angle=PI / 2,
            buff=0.05
        )
        graph_settings = gs.GraphSettings(
            x_label_settings=x_label_settings,
            y_label_settings=y_label_settings,
            plot_settings=plot_settings
        )

        graph, graph_parts = gu.generate_the_graph(graph_settings)
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