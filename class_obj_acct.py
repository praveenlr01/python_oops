db={}

class create:
    def reg():
        if len(db)==0:
            un=input("Enter your username: ")
            pw=input("Enter your password: ")
            db.update({un:pw})
            print(db)
        elif len(db)!=0:
            un=input("Enter your username : ")
            for i in db:
                if i in un:
                    print("Username is already taken...")
                    break 
            else:
                pw=input("Enter your Password: ")
                db.update({un:pw})
                print(db)      
        else:
            print("")               
c=create

class login:
    def log():
        un=input("Enter your username: ")
        if un in db:
            pw=input("Enter your password: ")
            if pw==db[un]:
                print("Login sucessfully.")
                a.act()
            else:
                print("Incorrect password.")
        else:
            print("Invalid username.")
l=login

class activity:
    def act():
        l,p,c,s=0,0,0,0
        while True:
            opt=int(input("[1]Like [2]Comment [3]Post [4]Share\nEnter: "))
            if opt==1:
                l+=1
                print("no of Like is = ",l)
            elif opt==2:
                c+=1
                print("no of comment is = ",c)
            elif opt==3:
                p+=1
                print("no of post is = ",p)
            elif opt==4:
                s+=1
                print("no of share is = ",s)
            else:
                print("Invalid Entery.")
a=activity
        
while True:
    opt=int(input("[1]Create [2]Login \nEnter: "))
    if opt==1:
        c.reg()
    elif opt==2:
        l.log()
    else:
        print("Invalid Entery.")
