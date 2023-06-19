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
    fhand = open(fname)
except FileNotFoundError:
    print(f"File cannot be opened: {fname}")
    exit()

domainsDict = {}
for line in fhand:
    if line.startswith('From:'):
        domain = line.split("@")
        domainsDict[domain[1]] = domainsDict.get(domain[1],0) + 1

print(domainsDict)
