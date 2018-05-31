#!/usr/bin/env python

'''
	Checks that some string is palindrome
	
	Package helps you to check that any string, word or text are palindrome.
	
	Check any strings:
	    from palindromus import *
	    
		somestr = """Ной и вера - шанс у Сиона
	    но Исус на шаре - Вийон"""
		
	    r = check(somestr)
	    print(r) # True
		
	Check any words:
	    from palindromus import *
	    
	    someword = "топот"
		
	    r = check(someword, check = WORD)
	    print(r) # True
		
	Check any multiline palindrome:
	    from palindromus import *
		
	    somemultiline = """Ад - жажда!
	    Ад - жар, вражда!
	    Ад гонит иногда."""
		
	    r = check(somemultiline, check = MULTILINE)
	    print(r) # True
		
	Check any text:
	    from palindromus import *
		
	    sometext = """Я нем и рад я,
	    так, трамвай,
	    январь равняй,
	    а в март катя,
	    дари меня."""
		
	    r = check(sometext, check = TEXT)
	    print(r) # True
		
	Check any superpalindrome:
	    from palindromus import *
		
	    sometext = "Nora. Omar. Ramo. Aron"
		
	    r = check(sometext, check = SUPER)
	    print(r) # True
		
	You can use global variablies STRING, WORD, TEXT, MULTILINE, SUPER for 
	checking any your strings as string, word, text, multiline palindrome or superpalindrome.
	
	You can use dictionaries of interchangeable letters (ALL, RUSSIAN, LATIN) for interchange.
'''

# Define metadata
__version__ 	= '1.0.0'
__author__ 		= 'Vladimir Saltykov'
__copyright__ 	= 'Copyright 2018, Vladimir Saltykov'
__email__ 		= 'vowatchka@mail.ru'
__license__ 	= "MIT"
__date__ 		= '2018-05-28'

__all__ = [
			'STRING', 'WORD', 'MULTILINE', 'TEXT', 'SUPER',  
			'check', 'checkstring', 'checkword', 'checkmultiline', 'checktext'
		  ]

# Import modules and packages
import re
import math

# define constants
STRING = 1
WORD = 2
MULTILINE = 3
TEXT = 4
SUPER = 5

# Define interchangeable letters.
# See at https://ru.wikipedia.org/wiki/%D0%9B%D0%B0%D1%82%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82#%D0%9C%D0%BE%D0%B4%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8_%D0%B1%D1%83%D0%BA%D0%B2
# Use follow format:
#  - each key of dictionary is letter that uses for interchange
#  - value of each key is list of letters thats must be interchanged
ALL = {
	"е": ["ё"], # russian
	"и": ["й"], # russian
	"a": ["ā","ă","â","ã","à","á","ä","ą"], # latin
	"ae": ["Æ"], # latin
	"c": ["ç","č","ć"], # latin
	"d": ["đ"], # latin
	"e": ["ē","ę"], # latin
	"g": ["ğ","ģ"], # latin
	"i": ["î","į","ì","í","ï","ī"], # latin
	"k": ["ķ"], # latin
	"l": ["ł"], # latin
	"n": ["ň"], # latin
	"o": ["ö","õ","ó","ø"], # latin
	"oe": ["œ"], # latin
	"s": ["ş","š","ś"], # latin
	"t": ["ţ"], # latin
	"u": ["ū","ŭ","ú","ù","û"], # latin
	"z": ["ž","ź","ż"], # latin
}
RUSSIAN = {
	"е": ["ё"],
	"и": ["й"],
}
LATIN = {
	"a": ["ā","ă","â","ã","à","á","ä","ą"],
	"ae": ["Æ"],
	"c": ["ç","č","ć"],
	"d": ["đ"],
	"e": ["ē","ę"],
	"g": ["ğ","ģ"],
	"i": ["î","į","ì","í","ï","ī"],
	"k": ["ķ"],
	"l": ["ł"],
	"n": ["ň"],
	"o": ["ö","õ","ó","ø"],
	"oe": ["œ"],
	"s": ["ş","š","ś"],
	"t": ["ţ"],
	"u": ["ū","ŭ","ú","ù","û"],
	"z": ["ž","ź","ż"],
}

