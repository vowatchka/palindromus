import pytest
from typing_extensions import Any

import palindromus as pld

pytestmark = [pytest.mark.check_palindrome]


@pytest.mark.parametrize(
    "somestr",
    [
        "404",
        "топот",
        "123 abc << >> cba 321",
        "A man, a plan, a canal-Panama",
        "Anita lava la tina",
        "Aire solo sería",
        "Reit nie tot ein Tier",
        "Sum summus mus",
        "Anastas kazak satsana",
    ]
)
def test_checkstring_true(somestr: str):
    """Test that some string is palindrome."""
    assert pld.checkstring(somestr)
    assert pld.check(somestr, check=pld.STRING)


@pytest.mark.parametrize(
    "somestr",
    [
        "",
        "123 abc <<",
        ",!..!,",
    ]
)
def test_checkstring_false(somestr: str):
    """Test that some string is not palindrome."""
    assert not pld.checkstring(somestr)
    assert not pld.check(somestr, check=pld.STRING)


@pytest.mark.parametrize(
    "somestr",
    [
        "топот",
        "Радар",
        "ШАБАШ",
        "noon",
        "saippuakauppias",
    ]
)
def test_checkword_true(somestr: str):
    """Test that some word is palindrome."""
    assert pld.checkword(somestr)
    assert pld.check(somestr, check=pld.WORD)


@pytest.mark.parametrize(
    "somestr",
    [
        "",
        "404",
        "123 abc << >> cba 321",
        "hello",
        "world",
        "Aire solo sería",
    ]
)
def test_checkword_false(somestr: str):
    """Test that some string is not word or not palindrome."""
    assert not pld.checkword(somestr)
    assert not pld.check(somestr, check=pld.WORD)


@pytest.mark.parametrize(
    "somestr",
    [
        "Ад - жажда!\nАд - жар, вражда!\nАд гонит иногда.",
        "Водоход доходов\n\nНеведом моде вен",
        ("Ein Neger mit Gazelle zagt im Regen nie.\n"
         "Ade, liebe Ella, red' nie in der Allee bei Leda!\n"
         "Grasmitte, da kniet ein Kadett im Sarg"),
    ]
)
def test_checkmultiline_true(somestr: str):
    """Test that some multiline text is multiline palindrome."""
    assert pld.checkmultiline(somestr)
    assert pld.check(somestr, check=pld.MULTILINE)


@pytest.mark.parametrize(
    "somestr",
    [
        "",
        "hello\nworld",
        "топот\nкопыт",
    ]
)
def test_checkmultiline_false(somestr: str):
    """Test that some multiline text is not multiline palindrome."""
    assert not pld.checkmultiline(somestr)
    assert not pld.check(somestr, check=pld.MULTILINE)


@pytest.mark.parametrize(
    "somestr",
    [
        "Я нем и рад я,\nтак, трамвай,\nянварь равняй,\nа в март катя,\nдари меня.",
        "Was it a car or a cat I saw?",
        "Race fast, safe car",
        "Anastas kazak satsana",
        "А роза упала на лапу Азора",
    ]
)
def test_checktext_true(somestr: str):
    """Test that some text is palindrome."""
    assert pld.checktext(somestr)
    assert pld.check(somestr, check=pld.TEXT)


@pytest.mark.parametrize(
    "somestr",
    [
        "",
        "Race slow, safe car",
        "hello world",
        "Я нем и рад я,\nтак, трамвай",
    ]
)
def test_checktext_false(somestr: str):
    """Test that some text is not palindrome."""
    assert not pld.checktext(somestr)
    assert not pld.check(somestr, check=pld.TEXT)


@pytest.mark.parametrize(
    "somestr",
    [
        "Мир или Рим",
        "Удав дeда,\n а дeд в аду",
    ]
)
def test_checksuper_true(somestr: str):
    """Test that some string is super palindrome."""
    assert pld.checksuper(somestr)
    assert pld.check(somestr, check=pld.SUPER)


@pytest.mark.parametrize(
    "somestr",
    [
        "",
        "hello\nworld",
        "404",
        "Race fast, safe car",
        "Водоход доходов\nНеведом моде вен",
    ]
)
def test_checksuper_false(somestr: str):
    """Test that some string is not super palindrome."""
    assert not pld.checksuper(somestr)
    assert not pld.check(somestr, check=pld.SUPER)


def test_check_exceptions():
    """Test `check` exceptions."""
    with pytest.raises(TypeError, match='keyword argument "check" must be an int'):
        pld.check("404", check="1")
    with pytest.raises(ValueError, match="Unknown mode"):
        pld.check("404", check=100500)


@pytest.mark.parametrize(
    "obj",
    [
        404,
        [404],
        {404: 404},
        True,
        False,
    ]
)
def test_only_strings_can_be_checked(obj: Any):
    """Test that only strings can be checked as palindrome."""
    with pytest.raises(TypeError, match="only strings can be checked"):
        pld.OnlyStringsCanBeChecked(obj)
