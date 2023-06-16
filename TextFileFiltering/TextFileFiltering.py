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
    
totalConfidence = 0
counter = 0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        counter +=1
        confidence = float(line.split()[1])
        totalConfidence += confidence
        
if count != 0:
    print(f"Average spam confidence: {totalConfidence / counter}")
else:
    print("No 'X-DSPAM-Confidence' lines found in the file.")

