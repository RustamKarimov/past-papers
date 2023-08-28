from manim import *

from settings.file_settings import BASE_DIR


class QuestionScene(Scene):
    """
    Extension of a Scene mobject with the following additions
    self.subject: Subject of the paper
    self.year: Year of the paper
    self.question: the text file containing the question
    """
    def __init__(
            self,
            subject="Physics",
            subject_short="PS",
            paper="P1",
            year="2022",
            month="November"
    ):
        """
        Initializes the QuestionScene class
        :param subject: Subject of the paper
        :param year: Year of the paper
        """
        self.subject = subject
        self.subject_short = subject_short
        self.paper = paper
        self.month = month
        self.year = year
        self.question = self.get_question_file()
        self.question_number = self.get_question_number()
        super().__init__()

    def get_question_file(self) -> Path:
        """
        Gets the file name of the text file containing the question
        :return: path to the question text file
        """
        question = self.__class__.__name__.split("_")[1]
        sub_question = f"{self.__class__.__name__.lower()}.txt"
        return BASE_DIR / self.subject / self.year / f"Question_{question}" / sub_question

    def get_question_number(self) -> str:
        """
        Generates the number of the question from the class name
        :return: the question number
        """
        question_number = self.__class__.__name__.split("_")[1:]
        question_number_with_period = ".".join(question_number)
        return f"Question {question_number_with_period}"

    def get_the_title(self) -> str:
        """
        Generates the title of the question.
        :return: title of the text
        """
        return f"{self.subject_short} - {self.year} {self.month} {self.paper} - {self.question_number}"
