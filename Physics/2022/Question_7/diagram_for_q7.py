from manim import *

from settings import stage_settings as ss

SCALE = 0.4
tex_kwargs = {
    "font_size": ss.BIG_TEX_SIZE,
    "color": ss.TEXT_COLOR
}

ceiling = Line().scale(2)
m_label = Tex("M", font_size=ss.BIG_TEX_SIZE, color=ss.BACKGROUND_COLOR)
n_label = Tex("N", font_size=ss.BIG_TEX_SIZE, color=ss.BACKGROUND_COLOR)
sphere_M = LabeledDot(m_label, radius=0.5)
sphere_M.next_to(ceiling, DOWN, buff=1.25)
sphere_N = LabeledDot(n_label, radius=0.5)
sphere_N.next_to(sphere_M, DOWN, buff=2)

tension = Line(ceiling.get_bottom(), sphere_M.get_top(), buff=0)
dash_m = DashedLine().scale(0.5).next_to(sphere_M, RIGHT, buff=0)
dash_n = dash_m.copy().next_to(sphere_N, RIGHT, buff=0)
arrow = DoubleArrow(dash_m.get_right(), dash_n.get_right(), max_tip_length_to_length_ratio=0.2, buff=0)

distance = Tex("0.3 m", **tex_kwargs)
distance.next_to(arrow, RIGHT)

charge_n = MathTex("Q_N = +8.6 \\times 10^{-8} \\, C", **tex_kwargs)
charge_n.color = YELLOW
charge_n.next_to(sphere_N, LEFT, buff=0.1)

force_g = Arrow(max_tip_length_to_length_ratio=0.2, color=YELLOW).rotate(270 * DEGREES)
force_g.next_to(sphere_N, DOWN, buff=0)

force_e = Arrow(max_tip_length_to_length_ratio=0.2, color=YELLOW).rotate(90 * DEGREES)
force_e.next_to(sphere_N, UP, buff=0)

label_g = MathTex("F_g", **tex_kwargs)
label_g.color = YELLOW
label_g.next_to(force_g.get_end(), RIGHT, buff=0.2)

label_e = MathTex("F_e", **tex_kwargs)
label_e.color = YELLOW
label_e.next_to(force_e.get_end(), LEFT, buff=0.2)

keys = (
    "ceiling", "sphere_m", "sphere_n", "tension", "dash_m", "dash_n", "arrow", "distance",
    "charge_n", "force_g", "force_e", "label_g", "label_e"
)
items = (
    ceiling, sphere_M, sphere_N, tension, dash_m, dash_n, arrow, distance,
    charge_n, force_g, force_e, label_g, label_e
)

diagram_dict = dict(zip(keys, items))
diagram = VGroup(*items).scale(SCALE)
