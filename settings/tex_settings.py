from manim import *


my_template = TexTemplate()
# my_template.add_to_preamble("\setlength{\textW}{\widthof{\alphaber} * \real{3}}")
my_template.add_to_preamble(r"\usepackage{amssymb}")

enum_template = TexTemplate()
enum_template.add_to_preamble(r"\usepackage{enumitem}")

tick = MathTex("\\checkmark", tex_template=my_template)

tex_environment = "\\begin{tabular}{p{18 cm}}{\\flushleft}"
half_tex_environment = "\\begin{tabular}{p{8 cm}}{\\flushleft}"


READING_SPEED = 20  # Characters per second
