import pytest

from random_wiki.models import Program, ResponseValidationError


class TestProgram:
    def test_response_validation_error(self):
        with pytest.raises(ResponseValidationError) as exception_info:
            raise ResponseValidationError("Test!")
        assert "ResponseValidationError" in str(exception_info.type)
