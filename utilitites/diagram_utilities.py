from manim import *

from settings import diagram_settings as ds


def rotate_the_part(part, diagram_part):
    rotation_angle = diagram_part.rotation_angle
    if rotation_angle:
        rotation_kwargs = diagram_part.rotation_kwargs
        part.rotate(rotation_angle * DEGREES, **rotation_kwargs)


def scale_the_part(part, diagram_part):
    scale = diagram_part.scale
    part.scale(scale)


def generate_shape(shape):
    function = shape.function
    function_args = shape.function_args
    function_kwargs = shape.function_kwargs
    return function(*function_args, **function_kwargs)


def generate_shapes(section, diagram, diagram_dict):
    for shape in section.shapes:
        shape_mobject = generate_shape(shape)
        diagram.add(shape_mobject)
        diagram_dict[shape.label] = shape_mobject


def generate_point(point: ds.DiagramPoint):
    reference = point.reference
    function = point.function
    function_args = point.function_args
    function_kwargs = point.function_kwargs

    return getattr(reference, function)(*function_args, **function_kwargs)


def generate_points(section, diagram_dict):
    for point in section.points:
        point_mobject = generate_point(point)
        diagram_dict[point.label] = point_mobject


def transform_shape(shape_mobject, shape, diagram_dict):
    pass


def position_shape(shape_mobject, shape, diagram_dict):
    function = shape.position_function
    if function is None:
        return

    function_kwargs = shape.position_kwargs
    reference_label = shape.reference
    reference_mobject = diagram_dict[reference_label]

    if function == "point_from_proportion":
        if reference_mobject is None:
            raise ValueError("Can't take proportion from an unspecified target mobject")
        point = getattr(reference_mobject, function)(**function_kwargs)
        shape_mobject.move_to(point)

    else:
        getattr(shape_mobject, function)(reference_mobject, **function_kwargs)


def transform_shapes(section, diagram_dict):
    for shape in section.shapes:
        shape_mobject = diagram_dict[shape.label]
        transform_shape(shape_mobject, shape, diagram_dict)
        position_shape(shape_mobject, shape, diagram_dict)


def generate_section(section: ds.Section, diagram: VGroup, diagram_dict: dict):
    generate_shapes(section, diagram, diagram_dict)
    generate_points(section, diagram_dict)
    transform_shapes(section, diagram_dict)


def transform_section(section, diagram_dict):


def generate_diagram(sections: list) -> (VGroup, dict):
    diagram = VGroup()
    diagram_dict = {}

    for section in sections:
        generate_section(section, diagram, diagram_dict)
        transform_section(section, diagram_dict)

    return diagram, diagram_dict
