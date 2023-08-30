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


class Question_6_5(QuestionScene):
    def construct(self):
        titles = ("Question:", "Solution:")
        box_details = get_box_details(box_structure="cc", titles=titles)

        titles, boxes = stage.set_the_stage(
            scene=self,
            title=self.get_the_title(),
            box_details=box_details,
        )

        question_title = titles[0]
        question_kwargs = {
            "tex_environment": lu.get_tabular_environment(p_size=6),
            "font_size": ss.TEX_SIZE
        }
        paragraphs = get_the_question(self, question_title, self.question, **question_kwargs)

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
        graph.scale(1.8).move_to(graph_box).shift(DOWN * 0.8)
        self.play(FadeIn(graph))
        self.wait()

        tex_kwargs = {"font_size": ss.TEX_SIZE, "color": ss.TEXT_COLOR}
        label_a = Tex("A", **tex_kwargs)
        label_b = Tex("B", **tex_kwargs)

        plot = graph_dict["plot"]
        label_a.next_to(plot.get_end(), UR, buff=0.1)

        self.play(Write(label_a))
        self.wait()

        eq_kwargs = {
            "font_size": ss.MEDIUM_TEX_SIZE,
            "color": ss.TEXT_COLOR
        }

        equations = MathTex(
            "Gradient = \\frac {\\Delta y} {\\Delta x} = ",
            "\\frac {f_L} {f_s} = \\frac {v + v_L} {v}",
            **eq_kwargs
        ).next_to(graph, UP)

        self.play(FadeIn(equations[1]))
        self.wait()
        self.play(FadeIn(equations[0]))
        self.wait()

        frame_1 = SurroundingRectangle(equations[1][7:11])
        self.play(Create(frame_1), rate_func=rate_functions.there_and_back, run_time=3)

        axes = graph_dict["axes"]
        plot_2 = axes.plot(
            function=lambda x: x * 1.6,
            x_range=[0, 0.5]
        )
        label_b.next_to(plot_2.get_end(), UR, buff=0.1)
        self.play(ReplacementTransform(plot.copy(), plot_2), run_time=3)
        self.play(Write(label_b))
        self.wait()

        tick_1 = tick.copy()
        tick_1.font_size = ss.MEDIUM_TEX_SIZE
        tick_1.next_to(plot_2.get_end(), LEFT, buff=0.2)
        tick_2 = tick_1.copy()
        tick_2.next_to(tick_1, LEFT, buff=0.05)

        self.play(Write(tick_2))
        self.wait()
        self.play(Write(tick_1))
        self.wait()
