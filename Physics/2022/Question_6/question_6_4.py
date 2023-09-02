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
from settings import graph_settings as gs


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
        paragraphs = get_the_question(self, question_title, self.question, **question_kwargs)

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
        solution_box = boxes[2]

        eq_kwargs = {
            "font_size": ss.SMALL_TEX_SIZE,
            "color": ss.TEXT_COLOR
        }

        equations = MathTex(
            "Gradient = \\frac {\\Delta y} {\\Delta x}",
            "= \\frac {f_L} {f_s}",
            "= 1,06",
            "f_L = \\frac {v \\pm v_L} {v \\pm v_s} \\times f_s",
            "\\frac {f_L} {f_s} = \\frac {v \\pm v_L} {v \\pm v_s}",
            "1,06 = \\frac {340 + v_L} {340}",
            "1,06 \\times 340 = 340 + v_L",
            "360,4 = 340 + v_L",
            "360,4 - 340 = v_L",
            "v_L = 20,4 \\, m \\times s^{-1}",
            **eq_kwargs
        )

        VGroup(
            equations[:3],
            VGroup(equations[3], equations[4]).arrange(RIGHT * 6),
            VGroup(equations[5], equations[6]).arrange(RIGHT * 6),
            VGroup(equations[7], equations[8]).arrange(RIGHT * 6),
            equations[9]
        ).arrange(DOWN).move_to(solution_box)

        self.play(FadeIn(equations[0]))
        self.wait()

        axes = graph_parts.axes
        plot = graph_parts.plot
        x_label = graph_parts.x_label

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
            [8, 9, 10, 11, 12, 13],
            [0, 1, 2, 3, 4, 5]
        ]

        anim.get_equation_transform(self, equations[0], equations[1], transform_matrix, run_time=2)

        transform_matrix = [
            [0, 1, 3, 4, 5],
            [0, 1, 2, 3, 4]
        ]

        anim.get_equation_transform(self, equations[1], equations[2], transform_matrix, run_time=2)

        self.play(
            Indicate(equations[2]),
            Indicate(paragraphs[0][-5:-1]),
            run_time=2
        )
        self.wait()

        self.play(FadeIn(equations[3]))
        self.wait()

        transform_matrix = [
            [0, 1, -3, -2, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            list(range(15))
        ]

        anim.get_equation_transform(self, equations[3], equations[4], transform_matrix, run_time=2)

        transform_matrix = [
            [0, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13],
            list(range(15))
        ]

        anim.get_equation_transform(self, equations[4], equations[5], transform_matrix, run_time=2)

        frame_1 = SurroundingRectangle(equations[:3], stroke_width=1)
        frame_2 = SurroundingRectangle(equations[4][:5], stroke_width=1)
        frame_3 = SurroundingRectangle(equations[5][:4], stroke_width=1)

        self.play(
            Create(frame_1), Create(frame_2), Create(frame_3),
            rate_func=rate_functions.there_and_back,
            run_time=5
        )
        self.wait()

        self.play(
            Indicate(equations[5][5:8]),
            Indicate(equations[5][-3:]),
            Indicate(paragraphs[1][24:32]),
            run_time=3,
        )
        self.wait()

        transform_matrix = [
            [0, 1, 2, 3, -4, -3, -3, -1, 4, 5, 6, 7, 8, 9, 10],
            list(range(15))
        ]

        anim.get_equation_transform(self, equations[5], equations[6], transform_matrix, run_time=2)

        transform_matrix = [
            [0, 0, 0, 1, 4, 8, 9, 10, 11, 12, 13, 14],
            list(range(12))
        ]

        anim.get_equation_transform(self, equations[6], equations[7], transform_matrix, run_time=2)

        transform_matrix = [
            [0, 1, 2, 3, 4, 9, 6, 7, 8, 5, 10, 11],
            list(range(12))
        ]

        anim.get_equation_transform(self, equations[7], equations[8], transform_matrix, run_time=2)

        transform_matrix = [
            [-2, -1, -3, 0, 2, 3, 4, 4, 5, 6, 7, 8],
            list(range(13))
        ]

        anim.get_equation_transform(self, equations[8], equations[9], transform_matrix, run_time=2)

        tick_1 = tick.copy()
        tick_1.font_size = ss.MEDIUM_TEX_SIZE
        tick_1.next_to(equations[3], RIGHT, buff=0.2)

        tick_2 = tick_1.copy()
        tick_2.next_to(equations[5], LEFT, buff=0.1)
        tick_3 = tick_1.copy()
        tick_3.next_to(tick_2, LEFT, buff=0.05)

        tick_4 = tick_1.copy()
        tick_4.next_to(equations[5], RIGHT, buff=0.2)

        tick_5 = tick_1.copy()
        tick_5.next_to(equations[9], RIGHT, buff=0.2)

        ticks = [tick_1, tick_2, tick_3, tick_4, tick_5]

        for a_tick in ticks:
            self.play(Write(a_tick))
            self.wait()
