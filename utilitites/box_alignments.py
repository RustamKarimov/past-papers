"""
Defines box alignments on the stage
R: Single box below the title.
RR: 2 boxes above each other.
CC: 2 boxes next to each other.
CRR: 1 box on the left side, 2 boxes on the right side (on top of each other).
RRC: 2 boxes on the left side (on top of each other), one box on teh left side.
CCR: 2 boxes on top row (next to each other), 1 box on the bottom row.
RCC: 1 box on the top row, 2 boxes on the bottom row (next to each other)
"""
from manim import *


R = [
    {
        "next_to": "title",
        "direction": DOWN,
        "align_to": "title",
        "alignment": LEFT,
        "height": 1,
        "width": 1
    }
]

RR = [
    {
        "next_to": "title",
        "direction": DOWN,
        "align_to": "title",
        "alignment": LEFT,
        "height": 0.49,
        "width": 1
    },
    {
        "next_to": 0,
        "direction": DOWN,
        "align_to": 0,
        "alignment": LEFT,
        "height": 0.49,
        "width": 1
    }
]

CC = [
    {
        "next_to": "title",
        "direction": DOWN,
        "align_to": "title",
        "alignment": LEFT,
        "height": 1,
        "width": 0.49
    },
    {
        "next_to": 0,
        "direction": RIGHT,
        "align_to": 0,
        "alignment": UP,
        "height": 1,
        "width": 0.49
    }
]

CRR = [
    {
        "next_to": "title",
        "direction": DOWN,
        "align_to": "title",
        "alignment": LEFT,
        "height": 1,
        "width": 0.49
    },
    {
        "next_to": 0,
        "direction": RIGHT,
        "align_to": 0,
        "alignment": UP,
        "height": 0.48,
        "width": 0.49
    },
    {
        "next_to": 1,
        "direction": DOWN,
        "align_to": 1,
        "alignment": LEFT,
        "height": 0.48,
        "width": 0.49
    }
]

RRC = [
    {
        "next_to": "title",
        "direction": DOWN,
        "align_to": "title",
        "alignment": LEFT,
        "height": 0.49,
        "width": 0.49
    },
    {
        "next_to": 0,
        "direction": DOWN,
        "align_to": 0,
        "alignment": LEFT,
        "height": 0.49,
        "width": 0.49
    },
    {
        "next_to": 0,
        "direction": RIGHT,
        "align_to": 0,
        "alignment": UP,
        "height": 1,
        "width": 0.49
    }
]

CCR = [
    {
        "next_to": "title",
        "direction": DOWN,
        "align_to": "title",
        "alignment": LEFT,
        "height": 0.49,
        "width": 0.49
    },
    {
        "next_to": 0,
        "direction": RIGHT,
        "align_to": 0,
        "alignment": UP,
        "height": 0.49,
        "width": 0.49
    },
    {
        "next_to": 0,
        "direction": DOWN,
        "align_to": 0,
        "alignment": LEFT,
        "height": 0.49,
        "width": 1
    }
]

RCC = [
    {
        "next_to": "title",
        "direction": DOWN,
        "align_to": "title",
        "alignment": LEFT,
        "height": 0.49,
        "width": 1
    },
    {
        "next_to": 0,
        "direction": DOWN,
        "align_to": 0,
        "alignment": LEFT,
        "height": 0.49,
        "width": 0.49
    },
    {
        "next_to": 1,
        "direction": RIGHT,
        "align_to": 1,
        "alignment": UP,
        "height": 0.49,
        "width": 0.49
    }
]

BOX_STRUCTURES = {
    "R": R,
    "RR": RR,
    "CC": CC,
    "CRR": CRR,
    "RRC": RRC,
    "CCR": CCR,
    "RCC": RCC
}


def get_box_details(box_structure: str, titles: tuple, box_sizes: tuple = None):
    if len(box_structure) != len(titles):
        message = f"""
        Length of box_structure and number of titles must be same.
        Length of the box_structure is {len(box_structure)}.
        Number of titles is {len(titles)} 
        """
        raise ValueError(message)
    elif box_sizes and len(box_structure) != len(box_sizes):
        message = f"""
        Length of box_structure and number of box sizes must be same.
        Length of the box_structure is {len(box_structure)}.
        Number of box sizes is {len(box_sizes)} 
        """
        raise ValueError(message)

    if box_sizes is None:
        box_sizes = (None for _ in range(len(box_structure)))

    structure = BOX_STRUCTURES[box_structure.upper()]
    for box, title, size in zip(structure, titles, box_sizes):
        box["title"] = title
        if size:
            box["height"] = size[0]
            box["width"] = size[1]
    return structure
