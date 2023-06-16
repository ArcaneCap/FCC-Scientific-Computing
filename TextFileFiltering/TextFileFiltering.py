print("1 > mbox-short.txt")
print("2 > mbox.txt")
choice = input("Choose 1 or 2: ")

if choice == "1":
    fName = 'mbox-short.txt'
elif choice == "2":
    fName = 'mbox.txt'
else:
    print("Invalid choice.")
    exit()

try:
    fhand = open(fName)
except:
    print(f"File cannot be opened: {fName}")
    exit()

count = 0
total = 0

for i in fhand:
    if i.find('X-DSPAM-Confidence') == -1:
        continue
    confidence = float(i.split()[1])
    count += 1
    total += confidence

if count != 0:
    average = total / count
    print("Average confidence:", average)
else:
    print("No 'X-DSPAM-Confidence' lines found in the file.")

