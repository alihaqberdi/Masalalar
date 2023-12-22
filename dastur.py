#begin-1
print("""masala-1
P=a * 4""")
a = int(input("a ="))
print("p=",a*4)

#----------------------------------------------------------------------

# #begin-2
print(""" masala-2     
S=a2""")
b = int(input("a ="))
print("S=",b*b)

#----------------------------------------------------------------------

# #begin-3
print(""" masala-3     
S=a*b 
p=2*(a+b)""")
sona = int(input("a ="))
sonb = int(input("b ="))
print("S=",sona*sonb )
print("p=",2*(sona+sonb))

#----------------------------------------------------------------------

#begin-4
print("""masala-4 
l=p*d
p =3.14""")
d=int(input("d="))
print("L=",d*3.14)

#----------------------------------------------------------------------

# begin-5
print("""masala -5
V =a3
S=6*a2""")
a = int(input("a="))
print("""V =""",a**3,"\nS=",6*(a**2))

#----------------------------------------------------------------------

#begin-6
print("""masla-6
V=a*b*c
S=2*(a*b+b*c+a*c)""")
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
print("V=",a*b*c,"S=",2*(a*b+b*c+a*c))

#----------------------------------------------------------------------

#begin-7
print("""masala-7
L=2*p*R
S=p*R2""")
r = int(input("r = "))
print("L=",2*3.14*r,"\nS =",3.14*(r**2))

#----------------------------------------------------------------------

#begin-8
print("""masala-8
(a+b)/2""")
a,b = map(int,input("a,b son kiriting").split())
print((a+b)/2)

#----------------------------------------------------------------------

#begin-9
print("""masala-9
ildiz(a*b) """)
a,b = map(int,input("a,b son kiriting").split())
print("javob: ",(a*b)**(1/2))

#----------------------------------------------------------------------

#begin-10
print("""masala-10
nolga teng bulmagan ikkita son kiritilsiz ularning yig'indisi ayirmasi ko'paytmasi bulinmasi va har birining kvadrati chiqarilsin""")
a,b = map(int,input("a,b son kiriting").split())
print(f"qo'shilsa = {a+b}  kvadrati= {(a+b)**2}\nayirmasi= {a-b}  kvadrati= {(a-b)**2}\nko'paytmasi = {a*b}  kvadrati= {(a*b)**2}\nbo'linmasi = {a/b}  kvadrati= {(a/b)**2}")
      
#----------------------------------------------------------------------

#begin-11
print("""masala-11
nolga teng bulmagan ikkita son kiritilsin ularning yig'indisi ko'paytmasi va moduli aniqlansin""")
a,b = map(int,input("a,b son kiriting").split())
print(f"ko'paytmasi = {a*b} \nyig'indisi = {a+b} ") 

#----------------------------------------------------------------------

#begin-12
print("""masala-12
C=ildiz(a2+b2)
P=a+b+c""")
a,b = map(int,input("a,b son kiriting").split())
c=(a**2+b**2)**(1/2)
p = a+b+c
print(f"C= {c} \nP ={p}")

#----------------------------------------------------------------------

#begin-13
print("""masala-13
r1=r2=(r1>r2)
s1 = p*r1 yuzasi
s2 = p*r2 yuzasi
s3 = p*(r1 - r2) ayirmasi
aniqlansin""")
r1,r2 = map(int,input("r1,r2 son kiriting").split())
p =3.14
s1 = p*r1
s2 = p*r2
s3 = p*(r1-r2)
print(f"S1= {s1}\nS2= {s2}\nS3= {s3}")

#----------------------------------------------------------------------

#begin-14
print("""masala-14
L=2*p*r
S=p*r2""",end="")
r =int(input("r = "))
p=3.14
L = 2*p*r
S = p*(r**2)
print("\nL= ",L," \nS=",S)

#----------------------------------------------------------------------

#begin-15
print("""masala-15
L = 2*p*r
S = p*r2 """,end="")
r = int(input("r = "))
p =3.14
L =2*p*r
S =p*(r**2) 
print(f"\nL = {L} \nS = {S}")

#----------------------------------------------------------------------

#begin-16
print("""masala-16
x1  x2  sonlar orasidagi masofa aniqlansin""",end="")
x1,x2 = map(int,input("x1,x2 =  ").split())
km = x1 -x2
print(f"masofa {km}")