def check(somestr, check = STRING, interchange = ALL):
	'''
		Checks that some string, word or text are palindrome. Checking performs case-insensitive
		
		:param str somestr:
		    It is some string that will be checked for palindrome
		
		:param int check:
		    It is mode of checking. Follows modes are available:
			
		       - STRING - means that checking of string performs as string. See more at help(palindromus.checkstring)
		       - WORD - means that checking of string performs as word. See more at help(palindromus.checkword)
		       - MULTILINE - means that checking of string performs as multiline palindrome. See more at help(palindromus.checkmultiline)
		       - TEXT - means that checking of string performs as text. See more at help(palindromus.checktext)
			   - SUPER - means that checking of string performs as superpalindrome. See more at help(palindromus.checksuper)
			
		    The STRING-mode is default
			
		:param dict interchange:
		    It is dictionary of interchangeable letters
			
		:except TypeError:
		    If the checked string is not a string
			
		:except TypeError:
		    If checking mode is not specified as integer
			
		:except ValueError:
		    If value of checking mode is not valid.
		    If value of checking mode in [STRING, WORD, MULTILINE, TEXT, SUPER] then it is valid
			
		:return bool:
	'''
	# check invalid data types
	OnlyStringsCanBeChecked(somestr)
	if not isinstance(check, int):
		raise TypeError('keyword argument "check" must be an int')
		
	if check == STRING:
		# check that string is palindrome
		return checkstring(somestr, interchange = interchange)
	elif check == WORD:
		# check that word is palindrome
		return checkword(somestr, interchange = interchange)
	elif check == MULTILINE:
		# check that text is multiline palindrome
		return checkmultiline(somestr, interchange = interchange)
	elif check == TEXT:
		# check that text is palindrome
		return checktext(somestr, interchange = interchange)
	elif check == SUPER:
		# check that text is super palindrome
		return checksuper(somestr, interchange = interchange)
	else:
		# all other cases
		raise ValueError('Unknown mode %i' % check)
		
def checkstring(somestr, interchange = ALL):
	'''
		Checks that some string is palindrome. Checking performs case-insensitive
		
		:param str somestr:
		    It is some string that will be checked for palindrome as string.
			
		    The string is any string that you want. The string also can be multiline.
			
		    If the checked string does not contains any alphabetic characters or numbers or 
		    it is empty then it will never be palindrome
			
		:param dict interchange:
		    It is dictionary of interchangeable letters
			
		:except TypeError:
		    If the checked string is not a string

		:return bool:
	'''
	# check invalid data types
	OnlyStringsCanBeChecked(somestr)
	
	if somestr != "":
		# remove all special symbols
		pattern = r'[^\w]+|[_]+'
		purestr = re.sub(pattern, '', somestr.lower().strip(), flags = re.IGNORECASE | re.MULTILINE)
		
		for k,v in interchange.items():
			ic_pattern = '|'.join(v)
			purestr = re.sub(ic_pattern, k, purestr, flags = re.IGNORECASE | re.MULTILINE)
		
		# reverse pure string
		reversstr = purestr[-1::-1]
		
		# if purestr == "" that means that specified string contains 
		# only special symbols. This string is not palindrome
		if purestr != "" and reversstr == purestr:
			return True
	# in other cases
	return False
		
def checkword(someword, interchange = ALL):
	'''
		Checks that some word is palindrome. Checking performs case-insensitive
		
		:param str someword:
		    It is some string that will be checked for palindrome as word.
		    What is the word see at help(palindromus.isword)
			
		:param dict interchange:
		    It is dictionary of interchangeable letters
			
		:except TypeError:
		    If the checked word is not a string
			
		:return bool:
	'''
	# check invalid data types
	OnlyStringsCanBeChecked(someword)
		
	if isword(someword):
		return checkstring(someword, interchange = interchange)
	else:
		return False
	
def checkmultiline(sometext, interchange = ALL):
	'''
		Checks that some text is multiline palindrome. Checking performs case-insensitive
		
		:param str sometext:
		    It is some string that will be checked for palindrome as multiline palindrome.
			
		    The multiline palindrome is text that contains palindrome at each line 
		    (what is the text see at help(palindromus.istext)).
			
		    Only multiline text can be the multiline palindrome.
			
		:param dict interchange:
		    It is dictionary of interchangeable letters
			
		:except TypeError:
		    If the checked text is not a string
			
		:return bool:
	'''
	# check invalid data types
	OnlyStringsCanBeChecked(sometext)
	
	if istext(sometext):
		lines = re.split(r'\r\n|\n|\r', sometext)
		if len(lines) > 1:
			for line in lines:
				if line.strip() == "":
					continue # skip empty lines
				if not checkstring(line, interchange = interchange):
					return False
			return True
	# in other cases
	return False
	
