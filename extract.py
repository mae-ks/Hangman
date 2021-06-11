import urllib.request, urllib.parse, urllib.error
link = urllib.request.urlopen("https://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt")
word_list = []
with open("dictionary.txt", 'w') as text:
    for line in link:
        word = line.decode().strip()
        if 4 < len(word) < 11 and not word[0].isupper():
            if word[-2:] != "ly" and word[-2:] != "ed" and word[-3:] != "ous" and word[-3:] != "ing" and word[-4:] != "ment" and word[-4:] != "ness" and word[-5:] != "ingly":
                word_list.append(word)
                text.write(word + '\n')

#ly, ous, ed, ing, ment, ingly
