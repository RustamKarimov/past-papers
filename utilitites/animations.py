from manim import *


def get_equation_transform(
        scene: Scene,
        equation_1: MathTex,
        equation_2: MathTex,
        transform_index: list,
        run_time: int = 3) -> None:
    """
    Transforms one equation to another one. To do so it is using transformation matrix with indexes of each equation.
    :param scene: Scene where the animation takes place.
    :param equation_1: The first equation
    :param equation_2: The target equation
    :param transform_index: matrix of two lists. First contains indexes of equation_1, the second
    contains indexes of equation_2.
    :param run_time: Duration of transformation
    :return: None
    """
    scene.play(
        *[
            ReplacementTransform(equation_1[i].copy(), equation_2[j])
            for i, j in zip(*transform_index)
        ],
        run_time=run_time
    )
    scene.wait()
