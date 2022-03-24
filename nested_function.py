print("\t\tWelcome to Atm..\t")
db={}

def create():
    un=input("Enter your username: ")
    pin=int(input("Enter your pin number: "))
    db.update({un:[pin,500]})
    
def login():
    while True:
        un=input("Enter your Username: ")
        if un in db:
            pin=int(input("Enter your Pin: "))
            if db[un][0]==pin:
                print("Login sussfully...")
                activity(un)
                break
            else:
                print("Incorrect pin.")
                break
        else:
            print("Incorrect username.")
        
def activity(un):
    while True:
        opt=int(input("[1]View balance [2]Deposit [3]Withdrawal [4]Transfer\nEnter: "))
        if opt==1:
            print("Your balance is : ",db[un][1])
        elif opt==2:
            dep=int(input("Enter the amount to be Deposit: "))
            db[un][1]=db[un][1]+dep
            print("Your current balance is: ",db[un][1])
        elif opt==3:
            wid=int(input("Enter the amount to be withdrawal: "))
            db[un][1]=db[un][1]-wid
            print("Your current balance is: ",db[un][1])
        elif opt==4:
            rec=input("Enter the reciver name:")
            if un!=rec:
                if rec in db:
                    tra=int(input("Enter the amount to be transfered: "))
                    db[rec][1]=db[rec][1]+tra
                    db[un][1]=db[un][1]-tra
                    print("Your current balance is: ",db[un][1])
                else:
                    print("Invalid username.")
            else:
                print("Incorrect username.")
        else:
            print("Invalid Entery.")
                       
def _main():
    while True:
        opt=int(input("[1]Create [2]Login \nEnter: "))
        if opt==1:
            create()
        elif opt==2:
            login()
        else:
            print("Invalid Entery..")
_main()
