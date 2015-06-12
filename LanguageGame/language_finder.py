class LanguageFinder:

	def __init__(self, lang_pattern, word):
		self.lang_pattern = lang_pattern
		self.word = word
		self.is_word_from_lang = self.is_word_from_lang()

	def is_word_from_lang(self):
		word_unique_chars = list(set(self.word))
		lang_chars = self.lang_pattern.split("^n")[:-1]
		count = {}
		if len(word_unique_chars) != len(lang_chars):
			return False
		for char in self.word:
			if char in count:
				count[char] += 1
			else:
				count[char] = 1
		if len(set(count.values())) == 1:
			return True
		return False