def checktext(sometext, interchange = ALL):
	'''
		Checks that some text is palindrome. Checking performs case-insensitive
		
		:param str sometext:
		    It is some string that will be checked for palindrome as text.
			
		    What is the text see at help(palindromus.istext)
			
		    The text can be multiline.
			
		:param dict interchange:
		    It is dictionary of interchangeable letters
			
		:except TypeError:
		    If the checked text is not a string
			
		:return bool:
	'''
	# check invalid data types
	OnlyStringsCanBeChecked(sometext)
	
	if istext(sometext):
		return checkstring(sometext, interchange = interchange)
	else:
		return False
		
def checksuper(sometext, interchange = ALL):
	'''	
		Checks that some text is superpalindrome. Checking performs case-insensitive
		
		:param str sometext:
		    It is some string that will be checked for superpalindrome as text.
			
		    What is the text see at help(palindromus.istext)
			
		    The text can be multiline.
			
		:param dict interchange:
		    It is dictionary of interchangeable letters
			
		:except TypeError:
		    If the checked text is not a string
			
		:return bool:
	'''
	def text_by_columns(text, columns):
		column_idx = 0
		result_text = ""
		while column_idx+1 <= columns:
			for idx in range(columns):
				result_text += text[idx*columns + column_idx]
			column_idx += 1
		return result_text
	
	# check invalid data types
	OnlyStringsCanBeChecked(sometext)
	
	if istext(sometext):
		# get only alphabetic
		matches = re.findall(r'\w+', sometext)
		
		if len(matches):
			alphabetic = (''.join(matches)).replace('_', '')
			
			# get matrix size
			n = math.sqrt(len(alphabetic))
			if math.ceil(n) == int(n):
				n = int(n) # float to integer
				if checkstring(alphabetic, interchange = interchange):
					# read by columns
					alphabetic_by_col = text_by_columns(alphabetic, n)
					if checkstring(alphabetic_by_col, interchange = interchange):
						return True
	# in other cases
	return False
	
def isword(somestr):
	'''
		Checks that some string is a word
		
		:param str somestr:
		    It is some string that will be checked for word.
			
		    The word is a string that contains only alphabetic characters, 
		    its length not less 2 characters and 
		    noone characters does not reeats more than 2 times in a row.
			
		    The word can not be multiline
			
		:except TypeError:
		    If the checked word is not a string
			
		:return bool:
	'''
	# check invalid data types
	OnlyStringsCanBeChecked(somestr)
	
	if somestr.isalpha() and len(somestr) > 1:
		# find characters that repeats more then 2 times in a row
		matches = re.search(r'(.)(\1)(\1)', somestr, flags = re.IGNORECASE)
		if matches == None:
			# russian
			# check first character
			if somestr.lower()[0:1] not in ['ъ', 'ь']:
				return True
	# in other cases
	return False
	
def isspecword(somestr):
	'''
		Checks that some string is a special word
		
		:param str somestr:
		    It is some string that will be checked for special word.
			
		    The special word is a string that contains only alphabetic characters, 
		    its length not less 1 character and not more 2 characters and 
		    also noone characters does not reeats more than 1 times in a row.
			
		    The special word can not be multiline.
			
		    For example, special word is preposition
			
		:except TypeError:
		    If the checked special word is not a string
			
		:return bool:
	'''
	# check invalid data types
	OnlyStringsCanBeChecked(somestr)
	
	if somestr.isalpha() and len(somestr) in [1, 2]:
		# find characters that repeats more then 1 times in a row
		matches = re.search(r'(.)(\1)', somestr, flags = re.IGNORECASE)
		if matches == None:
			# russian
			# check first character
			if somestr.lower()[0:1] not in ['ъ', 'ь']:
				return True
	# in other cases
	return False
	
def istext(somestr):
	'''
		Checks that some string is a text
		
		:param str somestr:
		    It is some string that will be checked for text.
			
		    The text is string that contains only words or special words such as preposition 
		    (what is the word and the special word see at help(palindromus.isword) and help(palindromus.isspecword)).
			All words can be divided any special symbols such as punctuation marks.
			
		    The text can be multiline
			
		:except TypeError:
		    If the checked text is not a string
			
		:return bool:
	'''
	# check invalid data types
	OnlyStringsCanBeChecked(somestr)
	
	# get all matches
	matches = re.findall(r'\w+', somestr.strip(), flags = re.IGNORECASE | re.MULTILINE)
	if not len(matches):
		return False
	else:
		for match in matches:
			if match.find("_") >= 0 or (not isspecword(match) and not isword(match)):
				return False
		return True
	
	
def OnlyStringsCanBeChecked(somestr):
	'''
		Raises TypeError if argument is not string
		
		:param str somestr:
		    It is some string
			
		:except TypeError:
		    If argument is not a string
		
		:return None:
	'''
	# check invalid data types
	if not isinstance(somestr, str):
		raise TypeError('only strings can be checked')