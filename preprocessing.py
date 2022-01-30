import unicodedata

filename = "data/english"
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

f = open(filename+".txt", "r")
data = f.read().split("\n")
data5 = set([remove_accents(word) for word in data if len(word)==5])
f.close()

f = open(filename+"5.txt", "w")
print('\n'.join(data5))
f.write('\n'.join(data5))
f.close()