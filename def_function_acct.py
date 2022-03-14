
users={}

def create():
    un=input("Enter your username: ")
    if un not in users:
         pw=input("Enter your password: ")
         users.update({un:pw})
    else:
        print("Username is already taken..")
        
def login():
    print("Login page")
    una=input("Enter your username: ")
    for i in users:
        if i in una:
            pws=input("Enter your password: ")
            if pws==users[una]:
                print("Login successfully...")
                break
            else:
                print("Incorrect password.")
                break
    else:
        print("Incorect username.")
        
def activites():
    like,comt,share,post=0,0,0,0
    while True:
        opt=int(input("[1]Like\t[2]Commant\t[3]Post\t[4]share\t[5]Logout\nEnter:"))
        if opt==1:
            like+=1
            print("No of Likes = ",like)
        elif opt==2:
            comt+=1
            print("No of Comments = ",comt)
        elif opt==3:
            post+=1
            print("No of Post = ",post)
        elif opt==4:
            share+=1
            print("No of Share = ",share)
        elif opt==5:
            print("Logout successfully..")
            login()
            break
        else:
            print("Invalid Entery.")
                  

def changes():
    while True:
        optt=int(input("[1] username change \t [2] password change \nEnter: "))
        if optt==1:
            uname=input("Enter your username: ")
            for i in users:
                if i in uname:
                    pwsd=input("Enter your password: ")
                    if users[uname]==pwsd:
                        new=input("Enter your new username: ")
                        users.update({new:users.pop(uname)})
                        print("Your Username is changed successfully...")
                        print(users)
                        break
                    else:
                        print("Incorrect password.")
                        break
            else:
                print("Incorrect username.")
        elif optt==2:
            uname=input("Enter your username: ")
            for i in users:
                if i in uname:
                    pwd=input("Enter your password: ")
                    if users[uname]==pwd:
                        newpas=input("Enter your new Password: ")
                        users[uname]=newpas
                        print("Your password is changed successfully...")
                        print(users)
                        break
                    else:
                        print("Incorrect password.")
                        break
            else:
                print("Incorrect username.")
        else:
            print("Invalid Entery.")

while True:
    opt=int(input("[1]create a account\t[2]Login\t[3]activities\t[4]changes\nEnter: "))
    if opt==1:
        create()
    elif opt==2:
        login()
    elif opt==3:
        activites()
    elif opt==4:
        changes()
    else:
        print("Invalid Entery.")
