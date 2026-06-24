import json
import random
import string
from pathlib import Path


class bankacc:
    try: 
        database = 'bankacc.json'
        dummy = []
        if Path(database).exists():
            with open(database) as fs:
                dummy = json.loads(fs.read())
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An error occured as {err}")

#for update in json file
    def update(self):
      try:
        with open(bankacc.database, "w") as f:
            json.dump(bankacc.dummy, f, indent=4)
      except Exception as err:
          print(f"An error occured as {err}")

#for generate acc no
    @staticmethod
    def __accnumbergenerator():
        try:
            alpha = random.choices(string.ascii_letters, k=3)
            n = random.choices(string.digits, k=3)
            spchar = random.choices("!@#%^&*", k=2)
            num = alpha + n + spchar
            random.shuffle(num)
            return "".join(num)
        except Exception as err:
         print(f"An error occured as {err}")

#for creating account
    def creatingaccount(self):
        try:
            info = {
                "name": input("tell your name:- "),
                "age": int(input("tell your age:- ")),
                "email": input("tell your email:- "),
                "pin": int(input("tell your 4 number pin:- ")),
                "account_no": bankacc.__accnumbergenerator(),
                "Balance": 0
            }

            if info['age'] < 18 or len(str(info['pin'])) != 4:
                print("You can't create your account")
            else:
                print("ACCOUNT CREATED SUCCESSFULLY")
                for i in info:
                    print(f"{i} : {info[i]}")
                print(f"Note down your account no, {info['account_no']}")
                bankacc.dummy.append(info)
                bankacc.update(self)
        except Exception as err:
          print(f"An error occured as {err}")  

#for deposite money
    def depositmoney(self):
        try:
            acc_no = input("Enter your Account number:- ").strip()
            pin = int(input("Enter your Pin number:- "))
            userdata = [i for i in bankacc.dummy if i["account_no"] == acc_no and i["pin"] == pin]

            if not userdata:
                print("NO DATA FOUND!!")
            else:
                amount = int(input("Enter how much you want to deposit:- "))
                if amount > 20000 or amount <= 0:
                    print("You can only deposit amount between 1 and 20000")
                else:
                    userdata[0]["Balance"] += amount
                    print(f"AMOUNT DEPOSITED SUCCESSFULLY! , Your current balane is {userdata[0]["Balance"]}")
                    bankacc.update(self)  
        except Exception as err:
          print(f"An error occured as {err}")

#for withdraw money
    def withdrawmoney(self):
        try:
            acc_no = input("Enter your Account number:- ").strip()
            pin = int(input("Enter your Pin number:- "))
            userdata = [i for i in bankacc.dummy if i["account_no"] == acc_no and i["pin"] == pin]

            if not userdata:
                print("NO DATA FOUND!!")
            else:
                amount = int(input("Enter how much you want to Withdraw:- "))
                if userdata[0]["Balance"] < amount:
                    print("You don't have enough balance to withdraw")
                else:
                    userdata[0]["Balance"] -= amount 
                    print(f"AMOUNT WITHDREW SUCCESSFULLY, Your remaining balance is {userdata[0]["Balance"]}")  
                    bankacc.update(self)
        except Exception as err:
          print(f"An error occured as {err}")
#for showing details 
    def showdetails(self):
        try:
            acc_no = input("Enter your Account number:- ").strip()
            pin = int(input("Enter your Pin number:- "))
            userdata = [i for i in bankacc.dummy if i["account_no"] == acc_no and i["pin"] == pin]
            if not userdata:
                print("No Such Data Found")
            else:
                print("Your Infomation is")
                for i in userdata[0]:
                    print(f"{i} : {userdata[0][i]}")
        except Exception as err:
          print(f"An error occured as {err}")

#For updating details
    def updatedetails(self):
        try:
            acc_no = input("Enter your Account number:- ").strip()
            pin = int(input("Enter your Pin number:- "))
            userdata = [i for i in bankacc.dummy if i["account_no"] == acc_no and i["pin"] == pin]
            if not userdata:
                print("No Data Found")

            print("You can only update name,pin and email address :- n/n/")
            print("fill the details for change or leave it for empty ")
            newinfo = {
                "name": input("Enter your new name or Enter for skip:-"),   
                "email": input("Enter your new Email or Enter for skip:-"),
                "pin" : input("Enter your new Pin or Enter for skip:-")
            }
            for i in newinfo:
                if newinfo["name"] == "":
                    newinfo["name"] = userdata[0]["name"]

                if newinfo["email"] =="":
                    newinfo["email"] = userdata[0]["email"]

                if newinfo["pin"] == "":
                    newinfo["pin"] = userdata[0]["pin"]

                newinfo["age"] = userdata[0]["age"]
                newinfo["account_no"] = userdata[0]["account_no"]
                newinfo["Balance"] = userdata[0]["Balance"]

                if type(newinfo["pin"]) == str:
                    newinfo["pin"] = int(userdata[0]["pin"])
                
                for i in newinfo:
                    if newinfo[i] == userdata[0][i]:
                        continue
                    else:
                        userdata[0][i] = newinfo[i]
                bankacc.update(self)
                print("UPDATED DETAILS SUCCESSFULLY")

        except Exception as err:
         print(f"An error occured as {err}")    

#for delete
    def deletedata(self): 
        try:
            acc_no = input("Enter your Account number:- ").strip()
            pin = int(input("Enter your Pin number:- "))

            userdata = [i for i in bankacc.dummy if i["account_no"] == acc_no and i["pin"] == pin]
            if not userdata:
                print("No Data Found")
            else:
                check = input("If you actualy want to delete your account then press 1  and you dont want to delete account then press 2 ")
                if check == 2:
                    print("bypassed")
                else:
                    index = bankacc.dummy.index(userdata[0])
                    bankacc.dummy.pop(index)
                    bankacc.update(self)
                    print("DELETE ACCOUNT SUCCESSFULLY")
        except Exception as err:
            print(f"An error occured as{err} ")


user = bankacc()

print("Press 1 for creating an account")
print("Press 2 for depositing the money in the bank account")
print("Press 3 for withdrawing money to the bank account")
print("Press 4 for checking the details to your account")
print("Press 5 for updating account")
print("Press 6 for deleting account")

response = int(input("Enter Your respone:- "))

if response == 1:
    user.creatingaccount()
elif response == 2:
    user.depositmoney()
elif response == 3:
    user.withdrawmoney()
elif response == 4:
    user.showdetails()
elif response == 5:
    user.updatedetails()
elif response == 6:
    user.deletedata()