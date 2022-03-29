class Insta:
    def __init__(self,un):
        self.un=un
    def create(self):
        un=input("Enter Username: ")
        pw=input("Enter Password: ")
        db.update({un:pw})
        print("created successfully.")
        
class Insta_log(Insta):
    def __init__(self,un,l,c,p,s,i):
        self.un=un
        self.l=l
        self.c=c
        self.p=p
        self.s=s
        self.i=i
    def login(self):
        self.un=input("Enter Your username: ")
        for b in db:
            if b==self.un:
                pw=input("Enter your Password: ")
                if pw==db[self.un]:
                    print("Login successfully...")
                    user.activity()
                else:
                    print("Incorrect password.")
                    break
        else:
            print("Invalid Username.")
            
    def activity(self):
        while True:
            opt=int(input("[1]Like [2]Comment [3]Post [4]Share[5]view activity \nEnter: "))
            self.i+=1
            if opt==1:
                user.like()
            elif opt==2:
                user.comt()
            elif opt==3:
                user.post()
            elif opt==4:
                user.share()
            elif opt==5:
                user.act()
            else:
                print("Invalid Entery")
                
    def like(self):
        self.l+=1
        print("no of like is: ",self.l)
        act.update({self.i:f'{self.i}.no of like is : {self.l}'})
    def comt(self):
        self.c+=1
        print("no of comment is: ",self.c)
        act.update({self.i:f'{self.i}.no of comment is : {self.c}'})
    def post(self):
        self.p+=1
        print("no of post is: ",self.p)
        act.update({self.i:f'{self.i}.no of post is : {self.p}'})
    def share(self):
        self.s+=1
        print("no of share is: ",self.s)
        act.update({self.i:f'{self.i}.no of share is : {self.s}'})
    def act(self):
        for x in range(len(act)):
            print(act[x+1])
        user.login()
    
db={}
act={}
user=Insta_log(un="",l=0,c=0,p=0,s=0,i=0)

while True:
    optt=int(input("[1]create [2]Login\nEnter:"))
    if optt==1:
        user.create()
    elif optt==2:
        user.login()
    else:
        print("Invalid Entery.")
