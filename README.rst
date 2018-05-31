Palindromus documentation
-------------------------
See at https://palindromus.readthedocs.io

Overwiew
--------
Package helps you to check that any string, word or text are palindrome.

Checking
--------
Check any strings::
	
	from palindromus import *
	
	somestr = """Ной и вера - шанс у Сиона
	но Исус на шаре - Вийон"""
	
	r = check(somestr)
	print(r) # True
	
Check any words::
	
	from palindromus import *
	
	someword = "топот"
	
	r = check(someword, check = WORD)
	print(r) # True
	
Check any multiline palindrome::
	
	from palindromus import *
	
	somemultiline = """Ад - жажда!
	Ад - жар, вражда!
	Ад гонит иногда."""
	
	r = check(somemultiline, check = MULTILINE)
	print(r) # True
	
Check any text::
	
	from palindromus import *
	
	sometext = """Я нем и рад я,
	так, трамвай,
	январь равняй,
	а в март катя,
	дари меня."""
	
	r = check(sometext, check = TEXT)
	print(r) # True
	
Check any superpalindrome::
	
	from palindromus import *
	
	sometext = "Nora. Omar. Ramo. Aron"
	
	r = check(sometext, check = SUPER)
	print(r) # True

Global settings
---------------
You can use global variablies ``STRING``, ``WORD``, ``TEXT``, ``MULTILINE``, ``SUPER`` for 
checking any your strings as string, word, text, multiline palindrome or superpalindrome.

You can use dictionaries of interchangeable letters (``ALL``, ``RUSSIAN``, ``LATIN``) for interchange.