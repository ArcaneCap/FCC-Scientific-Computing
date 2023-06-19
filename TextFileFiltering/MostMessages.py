import string

print("1. mbox.txt")
print("2. mbox-short.txt\n")

fchoice = input("Enter 1 or 2 > ")
if fchoice == "1":
    fname = 'mbox.txt'
elif fchoice == "2":
    fname = 'mbox-short.txt'
else:
    print("Invalid choice")

try:
    fhandle = open(fname)
except FileNotFoundError:
    print(f"File cannot be opened: {fname}")
    exit()

counts = {}

for line in fhandle:
    if not line.startswith('From'):
        continue
    line = line.strip().lower()
    # line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split()
    # print(repr(line))
    if len(words) > 2:
        counts[words[1]] = counts.get(words[1], 0) +1

print(f"Most messages in {fname}:\n")
max_key = max(counts, key=counts.get)
print(f"{max_key} ({counts[max_key]} messages)")
