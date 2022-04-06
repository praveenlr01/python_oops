class _main:
    def opt():
        while True:
            opt=int(input("[1]Create [2]Login \nEnter: "))
            if opt==1:
                atm_cre.cre()
            elif opt==2:
                atm_log.log()
            else:
                print("Invalid Entery.")
main=_main

class create(_main):
    def __init__(self):
        self.db={}
    def cre(self):
        un=input("Enter your username: ")
        pin=int(input("Enter your pin number: "))
        self.db.update({un:[pin,500]})
atm_cre=create()
                
class login(create):
    def __init__(self):
        self.un=""
    def log(self):
        self.un=input("Enter your username: ")
        for i in atm_cre.db:
            if i == self.un:
                pw=int(input("Enter your pin number: "))
                if pw==atm_cre.db[self.un][0]:
                    print("Login successfully..")
                    atm_act.act()
                    break
                else:
                    print("Incorrect password.")
                    break
        else:
            print("Invalid username.")
atm_log=login()

class activity(login):
    def act(self):
        while True:
            opt=int(input("[1]view balance [2]withdrawal [3]Deposit [4]Cancel \nEnter: "))
            if opt==1:
                print("Your current balance is : ",atm_cre.db[atm_log.un][1])
            elif opt==2:
                wid=int(input("Enter the amount to be withdrawal: "))
                atm_cre.db[atm_log.un][1]-=wid
                print("Your current balance is : ",atm_cre.db[atm_log.un][1])
            elif opt==3:
                bal=int(input("Enter the amount to be Deposit: "))
                atm_cre.db[atm_log.un][1]+=bal
                print("Your current balance is : ",atm_cre.db[atm_log.un][1])
            elif opt==4:
                break
            else:
                print("Invalid Entery.")                
atm_act=activity()

main.opt()
