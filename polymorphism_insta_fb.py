class _main:
    def _main_pro(self):
        while True:
            opt=int(input("[1]Insta [2]Facebook \nEnter: "))
            if opt==1:
                i_main.opt()
            elif opt==2:
                fb_main.opt()
            else:
                print("Invalid Entery.")
users_main=_main()

class main_insta(_main):
    def opt(self):
        while True:
            opt=int(input("[1]Create [2]Login [3]Cancel\nEnter: "))
            if opt==1:
                i_cre.cre()
            elif opt==2:
                i_log.log()
            elif opt==3:
                break
            else:
                print("Invalid Entery.")
i_main=main_insta()

class create_insta(_main):
    def cre(self):
        print("\"Welcome to Instagram\"")
        un=input("Enter Username: ")
        pw=input("Enter Password: ")
        db_i.update({un:pw})
i_cre=create_insta()

class login_insta(_main):
    def log(self):
        un=input("Enter Your username: ")
        for i in db_i:
            if i==un:
                pw=input("Enter your password: ")
                if pw==db_i[un]:
                    print("Login Successfully..")
                    i_act.act()
                    break
                else:
                    print("Invalid password.")
                    break
        else:
            print("Invalid username.")
i_log=login_insta()

class activity_insta(_main):
    def act(self):
        l,c,p,s=0,0,0,0
        while True:
            optt=int(input("[1]like [2]Comment [3]post [4]Share [5]logout \nEnter: "))
            if optt==1:
                l+=1
                print("no of like is ",l)
            elif optt==2:
                c+=1
                print("no of comment is ",c)
            elif optt==3:
                p+=1
                print("no of post is ",p)
            elif optt==4:
                s+=1
                print("no of share is ",s)
            elif optt==5:
                break
            else:
                print("Invalid Entery.")
i_act=activity_insta()

class main_facebook(_main):
    def opt(self):
        while True:
            opt=int(input("[1]Create [2]Login [3]Cancel \nEnter: "))
            if opt==1:
                fb_create.cre()
            elif opt==2:
                fb_login.log()
            elif opt==3:
                break
            else:
                print("Invalid Entery.")
fb_main=main_facebook()

class create_fb(_main):
    def cre(self):
        print("\"Welcome to Facebook\"")
        un=input("Enter Username: ")
        pw=input("Enter password: ")
        db_fb.update({un:pw})
fb_create=create_fb()

class Login_fb(_main):
    def log(self):
        un=input("Enter your username: ")
        for i in db_fb:
            if i == un:
                pw=input("Enter your password: ")
                if pw==db_fb[un]:
                    print("Login successfully.")
                    fb_act.act()
                    break
                else:
                    print("incorrect password.")
                    break
        else:
            print("Invalid username.")
fb_login=Login_fb()

class activity_fb(_main):
    def act(self):
        l,c,p,s=0,0,0,0
        while True:
            optt=int(input("[1]Like [2]comment [3]post [4]share [5]Logout \nEnter: "))
            if optt==1:
                l+=1
                print("no of like is ",l)
            elif optt==2:
                c+=1
                print("no of comment is ",c)
            elif optt==3:
                p+=1
                print("no of post is ",p)
            elif optt==4:
                s+=1
                print("no of share is ",s)
            elif optt==5:
                break
            else:
                print("Invalid Entery.")
fb_act=activity_fb()

db_i={}
db_fb={}
users_main._main_pro()
