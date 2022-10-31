import pytest

from random_wiki.models import (
    ResponseValidationError,
    get_random_wikipedia_article,
    open_link,
    validate_response,
)


class TestProgramLogic:
    def test_get_random_wiki_article(self):
        data = get_random_wikipedia_article()
        assert isinstance(data, list)
        assert len(data) == 2
        assert all([isinstance(i, str) for i in data])
        assert "http" in data[1]

    def test_validate_response_correct(self):
        correct_responses = ["yes", "yEs", "YES", "yeS", "YEs"]
        assert all([validate_response(response) for response in correct_responses])

    def test_validate_response_incorrect(self):
        incorrect_responses = ["yes ", 2, " no ", "yno"]
        for response in incorrect_responses:
            with pytest.raises(ResponseValidationError) as exception_info:
                validate_response(response)
            assert "ResponseValidationError" in str(exception_info.type)

    def test_open_link(self):
        open_link("http://google.com")
