from abc import ABCMeta, abstractmethod
import os
import re


class Utils(object, metaclass=ABCMeta):

    _input = None
    _custom_input = None

    @abstractmethod
    def __init__(self):
        filepath = os.path.abspath('input.txt')
        if not os.path.isfile(filepath):
            raise Exception("Path to the file is incorrect, make sure you name the input file as input.txt")

        file = open(filepath)
        self.input = file.readlines()
        file.close()

        if re.search('tests/', filepath):
            filepath = re.sub('tests/', '', os.path.abspath('input.txt'))
            file = open(filepath)
            self.custom_input = file.readlines()
            file.close()

