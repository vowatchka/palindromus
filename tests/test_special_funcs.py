import pytest

import palindromus as pld

pytestmark = [pytest.mark.special]


@pytest.mark.parametrize(
    "somestr",
    [
        "a",
        "as",
        "to",
        "be",
        "до",
        "от",
    ]
)
def test_isspecword_true(somestr: str):
    """Test that some text is special word."""
    assert pld.isspecword(somestr)


@pytest.mark.parametrize(
    "somestr",
    [
        "",
        "pre",
        "под",
        "перед",
        "after.",
        "bef\nore"
    ]
)
def test_isspecword_false(somestr: str):
    """Test that some text is not special word."""
    assert not pld.isspecword(somestr)


@pytest.mark.parametrize(
    "somestr",
    [
        "hello",
        "world",
        "топот",
        "привет",
        "as",
    ]
)
def test_isword_true(somestr: str):
    """Test that some text is word."""
    assert pld.isword(somestr)


@pytest.mark.parametrize(
    "somestr",
    [
        "",
        "classs",
        "a",
        "bef\nore",
    ]
)
def test_isword_false(somestr: str):
    """Test that some text is not word."""
    assert not pld.isword(somestr)


@pytest.mark.parametrize(
    "somestr",
    [
        "hello world",
        "привет, мир",
        "word",
    ]
)
def test_istext_true(somestr: str):
    """Test that some text is text."""
    assert pld.istext(somestr)


@pytest.mark.parametrize(
    "somestr",
    [
        "",
        "hello_world and friends",
        "404",
    ]
)
def test_istext_false(somestr: str):
    """Test that some text is not text."""
    assert not pld.istext(somestr)
