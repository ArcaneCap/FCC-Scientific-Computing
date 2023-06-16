#data = 'From stephen@gmail.com Sat Jun 5 09:14:16 2008'

#findPos_at = data.find('@')
#findPos_space = data.find(' ')

#email = data[findPos_at+1 data = 'From stephen@gmail.com Sat Jun 5 09:14:16 2008'

#findPos_at = data.find('@')
#findPos_space = data.find(' ')

#email = data[findPos_at+1:findPos_space]

#print(email)
#:findPos_space]

#print(email)





count = 0
total = 0 
fName = 'mbox-short.txt'
try: 
    fhand = open(fName)
except: 
    print(f"File cannot be opened: {fName} ")
    exit()

for i in fhand:
    if i.find('X-DSPAM-Confidence') == -1:
        continue
    confidence = float(i.split()[1])
    count+= 1
    total+= confidence
    

average = total / count
print("Average confidence:", average)