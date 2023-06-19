import string


fhand = open('romeo-full.txt', 'r')
counts = {}
for line in fhand:
    line = line.strip()
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split()
    for word in words:
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1


#Create a tuple of keys and values from counts dict.
lst = []
for key, val in list(counts.items()):
    lst.append((val,key))
lst.sort(reverse=True)



for key, val in lst[:10]:
    print(key, val)
