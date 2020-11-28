import re
patterns = ["term1", "term2"]

""" text = "This has a term1"

for pattern in patterns:
    if re.search(pattern,text):
        print("found"+ pattern) """

""" split_at = '@'
text = "alan@a.com"
print(text.split(split_at))
print(re.split(split_at, text)) """

#print(re.findall('match', 'this match matches the matched text'))

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern{}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = 'sdsd sssddd sdddd sdddds sdsds   dddssd  sdsd'
test_patterns = ['sd*']

multi_re_find(test_patterns, test_phrase)