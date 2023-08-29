from manim import *

from utilitites import stage_setup as stage
from utilitites.box_alignments import get_box_details
from utilitites.latex_utilities import get_the_question, display_paragraphs
from utilitites import latex_utilities as lu
from utilitites import graph_utilities as gu
from utilitites import animations as anim

from settings.class_settings import QuestionScene
from settings import stage_settings as ss


class Question_6_4(QuestionScene):
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
        solution_box = boxes[2]

        eq_kwargs = {
            "font_size": ss.SMALL_TEX_SIZE,
            "color": ss.TEXT_COLOR
        }

        equations = MathTex(
            "Gradient = \\frac {\\Delta y} {\\Delta x}",
            "= \\frac {f_L} {f_s}",
            "=1,06",
            "f_L = \\frac {v \\pm v_L} {v \\pm v_s} f_s",
            "\\frac {f_L} {f_s} = \\frac {v \\pm v_L} {v \\pm v_s}",
            "1,06 = \\frac {340 + v_L} {340}",
            "1,06 \\times 340 = 340 + v_L",
            "360,4 = 340 + v_L",
            "360,4 - 340 = v_L",
            "v_L = 20,4 m \\times s^{-1}",
            **eq_kwargs
        )

        equations_group = VGroup(
            equations[:2],
            VGroup(equations[3], equations[4]).arrange(RIGHT * 2),
            VGroup(equations[5], equations[6]).arrange(RIGHT * 2),
            VGroup(equations[7], equations[8]).arrange(RIGHT * 2),
            equations[9]
        ).arrange(DOWN).move_to(solution_box)

        self.play(FadeIn(equations[0]))
        self.wait()

        axes = graph_dict["axes"]
        plot = graph_dict["plot"]
        x_label = graph_dict["x_label"]

        plot_axes = axes.get_lines_to_point(plot.get_end())
        self.play(Create(plot_axes))
        self.wait()

        x_intercept = axes.coords_to_point(0.8, 0, 0)

        y_brace = BraceBetweenPoints(
            plot.get_end(),
            x_intercept,
            RIGHT
        )
        delta_y = MathTex("\\Delta y", "=f_L", **eq_kwargs)
        delta_y.next_to(y_brace, RIGHT, buff=0.1)

        x_brace = BraceBetweenPoints(
            plot.get_start(),
            x_intercept,
            DOWN
        )
        delta_x = MathTex("\\Delta x", "=f_s", **eq_kwargs)
        delta_x.next_to(x_brace, DOWN, buff=0.1)

        self.play(GrowFromCenter(y_brace))
        self.wait()
        self.play(Create(delta_y))
        self.wait()

        self.play(GrowFromCenter(x_brace), x_label.animate.shift(RIGHT))
        self.wait()
        self.play(Create(delta_x))
        self.wait()

        transform_matrix = [
            [0, 1, 2, 3, 5, 6, 7, 8, 11, 20, 23, 24, 25, 26, 27],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        ]

        anim.get_equation_transform(self, equations[0], equations[1], transform_matrix, run_time=2)
