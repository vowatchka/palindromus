.. meta::
	:description: Примеры палиндромов, которые можно проверить пакетом palindromus
	:keywords: пример палиндром проверка проверить palindromus check string text word multiline super

.. _some-examples:

Примеры палиндромов
===================

.. _check-string:

Строка-палиндром
----------------
.. code-block:: python

	from palindromus import *
	
	somestr = "123 abc << >> cba 321"
	
	r = check(somestr)
	print(r)
	
Результат::

	True

	
.. _check-word:

Слово-палиндром
---------------
.. code-block:: python

	from palindromus import *
	
	someword = "топот"
	
	r = check(someword, check = WORD)
	print(r)
	
Результат::

	True
	
	
.. _check-multiline:

Многострочный палиндром
-----------------------
.. code-block:: python

	from palindromus import *
	
	somemultiline = """Ад - жажда!
	Ад - жар, вражда!
	Ад гонит иногда."""
	
	r = check(somemultiline, check = MULTILINE)
	print(r)
	
Результат::

	True
	
	
.. _check-text:

Текст-палиндром
---------------
.. code-block:: python

	from palindromus import *
	
	sometext = """Я нем и рад я,
	так, трамвай,
	январь равняй,
	а в март катя,
	дари меня."""
	
	r = check(sometext, check = TEXT)
	print(r)
	
Результат::

	True
	
	
.. _check-super:

Суперпалиндром
--------------
.. code-block:: python

	from palindromus import *
	
	sometext = "Nora. Omar. Ramo. Aron"
	
	r = check(sometext, check = SUPER)
	print(r)
	
Результат::

	True
	

.. _english-examples:

Английские палиндромы
---------------------
.. code-block:: python

	r = check("""- Madam, I'm Adam.
	- Eve.""", check = MULTILINE) # True
	
.. code-block:: python

	r = check("A man, a plan, a canal-Panama") # True
	
.. code-block:: python

	r = check("Was it a car or a cat I saw?", check = TEXT) # True
	
.. code-block:: python

	r = check('"Not New York", – Roy went on', check = TEXT) # True
	
.. code-block:: python

	r = check("Do geese see God?", check = TEXT) # True
	
.. code-block:: python

	r = check("Race fast, safe car") # True
	
.. code-block:: python

	r = check("level", check = WORD) # True

.. code-block:: python
	
	r = check("noon", check = WORD) # True
	
.. code-block:: python
	
	r = check("sagas", check = WORD) # True
	
	
.. _spanish-examples:

Испанские палиндромы
--------------------
.. code-block:: python

	r = check("Anita lava la tina") # True
	
.. code-block:: python
	
	r = check("Aire solo sería") # True
	
.. code-block:: python

	r = check("Dábale arroz a la zorra el abad.", check = TEXT) # True

	
.. _finnish-examples:

Финские палиндромы
------------------
.. code-block:: python
	
	r = check("saippuakauppias", check = WORD) # True
	

.. _german-examples:

Немецкие палиндромы
-------------------
.. code-block:: python
	
	r = check("Reit nie tot ein Tier") # True
	
.. code-block:: python

	r = check("""Ein Neger mit Gazelle zagt im Regen nie. 
	Ade, liebe Ella, red' nie in der Allee bei Leda! 
	Grasmitte, da kniet ein Kadett im Sarg""", check = MULTILINE) # True
	

.. _latin-examples:

Латинские палиндромы
--------------------
.. code-block:: python
	
	r = check("Sum summus mus") # True
	
	
.. _turkish-examples:

Турецкие палиндромы
-------------------
.. code-block:: python
	
	r = check("Anastas kazak satsana", check = TEXT) # True
	
	
.. _superpalimdromes:

Суперпалиндромы
---------------
.. code-block:: python
	
	r = check("Мир или Рим", check = SUPER) # True
	
.. code-block:: python
	
	r = check("Удав дeда, а дeд в аду", check = SUPER) # True
	
.. code-block:: python
	
	r = check("""— Ужели желал, ел, алел? А, лежи!
	— Лежу. """, check = SUPER) # True
	
.. code-block:: python
	
	r = check("Цена тела банан, а на бале - танец", check = SUPER) # True
	
	
.. _more-examples:

Еще больше примеров
-------------------
.. code-block:: python
	
	# Число 404
	r = check("404", check = STRING) # True
	
.. code-block:: python
	
	# Слово
	r = check("Топот", check = WORD) # True
	
.. code-block:: python
	
	# Самое длинное слово-палиндром в мире (фин. "продавец мыла; торговец щёлоком")
	r = check("saippuakivikauppias", check = WORD) # True
	
.. code-block:: python
	
	# Самый длинный текст палиндром в мире
	r = check("А роза упала на лапу Азора", check = TEXT) # True
	
