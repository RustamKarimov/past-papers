from manim import *


def draw_a_part(diagram_part):
    function = diagram_part.function
    function_kwargs = diagram_part.function_kwargs
    return function(**function_kwargs)


def position_the_part(part, diagram_part, diagram_dict):
    function = diagram_part.position_function
    if function:
        function_kwargs = diagram_part.position_kwargs
        reference_label = function_kwargs.pop("reference")
        reference_point = diagram_dict[reference_label]
        getattr(part, function)(reference_point, **function_kwargs)


def rotate_the_part(part, diagram_part):
    rotation_angle = diagram_part.rotation_angle
    if rotation_angle:
        rotation_kwargs = diagram_part.rotation_kwargs
        part.rotate(rotation_angle * DEGREES, **rotation_kwargs)


def scale_the_part(part, diagram_part):
    scale = diagram_part.scale
    part.scale(scale)


def generate_part_of_the_diagram(diagram_part, diagram_dict):
    part = draw_a_part(diagram_part)
    scale_the_part(part, diagram_part)
    rotate_the_part(part, diagram_part)
    position_the_part(part, diagram_part, diagram_dict)

    return part


def generate_diagram(parts_of_diagram):
    diagram = VGroup()
    diagram_dict = {}
    for part in parts_of_diagram:
        diagram_part = generate_part_of_the_diagram(part, diagram_dict)
        diagram_dict[part.label] = diagram_part
        diagram.add(diagram_part)

    return diagram, diagram_dict


# todo: try to get proportion for a point
# todo: try to get starts end and other points
