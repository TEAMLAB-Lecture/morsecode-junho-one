import re

raw_english_sentence = "This is CS5501!!!"
a = re.sub("[\.,!?]", "", raw_english_sentence.strip())

print(a)