#28.06.2022   son topish o'yini
def son_topaman(x=100):
    print("Keling o'ylangan son topish o'yinini o'ynaymiz ")
        #kamyutera uylesha mon meyobem
    import random
    r= random.randint(1, x)
    otvet = int(input(f"Men 1-{x} gacha son o'yladim topishga harakat qiling: "))
    taxmin =0
    while True:
        taxmin +=1
        if otvet > r:
            otvet = int(input("Xato! Men o'ylagan son bundan kichikroq: "))
        elif otvet < r:
            otvet = int(input("Xato! Men o'ylagan son bundan kattaroq: "))
        else:
            otvet =f"Topdingiz men {r} sonini o'ylagandim "
            break
    print(otvet,f"\nSiz {taxmin} urinush bilan topdingiz!")
    return taxmin

def son_top_pc(x=100):
    import random
    ry = random.randint(1,x//2)
    input("Endi siz 1- 100 gacha son o'ylang men topishga harakat qilaman. enter ni bosing: ")
    print("Siz o'ylagan son, men aytgan sondan katta bo'lsa (+)  kichkina bo'lsa (-) topgan bo'lsam (T) ni yuborasiz ")
    birinchi = 0
    oxirgi = x
    taxmin_kamp=0
    while True:
        taxmin_kamp += 1
        savol = input(f"siz {ry} o'yladingiz: ")
        if savol == "+" :
            birinchi =ry
            ry += (oxirgi - birinchi) //2
        elif savol == "-" : 
            oxirgi =ry
            ry -= (oxirgi - birinchi)//2 
        elif savol.lower() == 't':
            print(f"men {taxmin_kamp} urinish bilan topdim")
            break
    return taxmin_kamp

def play(x=100) :
    """son topish o`yini. Siz play(x) argument kiriting misol: play(10)
    Kiritilgan x argument o`yinning 1 dan x gacha  bo`lishini taminlaydi 
    x son hisonga olinmaydi!!"""
    push = True
    bot = 0
    odam = 0
    while push:
        taxmin_users =son_topaman(x)
        taxmin_kmp= son_top_pc(x)
        if taxmin_users > taxmin_kmp:
            bot +=1
            s ="Men yutdim"
        elif taxmin_users < taxmin_kmp:
            s ="Tabriklayman Siz yutdingiz"
            odam += 1
        elif taxmin_users == taxmin_kmp:
            s ="natija durrang buldi"
        print(f"{s}\nNatija: Men-{bot}  siz-{odam}")
        push = int(input("yana o'ynaymizmi: ha(1) / yo'q(0)  "))
play()