#----------------------------------------------------------------------

#begin-17
print("""masala-17
AC  BC uzunligini,
kesmalar uzunligining yig'indisini topilsin""")
a,b,c = map(int,input("a  b  c =  ").split())
ac = a-c
bc = b-c
plus =ac+bc
print(f"AC ning uzunligi = {ac}\nBC ning uzunligi = {bc}\nuzunliklarning yig'indisi = {plus}")

#----------------------------------------------------------------------

#begin-18
print("""masala-18
A C B nuqtalar berilgan A va B orasida C nuqta joylashgan
AC va BC ning uzunligining ko`paytmasi ?   """)
a,c,b = map(int,input("A C B = ").split())
ac = c-a
bc = b-c
kopayturuv = ac * bc
print(f"AC ning uzunligi = {ac}\nBC ning uzunligi = {bc}\nularning uzunligini ko`paytmasi = { kopayturuv}")

######################################################################################################################################################################


#masalalar 22.06.2022 yozilgan

                    #integer
# integer-1
sm = int(input("santimetr kiriting: "))
metr = sm // 100
smq = sm % 100
print(f"{sm} sm=  {metr}-metr {smq} santimetr")



# integer-2
kg =int(input("kg kirit: "))
to = kg //1000
toq = kg %1000
print(f"{kg} kilogram = {to} tonna {toq} kg")



# integer-3
bayt =int(input("bayt kiriting: "))
kb = bayt // 1024
kbq =bayt % 1024
print(f"{bayt} bayt = {kb} kilobayt {kbq} bayt")



# integer-4
a ,b = map(int,input("a > b.  son kirit a b: ").split())
javob = a // b
print(javob ,"martta")



# integer-5
a ,b = map(int,input("a > b.  son kirit a b: ").split())
javob = a // b
javobq = a % b
print(javob ,"martta",javobq,"qoldiq")



# integer-6
raqam =int(input("son kirit: "))
onlik = raqam // 10 * 10
birlik = raqam % 10
print(f"{raqam} raqamida  {onlik} o`nlik  {birlik} birlik")



