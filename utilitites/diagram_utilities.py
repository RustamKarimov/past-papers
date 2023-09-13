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


def apply_individual_action(action):
    pass


def apply_action(action):
    pass


def generate_diagram(sections):
    diagram = VGroup()
    diagram_dict = {}

    for section in sections:
        for part in section.parts:
            diagram_part = generate_part_of_the_diagram(part, diagram_dict)
            diagram_dict[part.label] = diagram_part
            diagram.add(diagram_part)

        if section.individual_actions:
            for action in section.individual_actions:
                apply_individual_action(action)

        if section.actions:
            for action in section.actions:
                apply_action(action)

    return diagram, diagram_dict
