from language_finder import LanguageFinder


print "Input:"
while True:
    language_pattern = raw_input()
    if language_pattern == "":
        break
    word = raw_input()
    if word == "":
        break

    lang_finder = LanguageFinder(language_pattern, word)
    print "Output: "
    print ("no", "yes")[lang_finder.is_word_from_lang]
