# palindromus

[![release-badge](https://badge.fury.io/py/palindromus.svg)](https://badge.fury.io/py/palindromus)
[![license-badge](https://img.shields.io/github/license/vowatchka/palindromus.svg)](http://choosealicense.com/licenses/mit/)
![coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/vowatchka/45e50e250b2e6532951b7ce1bb4d590c/raw/pytest-coverage-comment__main.json)

## Palindromus documentation
See at https://palindromus.readthedocs.io

## Overwiew
Package helps you to check that any string, word or text are palindrome.

## Checking
Check any strings:
```python
from palindromus import *

somestr = """Ной и вера - шанс у Сиона
но Исус на шаре - Вийон"""

r = check(somestr)
print(r) # True
```

Check any words:
```python
from palindromus import *

someword = "топот"

r = check(someword, check = WORD)
print(r) # True
```

Check any multiline palindrome:
```python
from palindromus import *

somemultiline = """Ад - жажда!
Ад - жар, вражда!
Ад гонит иногда."""

r = check(somemultiline, check = MULTILINE)
print(r) # True
```

Check any text:
```python
from palindromus import *

sometext = """Я нем и рад я,
так, трамвай,
январь равняй,
а в март катя,
дари меня."""

r = check(sometext, check = TEXT)
print(r) # True
```

Check any superpalindrome:
```python
from palindromus import *

sometext = "Nora. Omar. Ramo. Aron"

r = check(sometext, check = SUPER)
print(r) # True
```

## Global settings
You can use global variablies `STRING`, `WORD`, `TEXT`, `MULTILINE`, `SUPER` for
checking any your strings as string, word, text, multiline palindrome or superpalindrome.

You can use dictionaries of interchangeable letters (`ALL`, `RUSSIAN`, `LATIN`) for interchange.
