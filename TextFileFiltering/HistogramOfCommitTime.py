fname = 'mbox-short.txt'
fhand = open(fname)

commitTime = {}



for line in fhand:
    if line.startswith('From'):
        words = line.split()
        if len(words) > 5:
            time = words[5].split(":")
            
            hour = time[0]
            commitTime[hour] = commitTime.get(hour, 0) +1

lst = sorted(commitTime.items())

for key, val in lst:
    print(val, key)


