.. meta::
	:description: Пакет palindromus предоставляет функции и глобальные переменные, позволяющие проверить строку, слово или текст на палиндромом.
	:keywords: palindromus check checkstring checkword checktext checkmultiline checksuper палиндром проверка проверить слово фраза текст text word

.. _palindrome-check:

Проверка палиндромов
====================

Пакет ``palindromus`` предоставляет ряд функций и глобальных переменных, позволяющих проверить, являются ли некоторая строка, слово или текст палиндромом.


.. _global-vars:

Глобальные переменные пакета palindromus
----------------------------------------
	* ``STRING`` - для проверки строки, как обычной строки.
	* ``WORD`` - для проверки строки, как слова.
	* ``MULTILINE`` - для проверки, является ли строка многострочным палиндромом.
	* ``TEXT`` - для проверки строки, как текста.
	* ``SUPER`` - для проверки, является ли строка суперпалиндромом.
	
	Для более подробной информации см. :ref:`general-terms`.
	
	
.. _intercahngable-letters:

Взаимозаменяемые буквы
----------------------
Пакет ``palindromus`` предоставляет словари взаимозаменяемых букв. Взаимозаменяемыми буквами, например, являются буквы ``и`` и ``й`` в русском языке.

Словарь взаимозаменяемых букв формируется по следующим правилам:
	
	* каждый ключ словаря - это буква, которая будет использоваться для замены;
	* значение каждого ключа - это список букв, которые будут заменены.
	
В пакете ``palindromus`` определены следующие словари взаимозаменяемых букв:

	* ``ALL`` - словарь русских и латинских взаимозаменяемых букв.
	* ``RUSSIAN`` - словарь русских взаимозаменяемых букв.
	* ``LATIN`` - словарь латинских взаимозаменяемых букв.
	
Информация по взаимозаменяемым латинским буквам взята с `русскоязычной Википедии <https://ru.wikipedia.org/wiki/%D0%9B%D0%B0%D1%82%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82#%D0%9C%D0%BE%D0%B4%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8_%D0%B1%D1%83%D0%BA%D0%B2>`_.

	
.. _func-check:
	
Функция check
-------------
.. py:function:: check(somestr, check = STRING, interchange = ALL)

	Проверяет, что строка, слово или текст являются палиндромом.
	
	:param somestr: проверяемая строка.
	:type somestr: ``str``
	
	:param check: режим проверки. Существуют следующие режимы (см. :ref:`global-vars`):
		
		* STRING
		* WORD
		* MULTILINE
		* TEXT
		* SUPER
		
		Режим STRING используется по умолчанию.
	:type check: ``int``
	
	:param interchange: словарь взаимозаменяемых букв.
	:type interchange: ``dict``
	
	:except TypeError: если проверяемая строка имеет нестроковый тип данных.
	
	:except TypeError: если режим проверки указан не как целое число.
	
	:except ValueError: если режим проверки задан неправильно. Если значение режима проверки находится в [STRING, WORD, MULTILINE, TEXT, SUPER], то режим проверки указан верно.
	
	:return: ``True`` если строка является палиндромом и ``False`` в противном случае.
	:rtype: ``bool``
	
	
.. _func-checkstring:

Функция checkstring
-------------------
.. py:function:: checkstring(somestr, interchange = ALL)

	Проверяет, что строка является палиндромом. Пример: :ref:`check-string`.
	
	:param somestr: проверяемая строка.
	
		.. important::
		
			Если проверяемая строка не содержит буквенных и/или цифровых символов или пуста, то она никогда не будет палиндромом.
			
	:type somestr: ``str``
	
	:param interchange: словарь взаимозаменяемых букв.
	:type interchange: ``dict``
	
	:except TypeError: если проверяемая строка имеет нестроковый тип данных.
	
	:return: ``True`` если строка является палиндромом и ``False`` в противном случае.
	:rtype: ``bool``
	
	
.. _func-checkword:

