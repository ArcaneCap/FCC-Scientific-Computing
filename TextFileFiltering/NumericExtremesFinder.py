userList = []
choice = ""

while True:
    userNum = input("Enter a number ")
    if userNum.isdigit():
        userList.append(int(userNum))
        if input("Enter another? (Y/N) ").lower() == "n":
            break
  
    else: 
        print("Enter a valid number")

print(f"Maximum:  {max(userList)}" )
print(f"Minimum: {min(userList)}")
