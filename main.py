import os

def getInt(message):
  temp = 0
  while(True):
    try:
      temp = int(input(message))
      break
    except:
      print("That is not the proper value.")
  return temp
  
def getStr(message):
  while(True):
    temp = input(message)
    try:
      temp = int(temp)
      print("That is not the proper value.")
    except:
      temp.lower
      break
  return temp

def menu():
  while(True):
    print("1. Create a account")
    print("2. View account.")
    print("3. Deposite money.")
    print("4. Withdraw money.")
    print("5. Exit.")
    temp = getInt("Write which choice you would like: ")
    if (temp == 1):
      createTXT()
    elif(temp == 5):
      print("Thank you for using our service.")
      break
    elif(temp == 2 or temp == 3 or temp == 4):
      ided(temp)
    else:
      print("Give a real answer.")
    print()
      
def ided(choice):
  temp = getInt("Write your ID: ")
  id = str(temp) + ".txt"
  if(os.path.exists(id)):
    if(choice == 2):
      openTXT(id)
    elif(choice == 3):
      deposite(id)
    elif(choice == 4):
      withdraw(id)
    

def deposite(id):
  balance = 0
  with open(id) as f:
    money = int(f.read())
    print(f"Your balance is currently ${money}.")
    temp = getInt("How much would you like to deposite? ")
    balance = money + temp
  print(balance)
  print(f"Your new balance is : ${balance}.")
  with open(id, "w") as f:
    f.write(str(balance))

def withdraw(id):
  balance = 0
  with open(id) as f:
    money = int(f.read())
    print(f"Your balance is currently ${money}.")
    temp = getInt("How much would you like to withdraw? ")
    balance = money - temp
  print(balance)
  print(f"Your new balance is : ${balance}.")
  with open(id, "w") as f:
    f.write(str(balance))

def openTXT(id):
  with open(id) as f:
    h = f.read()
    print(f"Your balance is ${h}")

def createTXT():
  while(True):
    temp = getInt("Write your ID: ")
    id = str(temp) +".txt"
    if(os.path.exists(id)):
      print("this account is already created with us. Sorry pal!")
    else:
      create(id)
      break

def create(id):
  with open(id, "w") as f:
    f.write("0")
  with open(id) as f:
    h = f.read()
    print(f"Your account has been created! Your starter balance is ${h}.")
  while(True):
    a = getStr("Would you like to deposite some of your preciouse cash? Y/N; ")
    if(a == "y"):
      deposite(id)
      break
    elif(a == "n"):
      print("Thank you for making a account from us.")
      break
    else:
      print("You must make a decision you fooool!")
  
menu()