# integer-7
son1 = int(input("son kirit: "))
qoshish = (son1 // 10)+(son1 % 10)
print(qoshish)



# integer-8
son2 = int(input("son kirit: "))
teskari = son2 % 10 * 10 + son2 // 10
print(teskari)



# integer-9
son3 = int(input("son kirit: "))
yuz = son3 // 100
print("yuzlar xonasidagi raqami = ",yuz)


# integer-10
son4 = int(input("son kirit: "))
birlik = son4 % 10
onlik = (son4 % 100 ) // 10 
print(f"raqam: {son4} \nbirliklar xonasidagi raqami {birlik}  \no'nliklar xonasidagi raqami  {onlik}")



# integer-11
son5 = int(input("son kirit: "))
yigindi = (son5 // 100) +(son5 % 100 // 10)+(son5 % 10) 
print(f"son: {son5}  \nyig`indi = {yigindi}")



#integer -12 
a =input("uch xonali son kiriting teskarisiga chiqarib beraman: ")
print(a[-1::-1])



#integer-13
son =int(input("uch xonali son kiriting: "))
javob =son // 100
print(((son % 100)*10)+javob)



#integer-14
son =int(input("uch xonali son kiriting: "))
javob = son % 10
print(javob*100+(son //10))


#integer-15
a = int(input("uch xonali son kiriting: "))
yuz = ((a % 100) - (a % 10))*10
on = a // 100 * 10
bir = a % 10
obshi = yuz + on + bir
print(obshi)



#integer-16
a = int(input('uch xonali son kiriting: '))
yuz = (a // 100)*100
on = (a %10)*10
bir = (a % 100) // 10
yig = yuz + on + bir
print(yig)



#integer17
a = int(input('son kiriting: '))
x = a // 100
xq =a % 100
print("yuzliklar orasidagi soni",x,"\nqoldiq",xq)



#integer18
a = int(input('son kiriting: '))
x = a // 1000
xq =a % 1000
print("yuzliklar orasidagi soni",x,"\nqoldiq",xq)



#integer19
a = int(input('sekund kiriting: '))
minu = a //60
print(a,"sekund  ==",minu,"minut")



#integer20
a = int(input('sekund kiriting: '))
soat = a //3600
print(a,"sekund  ==",soat,"soat")



#integer21
a = int(input('sekund kiriting: '))
minu = a //60
sekund = a % 60
print(a,"sekund  ==",minu,"minut",sekund,"sekund")


#integer22
a = int(input('sekund kiriting: '))
soat = a //3600
secund = a % 3600
print(f"{a} sekund == {soat} soat  {secund} sekund")



#integer23
a = int(input('sekund kiriting: '))
soat = a //3600
minut = (a % 3600) // 60
secund = a % 60
print(f"{a} sekund == {soat} soat  {minut} minut {secund} sekund")



#integer-24
kun =int(input("shu yildagi 1 365 gacha bulgan sana kirit qaysi hafta ekanini topaman: "))
hafta = kun % 7
a = ['yakshanba','dushanba','seshanba','chorshanba','payshanba','jumma','shanba']
print(a[hafta])



#integer-25
kun =int(input("shu yildagi 1 365 gacha bulgan sana kirit qaysi hafta ekanini topaman: "))
hafta = kun % 7
a = ['yakshanba','dushanba','seshanba','chorshanba','payshanba','jumma','shanba']
print(a[hafta+3])


#integer-26
kun =int(input("shu yildagi 1 365 gacha bulgan sana kirit qaysi hafta ekanini topaman: "))
hafta = kun % 7
a = ['dushanba','seshanba','chorshanba','payshanba','jumma','shanba','yakshanba']
print(a[hafta])



#integer-27
kun =int(input("shu yildagi 1 365 gacha bulgan sana kirit qaysi hafta ekanini topaman: "))
hafta = kun % 7
a = ['dushanba','seshanba','chorshanba','payshanba','jumma','shanba','yakshanba']
print(a[hafta-2])



#integer-28
n = int(input("(hafta kunlari soni 1-7 (yaksanba ==1)  n="))
kun =int(input("shu yildagi 1 365 gacha bulgan sana kirit qaysi hafta ekanini topaman: "))
hafta = kun % 7
a = ['yakshanba','dushanba','seshanba','chorshanba','payshanba','jumma','shanba',]
print(a[hafta+(n-2)])



#integer29
a ,b ,c = map(int,input("a,b,c son kirit:").split())
ab = a*b 
ca =c**2
javob = ab // ca
javq = ab % ca
print(f"a b to'gri to'rt burchakning ichida  c ning kvadrati \n{javob} butun hamda {javq} qoldiq")


#integer30
n = int(input("yil kiriting: "))
print((n // 100)+1,"- yuz yillik")


###################################################################################################################################################################


       #shart operator masalalar
#if-1
son = int(input("son musbat bo'lsa 1 ga oshiriladi: "))
if son > 0:
    print(son+1)
else:
    print(son)          

#----------------------------------------------------------------------

#if-2
son = int(input("son musbat bo'lsa 1 ga oshirilsin aks holda 2 ga kamaytirilsin: "))
if son > 0:
    print(son+1)
else:
    print(son-2) 

#----------------------------------------------------------------------  

#if-3
son = int(input("son musbat bulsa 1 ga oshirilsin, manfiy bulsa 2 ga kamaytir, 0 ga teng bulsa 10 ni uzlashtirsin"))
if son > 0:
    print(son+1)
elif son == 0:
    print(10)
else:
    print(son-2)   

#----------------------------------------------------------------------  

#if-4
musbat = 0
rezult = map(int,input('xoxlahan musnat yo manfiy 3ta son kiriting:  ').split())
for raqam in rezult:
    if raqam > 0:
        musbat += 1     
print(f'{musbat} ta musbat son')

#----------------------------------------------------------------------  

#if-5
musbat = 0
manfiy = 0
rezult = map(int,input('xoxlahan musnat yo manfiy 3ta son kiriting:  ').split())
for raqam in rezult:
    if raqam > 0:
        musbat += 1
    else:
        manfiy +=1
print(f'{musbat} ta musbat son')
print(f'{manfiy} ta manfiy son')

#----------------------------------------------------------------------  

#if-6
son = map(int,input("sonni kattasini aniqlaymiz").split())
print(max(son))

#---------------------------------------------------------------------- 

#if-7
a = list(map(int,input("sonnig kichigini tartib raqamini aniqlaymiz: ").split()))
print(a.index(min(a))+1)

#---------------------------------------------------------------------- 

#if-8
a=list(map(int,input().split()))
print(max(a),min(a))

#---------------------------------------------------------------------- 

# #if-9
a,b=map(int,input().split())
b *=a 
print(a,b)

#---------------------------------------------------------------------- 

# #if-10
a,b = map(int, input().split())
if a != b:
    print(a+b)
if a == b:
    print(0)

#---------------------------------------------------------------------- 

# #if-11
a,b = map(int, input().split())
if a > b:
    x =a
elif a < b :
    x = b
else:
    x =0
print(x)

#---------------------------------------------------------------------- 

# #if-12
a,b,c = map(int, input().split())
if a > b and c > b:
    x =b
elif a > c and b > c:
    x =c
else:
    x =a
print(x)

#---------------------------------------------------------------------- 

# #if-13
a,b,c = map(int, input().split())
if a > b and c > b:
    x =b
elif a > c and b > c:
    x =c
else:
    x =a
print(x)

#---------------------------------------------------------------------- 

# #if-14
a,b,c = map(int,input('3 ta son kiritig:  ').split())
if a < b and a < c:
    print(a)
if b < a and b < c:
    print(b)
if c < b and c < a:
    print(c)
if a > b and a > c:
    print(a)
if b > a and b > c:
    print(b)
if c > b and c > a:
    print(c)

#---------------------------------------------------------------------- 

# #if-15
a,b,c = map(int,input('3 ta son kiritig:  ').split())
if a > b and a > c:
    print(a+b,a+c)
if b > a and b > c:
    print(b+a,b+c)
if c > b and c > a:
    print(c+a,c+b)

#---------------------------------------------------------------------- 

# #if-16
a,b,c = map(int,input('3 ta son kiritig:  ').split())
print(f"{a,b,c} sonlar berilgan agar tartiblangan bo`lsa ikkilantiriladi aks holda 2 qoshiladi")
if a < b < c :
    print(a*2,b*2,c*2)
else:
    print(a+2,b+2,c+2)   

#---------------------------------------------------------------------- 

# #if-17
a,b,c = map(int,input('3 ta son kiritig:  ').split())
print(f"{a,b,c} sonlar berilgan agar tartiblangan bo`lsa ikkilantiriladi aks holda 2 qoshiladi")
if a < b < c or a > b > c:
    print(a*2,b*2,c*2)
else:
    print(a+2,b+2,c+2)  

#---------------------------------------------------------------------- 

# #if-18
a,b,c= map(int,input('son kiriting 3 ta 2 ta si birxil bo`lsin 1 ta bir xil bolmagan sonni indexini topaman: \n').split())
if a != b and a !=c:
    print(1)
if b != a and b !=c:
    print(2)
if c != a and c !=b:
    print(3)

#---------------------------------------------------------------------- 

# #if-19
a,b,c,d= map(int,input('4 ta  son kiriting 3 ta si birxil bo`lsin 1 ta bir xil bolmagan sonni indexini topaman: \n').split())
g = a,b,c,d
g = list(g)
if a != b and a !=c and a!=d:
    print(1)
if b != a and b !=c and b != d:
    print(2)
if c != a and c !=b and c != d: 
    print(3)
if d != a and d !=b and d != c: 
    print(4) 

#---------------------------------------------------------------------- 

# #if-20
a,b,c = map(int,input('a katta son bolsin b c son kiriting a yaqin bo`lgan son va ualr orasidagi masofani topaman \n ').split())
if b-a < c-a:
    print(f"a ga yaqin son {b} va ualr orasidagi masofa {b-a}")
if b-a > c-a:
    print(f"a ga yaqin son {c} va ualr orasidagi masofa {c-a}")
    
###################################################################################################################################################################



            #for tsikl operatori masalalar
# for-1
print("""k  va  n var bor,   k qiymatni  n martta takrorlanuvchi masala   """)
k = input("biror suz yoki son kiriting: ")
n = int(input("necha martta takrorlansin"))
for l in range(n) :
    print(l+1,k)
print("k  qiymat",n,"martta takrorlandi")

#-----------------------------------------------------------------------------

# for-2
print("""a va  b qiymat bor a<b .   a  va b orasidagi butun sonlarni a va b ni ham chiqaruvchi masala 
chiqarilgan sonlar soni aniqlansin""")
a,b =map(int,input("a va b son kiriting").split())
son = 0
for n in range(a,b+1) :
    son += 1
    print(n)
print("chiqarilgan sonlar soni",son)

#---------------------------------------------------------------------------

# for-3
print("""a va b son berilgan. a va b sonlar orasidagi sonlarni   a va b dan tashqari kamayish tartibida chiqarilsin
chiqarilgan sonlar soni aniqlansin""")
a,b =map(int,input("a va b son kiriting: ").split())
s = 0
for n in range(b-1,a,-1) :
    s +=1
    print(n)
print(f"chiqarilgan sonlar soni {s}")

#-----------------------------------------------------------------------------

# for-4
print("""1 kg konfetning narxi 29999 berilgan.  kg? kanfet narxini aniqlanydigan masala""")
kon =int( input("kanfet kg sini kiriting: "))
for n in range(kon) :
    n += 1
    print(f"{n}-kg konfetning narxi {n*29999}")

#----------------------------------------------------------------------------

# for-5 
print("""1 kg konfetning narxi 29999 berilgan. 0.1,0,2 ...1 kg? kanfet narxini aniqlanydigan masala""")
kon =int( input("kanfet kg sini kiriting: "))
kon =kon*10
for n in range(kon) :
    n += 1
    n /=10
    print(f"{n}-kg konfetning narxi {n*29999}")

#------------------------------------------------------------------------

# for-6
print("""1 kg konfetning narxi 1000 berilgan. 1.2, 1.4, 1.6  ...2 kg? kanfet narxini aniqlanydigan masala""")
kon =int( input("kanfet kg sini kiriting: "))
kon =kon*5
for n in range(kon) :
    n += 1
    n /= 5
    print(f"{n}-kg konfetning narxi {n*1000}")

#----------------------------------------------------------------------------

# for-7
print("""a va ba son berilgan. a va b gacha bulga barcha butun sonlar yig'indisini hisobi """)
a,b =map(int,input("a va b son kiriting: ").split())
yig = 0
for n in range(a,b+1) :
    yig +=n
    print(n)
print(f"barcha butun sonlar yig'indisi: {yig}")

#------------------------------------------------------------------------------

# for-8
print("""a va ba son berilgan. a va b gacha bulga barcha butun sonlar ko'paytmasi hisobi """)
a,b =map(int,input("a va b son kiriting: ").split())
yig = 1
for n in range(a,b+1) :
    yig *=n
    print(n)
print(f"barcha butun sonlar ko'paytmasi: {yig}")

#----------------------------------------------------------------------

# for-9
print("""a va ba son berilgan. a va b gacha bulga barcha butun sonlar kvadratini hisobi """)
a,b =map(int,input("a va b son kiriting: ").split())
yig = 0
for n in range(a,b+1) :
    yig +=n**2
    print(n,"ning kvadrati:",n**2)
print(f"barcha butun sonlar kvadrati: {yig}")

#----------------------------------------------------------------------

#for- 10
kilent = int(input("son kirit: "))
s ="1"
mas =1
for n in range(2,kilent) :
    n= str(n)
    s += "+1/"+n
    n =int(n)
    mas +=1/n
print(s,"=",mas)

#----------------------------------------------------------------------

#for-11 
n = int(input("son kirit: "))
s = f"{n}**2"
javob = 0

for x in range(1,n) :
    n = str(n)
    x = str (x)
    s += "+("+n+"+"+x+")**2"
    n =int(n)
    x =int(x)
    l =n+x
    javob = javob + (l * l)
javob += (2*n)**2
javob +=n**2
s +=f"+(2*{n})**2"
print(s,"=",javob) 

#----------------------------------------------------------------------

#for-12
x = int(input("son kirit"))

s =""
for n in range(x) :
    n +=1
    n /= 10
    n =str(n)
    s +=n
print(s) 


#################################################################################################################################################################


#while-1
a,b =map(int,input().split())
while a>b :
    a-=b
print(a)

#----------------------------------------------------------------------

#while-2
a,b =map(int,input().split())
s=0
while a>=b:
    a-=b
    s+=1
print(s)

#----------------------------------------------------------------------

#while-3
a,b =map(int,input().split())
s=0
while a>=b:
    a-=b
    s+=1
print(s,a,'qoldiq')

#----------------------------------------------------------------------

#while-4
n = int(input())
s = 1
a = True
while a:
    s *= 3
    if n==s:
        print('3 ning darajasi')
        break
    if s > n :
        a = False
        print("3 ning darajasi emas")

#----------------------------------------------------------------------

#while-5
a=0
k = 1
n = int(input())
while n>0:
    k*=2
    n-=k
    a+=1
print(f"2 ning {a} darajasi {2**a}") 

#----------------------------------------------------------------------

#while-7
n = int(input())
x = 0
while n > x:
    x+=1
    if n < x**2:
        print(x)
        break

#----------------------------------------------------------------------

#while-8
n = int(input())
x = 0
while n > x:
    x+=1
    if n < x**2:
        print(x-1)
        break        

#----------------------------------------------------------------------

#while-9
n=int(input())
s = 1
while True:
    s*=3
    if s > n:
        print(s)
        break

#----------------------------------------------------------------------

#while-10
n=int(input())
s = 1
while True:
    s*=3
    if s >= n:
        print(s//3)
        break

#----------------------------------------------------------------------

#while-11
n = int(input())
k = 1
f = 1
while True :
    k +=1
    f += k
    if f >= n:
        break
print(f,k)

#----------------------------------------------------------------------

#while-12
n = int(input())
k = 1
f = 1
while True :
    k +=1
    f += k
    if f >= n:
        f -= k
        k -=1
        break
print(f,k)

#----------------------------------------------------------------------

#while-13
n = int(input())
k = 1
s =0
while True :
    s +=1
    k += 1/s
    if k >= n :
        break
print(k , s)

#----------------------------------------------------------------------

#while-14
n = int(input())
k = 1
s =0
while True :
    s +=1
    k += 1/s
    if k >= n :
        k -=1/s
        s -=1
        break
print(k , s)

#----------------------------------------------------------------------

#while-15
s = int(input("Bankka qo'yadiga summa :"))
x =s+s
p = int(input("Bank foizi: "))
oy = 0
while s < x :
    oy += 1
    s +=(s/100)*p
print(oy,int(s))

#----------------------------------------------------------------------

#while-16
a = 10
p = int(input("foiz: "))
kun = 0
while a < 200:
    kun +=1
    a +=(a/100)*p
print(kun,a)

#----------------------------------------------------------------------

#while-17
x=0
n,m = map(int,input().split())
while n>=m:
    n-=m
    x+=1
print(f"{x} {n}-qoldiq")

#----------------------------------------------------------------------

#while-18
n = int(input())
while n:
    n-=1
    print(n)

#----------------------------------------------------------------------

#while-19
n = int(input())
x=0
y = 0
while n > x:
    x+=1
    y+=x
print(y,x)

#----------------------------------------------------------------------

#while-20    
n = input()
while True:
    if '2' in n:
        print("yes")
        break
    else:
        print('no')
        break


#----------------------------------------------------------------------

#while-21
n = int(input())
v =0
while v<n:
    v +=1
    if v%2!=0:
        print(v)


#---------------------------------------------------------------------- 

#while-23
x =0
a,b = map(int,input().split())
while True:
    x+=1
    if x %a ==0 and x %b ==0:
        print(x)
        break

#----------------------------------------------------------------------

#while-24
a = int(input())
x = 1
y = 1
while x <=a or y <= a :
    x += y
    y +=x
    if a == x or a == y:
        print("this fib number")
        break
else:
    print("this not fib number")

#----------------------------------------------------------------------

#while-25
n = int(input())
x=1
y=1
while True:
    x+=y
    y+=x
    if x > n:
        print(x)
        break
    elif y > n:
        print(y)
        break

#----------------------------------------------------------------------

#while-26
n = int(input())
x=1
y=1
while True:
    x+=y
    if x > n :
        print(y,x)
        break
    y+=x
    if y > n :
        print(x,y)
        break

#----------------------------------------------------------------------

#while-27
n = int(input())
x=1
y=1
d =0
while True:
    if x < n:
        x+=y
        d +=1
        if x > n:
            break
    if y < n:
        y+=x
        d +=1
        if y > n:
            break
print(d)

#----------------------------------------------------------------------

#while-30
a,b,c = map(int,input().split())
f=0
ab = a*b
while ab:
    ab-=c
    f+=1
print(f)
