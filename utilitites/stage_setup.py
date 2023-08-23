"""
Sets the stage ready for the video by
generating boxes and titles.
"""

from manim import *

from settings import stage_settings as ss
from settings import file_settings as fs


def get_title_box():
    """
    Generates a rectangle for the title of the video
    :return: Manim Rectangle mobject
    """
    return Rectangle(
        height=ss.TITLE_BOX_HEIGHT,
        width=ss.TITLE_BOX_WIDTH,
        fill_color=ss.BOX_FILL_COLOR,
        fill_opacity=ss.BOX_FILL_OPACITY,
        stroke_opacity=ss.BOX_STROKE_OPACITY,
        stroke_width=ss.BOX_STROKE_WIDTH
    ).to_corner(ss.TITLE_BOX_POSITION, buff=ss.BOX_BUFF)


def get_boxes(title_box: Rectangle, box_details: list) -> VGroup:
    """
    Aligns box on the stage according to info rom box_details
    :param title_box: The box containing the title. It's reference point for other boxes
    :param box_details: A list of dictionaries. Each dictionary contains info about the specific box.
    :return: VGroup object of Rectangles. Each rectangle is a box container for specific content
    """
    boxes = VGroup()
    for detail in box_details:
        next_to = title_box if detail["next_to"] == "title" else boxes[detail["next_to"]]
        align_to = title_box if detail["align_to"] == "title" else boxes[detail["align_to"]]
        direction = detail["direction"]
        alignment = detail["alignment"]

        box = Rectangle(
            height=ss.DEFAULT_BOX_HEIGHT * detail["height"],
            width=ss.DEFAULT_BOX_WIDTH * detail["width"],
            fill_color=ss.BOX_FILL_COLOR,
            fill_opacity=ss.BOX_FILL_OPACITY,
            stroke_opacity=ss.BOX_STROKE_OPACITY,
            stroke_width=ss.BOX_STROKE_WIDTH
        ).next_to(next_to, direction).align_to(align_to, alignment)

        boxes.add(box)

    return boxes


def animate_title_box(scene: Scene, title: str, title_box: Rectangle) -> None:
    """
    Animating the title of the video
    :param scene: the scene where the animation takes play
    :param title: The title to be displayed
    :param title_box: The placeholder rectangle for the title
    :return: None
    """
    logo_file = fs.LOGO
    logo = SVGMobject(
        logo_file,
        height=title_box.height * 0.8,
        fill_color=ss.TEXT_COLOR,
        fill_opacity=1,
        stroke_color=ss.TEXT_COLOR,
        stroke_width=1
    )
    logo.move_to(title_box, aligned_edge=LEFT).shift(RIGHT * ss.LOGO_BUFF)

    title_text = Text(
        title,
        font_size=ss.TITLE_TEXT_SIZE,
        color=ss.TEXT_COLOR
    ).next_to(logo, RIGHT)

    scene.play(
        LaggedStart(
            DrawBorderThenFill(logo),
            Write(title_text),
            lag_ratio=0.8
        )
    )
    scene.wait()


def animate_boxes(
        scene: Scene,
        boxes: VGroup,
        box_details: list,
        font_size: int = ss.TEX_SIZE,
        text_color: str = ss.TEXT_COLOR
) -> VGroup:
    """
    Animates the intro of boxes and their titles
    :param scene: Scene object where all the animation will take the place
    :param boxes: VGroup of box mobjects.
    :param box_details: List of dictionaries. Each dictionary contains info about the relative box
    :param font_size: Size of the title
    :param text_color: Color of the title
    :return: VGroup mobject containing all the box title mobjects.
    """
    titles = VGroup()
    lines = VGroup()

    for box, details in zip(boxes, box_details):
        if details["title"]:
            size = details.get("font_size", font_size)
            text_color = details.get("color", text_color)

            title = Tex(
                details["title"],
                font_size=size,
                color=text_color
            ).move_to(box, aligned_edge=UL).shift(DR * ss.BOX_BUFF)

            line = Line(title.get_left(), title.get_right()).next_to(title, DOWN, buff=ss.BOX_BUFF / 3)

            titles.add(title)
            lines.add(line)

    scene.play(*[Write(title) for title in titles])
    scene.play(*[GrowFromEdge(line, LEFT) for line in lines])
    scene.wait()

    return titles


def set_the_stage(scene:Scene, title: str, box_details: list) -> VGroup:
    """
    Sets the stage for the video by animating and placing the titles and the boxes
    in their relative positions. Animation
    :param scene: Scene object where all the animations take place
    :param title: Title of the video
    :param box_details: A list of dictionaries. Each dictionary has the info about the relative box.
    :return: VGroup object consisting of titles and boxes.
            titles: is the VGroup mobject containing title mobjects.
            boxes: is the VGroup mobject containing box mobjects
    """
    title_box = get_title_box()

    boxes = get_boxes(title_box, box_details)

    scene.play(
        FadeIn(title_box),
        *[FadeIn(box) for box in boxes]
    )
    scene.wait()

    animate_title_box(scene, title, title_box)
    titles = animate_boxes(scene, boxes, box_details)

    return VGroup(titles, boxes)
