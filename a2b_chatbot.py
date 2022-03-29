print("\tWelcome you to \"Adayar Ananda Bhavan\"(veg.Restaurant)")
print("How can I help you?")
answers=["\thai","\thello","\t7AM - 10.30PM","\tYes.we have car parking in front of restaurant with no charges.","\tMORNING MENU\t","\nIDLI--45 \nSAMABAR IDLI--55 \nRAVA IDLI--50 \nIDIYAPPAM--60 \nDOSAI \nPLAIN DOSAI--65\nONION DOSAI--75\nPODI DOSAI--85\nMASALA DOSAI--90\nA2B COMBOS MINI TIFFIN--90","\tLUNCH MENU\t","\nVaraity rice(sambar-lemon-tomoto-curd)--55\nfull meals--110","\tDINNER\t","\nChapathi--65\nPorota--75 \nBEVERAGES\nMASALA TEA\nROSE MILK --65\nMANGO LASSI--75\nSTRAWBERRY MILKSHAKE--85\nAVACADO MILKSHAKE--85","\tNO,it is pure veg restaurant.","\tthank you.we also love you!","\tsorry.I can't understand..","\tyou are my creator","\tyes.we serve north indian dishes in dinner time","Cash\ndebit\\credit Cards\nUPI transations.","\tSure.use the link below","\thttps://a2bva.com/order-online/","\tThank you for visiting"]

def hai():
    print(answers[0])
def hello():
    print(answers[1])
def timing():
    print(answers[2])
def menu():
    me=int(input("[1]tiffin[2]lunch[3]dinner[4]All menu\nEnter: "))
    if me==1:
        print(answers[4],answers[5])
    elif me==2:
        print(answers[6],answers[7])
    elif me==3:
        print(answers[8],answers[9])
    else:
        print(answers[4],answers[5])
        print(answers[6],answers[7])
        print(answers[8],answers[9])
def parking():
    print(answers[3])
def nonveg():
    print(answers[10])
def love():
    print(answers[11])
def sorry():
    print(answers[12])
def creator():
    print(answers[13])
def north():
    print(answers[14])
def payment():
    print(answers[15])
def online():
    print(answers[16])
    print(answers[17])
def table():
    print(answers[16])
    print(answers[17])
def thank():
    print(answers[18])

ques={"hai":hai,"hello":hello,"timing":timing,"menu":menu,"car parking":parking,"nonveg is available":nonveg,"i love you":love,"who is your creator":creator,"do you serve north indian dishes":north,"payment option":payment,"can i order through online":online,"can i book table":table,"thank you":thank}

while True:
    ab=input()
    if ab in ques:
        ques[ab]()
    else:
        sorry()