Функция checkword
-----------------
.. py:function:: checkword(someword, interchange = ALL)

	Проверяет, что слово является палиндромом. Пример: :ref:`check-word`
	
	:param someword: проверяемое слово.
	
		.. important::
		
			Если проверяемая строка не является словом (см. :ref:`general-terms`), то она никогда не будет палиндромом.
			
	:type someword: ``str``
	
	:param interchange: словарь взаимозаменяемых букв.
	:type interchange: ``dict``
	
	:except TypeError: если проверяемая строка имеет нестроковый тип данных.
	
	:return: ``True`` если слово является палиндромом и ``False`` в противном случае.
	:rtype: ``bool``
	
	
.. _func-checkmultiline:

Функция checkmultiline
----------------------
.. py:function:: checkmultiline(sometext, interchange = ALL)

	Проверяет, что строка является многострочным палиндромом. Пример: :ref:`check-multiline`
	
	:param sometext: проверяемый текст.
	
		.. important::
		
			Если проверяемая строка не является многострочным палиндромом (см. :ref:`general-terms`), то она никогда не будет палиндромом.
			
	:type sometext: ``str``
	
	:param interchange: словарь взаимозаменяемых букв.
	:type interchange: ``dict``
	
	:except TypeError: если проверяемая строка имеет нестроковый тип данных.
	
	:return: ``True`` если строка является многострочным палиндромом и ``False`` в противном случае.
	:rtype: ``bool``
	
	
.. _func-checktext:

Функция checktext
-----------------
.. py:function:: checktext(sometext, interchange = ALL)
	
	Проверяет, что текст является палиндромом. Пример: :ref:`check-text`
	
	:param sometext: проверяемый текст.
	
		.. important::
		
			Если проверяемая строка не является текстом (см. :ref:`general-terms`), то она никогда не будет палиндромом.
			
	:type sometext: ``str``
	
	:param interchange: словарь взаимозаменяемых букв.
	:type interchange: ``dict``
	
	:except TypeError: если проверяемая строка имеет нестроковый тип данных.
	
	:return: ``True`` если текст является палиндромом и ``False`` в противном случае.
	:rtype: ``bool``
	
	
.. _func-checksuper:

Функция checksuper
------------------
.. py:function:: checksuper(sometext, interchange = ALL)

	Проверяет, что строка является суперпалиндромом. Пример: :ref:`check-super`
	
	:param sometext: проверяемый текст.
	
		.. important::
		
			Если проверяемая строка не является суперпалиндромом (см. :ref:`general-terms`), то она никогда не будет палиндромом.
			
	:type sometext: ``str``
	
	:param interchange: словарь взаимозаменяемых букв.
	:type interchange: ``dict``
	
	:except TypeError: если проверяемая строка имеет нестроковый тип данных.
	
	:return: ``True`` если строка является суперпалиндромом и ``False`` в противном случае.
	:rtype: ``bool``
	
	
.. _func-isword:

Функция isword
--------------
.. py:function:: isword(somestr)

	Проверяет, что некоторая строка является словом (см. :ref:`general-terms`).
	
	:param somestr: проверяемая строка.
	:type somestr: ``str``
	
	:except TypeError: если проверяемая строка имеет нестроковый тип данных.
	
	:return: ``True`` если строка является словом и ``False`` в противном случае.
	:rtype: ``bool``
	
	
.. _func-isspecword:

Функция isspecword
------------------
.. py:function:: isspecword(somestr)

	Проверяет, что некоторая строка является специальным словом (см. :ref:`general-terms`)
	
	:param somestr: проверяемая строка.
	:type somestr: ``str``
	
	:except TypeError: если проверяемая строка имеет нестроковый тип данных.
	
	:return: ``True`` если строка является специальным словом и ``False`` в противном случае.
	:rtype: ``bool``
	

.. _func-istext:

Функция istext
--------------
.. py:function:: istext(somestr)

	Проверяет, что некоторая строка является текстом (см. :ref:`general-terms`)
	
	:param somestr: проверяемая строка.
	:type somestr: ``str``
	
	:except TypeError: если проверяемая строка имеет нестроковый тип данных.
	
	:return: ``True`` если строка является текстом и ``False`` в противном случае.
	:rtype: ``bool``