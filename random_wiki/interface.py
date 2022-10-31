"""
This file is for the user interface. The underlying program will extend a main function - all this needs to do
is take in a program, then execute the program. This is an example delivery mechanism of the project and others
can be used.
"""
from random_wiki.models import Program


class Interface:
    def __init__(self, program: Program):
        self.program = program

    def main(self):
        return self.program.main()
