import pytest
from random_wiki.models import Program, RandomWiki, ResponseValidationError


class TestProgram:

    def test_program(self):
        class HelloWorldProgram(Program):
            program_name = "Hello World!"

            def main(self):
                print(self.program_name)

        program = HelloWorldProgram()
        assert isinstance(program, Program)

    def test_response_validation_error(self):
        with pytest.raises(ResponseValidationError) as exception_info:
            raise ResponseValidationError("Test!")
        assert "ResponseValidationError" in str(exception_info.type)
