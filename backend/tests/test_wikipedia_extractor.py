# coding: utf-8

import pytest
import error

examples = [
    "Cité Paradis",
]

def test_is_string():
    pass

def test_is_url():


def test_manage_error():
    with pytest.raises(error.APIError):
        pass
