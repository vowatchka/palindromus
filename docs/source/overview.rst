.. meta::
	:description: Пакет palindromus позволяет проверить, являются ли строка, слово или текст палиндромом.
	:keywords: пакет palindromus строка текст слово палиндром многострочный супер суперпалиндром проверить

.. _overview:

Обзор
=====
Пакет ``palindromus`` позволяет проверить, являются ли строка, слово или текст палиндромом.


.. _setup:

Установка
---------
С помощью pip::

	pip install palindromus
	

.. _usage:

Как использовать?
-----------------
Проверяйте любые строки:

.. code-block:: python

	from palindromus import *
	
	somestr = """Ной и вера - шанс у Сиона
	но Исус на шаре - Вийон"""
	
	r = check(somestr)
	print(r) # True
	
Проверяйте любые слова:

.. code-block:: python

	from palindromus import *
	
	someword = "топот"
	
	r = check(someword, check = WORD)
	print(r) # True
	
Проверяйте любые многострочные палиндромы:

.. code-block:: python
	
	from palindromus import *
	
	somemultiline = """Ад - жажда!
	Ад - жар, вражда!
	Ад гонит иногда."""
	
	r = check(somemultiline, check = MULTILINE)
	print(r) # True
	
Проверяйте любой текст:

.. code-block:: python
	
	from palindromus import *
	
	sometext = """Я нем и рад я,
	так, трамвай,
	январь равняй,
	а в март катя,
	дари меня."""
	
	r = check(sometext, check = TEXT)
	print(r) # True
	
Проверяйте любые суперпалиндромы:

.. code-block:: python
	
	from palindromus import *
	
	sometext = "Nora. Omar. Ramo. Aron"
	
	r = check(sometext, check = SUPER)
	print(r) # True
	
Вы можете использовать глобальные переменные ``STRING``, ``WORD``, ``TEXT``, ``MULTILINE``, ``SUPER`` для проверки на палиндром любых ваших строк, слов и текста или же вы можете использовать отдельные функции (см. :ref:`palindrome-check`).