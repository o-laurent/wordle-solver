import unicodedata

filename = "./data/english_dict"


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def valid(word):
    return not "-" in word and not "'" in word and not "." in word

f = open(filename+".txt", "r")
data = f.read().split("\n")
data5 = set([remove_accents(word).lower() for word in data if len(word) == 5 and valid(word)])
f.close()

f = open(filename+"5.txt", "w")
print(len(data5))
f.write('\n'.join(data5))
f.close()
