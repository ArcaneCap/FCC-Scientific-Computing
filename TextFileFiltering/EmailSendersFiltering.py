
count = 0
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if not line.startswith('From '): 
        continue
    count +=1
    words = line.split()
    print(repr(words[1]))
print(f"There were {count} lines in the file with 'From' as the first word")
