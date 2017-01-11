#!/git/playground/hello_world/bin/python

import pytest
from HelloWorld.Greeting import greeting


@pytest.fixture()
def setup():
    data = greeting()
    return data


def test_hello_world():
    result = setup()
    assert 'ello' in result
