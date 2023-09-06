from manim import *


def generate_part_of_the_diagram(part):
    # todo: get part class
    # todo: get part kwargs
    # todo: draw part with function and kwargs
    # todo: position part
    # todo: generate labels of the part
    # todo: rotate part
    # todo: return the part mobject and its string name

    return None, None


def generate_diagram(parts_of_diagram):
    diagram_dict = {}
    for part in parts_of_diagram:
        part_mob, part_name = generate_part_of_the_diagram(part)
        diagram_dict[part_name] = part_mob
        
