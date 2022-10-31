"""
Test the interface outlined in random_wiki/interface.py
"""
from random_wiki import interface
from random_wiki.models import Program


class TestInterface:
    def test_init(self):
        class HelloWorldProgram(Program):
            program_name = "Hello World!"

            def main(self):
                print(self.program_name)

        # Test init
        interface.Interface(program=HelloWorldProgram())

    def test_call_main(self):
        class HelloWorldProgram(Program):
            program_name = "Hello World!"

            def main(self):
                return 2

        i = interface.Interface(program=HelloWorldProgram())
        data = i.main()
        assert data == 2