.. code-block:: python
	
	# Фраза
	r = check("Аргентина манит негра", check = TEXT) # True
	
.. code-block:: python
	
	# Фраза
	r = check("Я иду с мечем судия", check = TEXT) # True
	
.. code-block:: python
	
	# Фраза
	r = check("Madam, I'm Adam", check = TEXT) # True
	r = check("Eve", check = TEXT) # True
	
.. code-block:: python
	
	# Фраза
	r = check("Sum summus mus", check = TEXT) # True
	
.. code-block:: python
	
	# Фраза
	r = check("Νιψον ανομηματα μη μοναν οψιν", check = TEXT) # True
	
.. code-block:: python
	
	# Текст
	r = check("Муза! Ранясь шилом опыта, ты помолишься на разум", check = TEXT) # True
	
.. code-block:: python
	
	# Несколько однострочных палиндромов
	r = check("""Кит на море романтик
	Лёша на полке клопа нашёл
	И любит Сева вестибюли
	Удавы рвали лавры в аду
	А щи - пища?
	Яд ем как мед я!
	Иди, Сеня, не сиди!""", check = MULTILINE) # True
	
.. code-block:: python
	
	# Несколько слов палиндромом
	r = check("""довод
	доход
	заказ
	кабак
	казак
	комок
	потоп
	радар
	шабаш
	шалаш""", check = MULTILINE) # True
	
.. code-block:: python
	
	# Стихотворение Д.Авалиани
	r = check("""Ной и вера - шанс у Сиона
	но Исус на шаре - Вийон""", check = TEXT) # True

.. code-block:: python
	
	# Многострочный палиндром В.Гершуни
	r = check("""Ад - жажда!
	
	Ад - жар, вражда!
	
	Ад гонит иногда.""", check = MULTILINE) # True
	
.. code-block:: python
	
	# Стихотворение Б.Гольдштейна
	r = check("""Сел в озере березов лес,
	сел лес,
	нося сон...
	Мир берест серебрим,
	мир зрим
	обуло грезой озер голубо.
	Сел в озере березов лес,
	луну дунул,
	лапу купал...
	А к долу лодка
	еле-еле
	лак резала зеркал.""", check = MULTILINE) # True
	
.. code-block:: python
	
	# Многострочный палиндром В.Рыбинского
	r = check("""Водоход доходов
	Неведом моде вен""", check = MULTILINE) # True
	
.. code-block:: python
	
	# Многострочный палиндром П.Нагорских
	r = check("""Лит ум да лик и лад мутил.
	Мат, их носи и сон хитам...""", check = MULTILINE) # True
	
.. code-block:: python
	
	# Стихотворение Б.Гольдштейна
	r = check("""Я нем и рад я,
	
	так, трамвай,
	
	январь равняй,
	
	а в март катя,
	
	дари меня.""", check = TEXT) # True
	
.. code-block:: python
	
	# Многострочный палиндром Н.Ладыгина
	r = check("""Один, души пишу дни до
	Отказа. Кто
	Ты? Пойми опыт
	И жар и миражи.""", check = MULTILINE) # True
	
.. code-block:: python
	
	# Палиндром В.Сафроницкого
	r = check("Сенсация! Поп яйца снес.", check = TEXT) # True
	
.. code-block:: python
	
	# Палиндром А.Воловика
	r = check("Сенсация: я яйца снес!", check = TEXT) # True
	
.. code-block:: python
	
	# Стихотворение с неправильным переносом
	r = check("""Пенелопа на полене-П
	олетит на антитело""", check = MULTILINE) # True
	
.. code-block:: python
	
	# Строки Г.Державина
	r = check("Я разуму уму заря,", check = TEXT) # True
	r = check("Я иду с мечем судия.", check = TEXT) # True
	
.. code-block:: python
	
	# Несколько длинных палиндромов
	text = """нольлон
	рогаммагаммагор
	маганолелонагам
	лебедрогамамагордебел
	рогаммагонолелоногаммагор."""
	
	# Многострочный палиндром
	r = checkmultiline(text)
	print("Многострочный палиндром - %s" % r) # Многострочный палиндром - True
	
	lines = text.split("\n")
	for line in lines:
		r = checktext(line)
		print("Текстовая строка - %s" % r) # Текстовая строка - True
		
		r = checkword(line)
		print("Слово - %s" % r) # Слово - True. Для последней строки выведет: Слово - False
		
.. code-block:: python
	
	# Длинное слово палиндром
	text = "рогаммагонолелоногаммагор."
	
	r = checkstring(text)
	print(r) # True
	
	r = checkword(text[:-1])
	print(r) # True
	
	r = checktext(text)
	print(r) # True