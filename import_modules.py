from cre_log_mod import I_login
from act_mod import activity

db={}
i_users=I_login(db)
while True:
    opt=int(input("[1]Create [2]Login [3]Cancel \nEnter: "))
    if opt==1:
        i_users.cre()
    elif opt==2:
        i_users.login()
    elif opt==3:
        break
    else:
        print("Invalid Entery.")

