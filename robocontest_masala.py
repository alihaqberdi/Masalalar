"masala 1"
print(sum(map(int,input().split())))


"masala-2"
a, b = map(int,input().split())
if a > b:
    x=">"
if a < b:
    x="<"
if a==b:
    x="="
print(x)


"masala -3"
print(int(input())+int(input()))


"masala -4"
n,k=map(int,input().split())
print(n*k)


"masala-6"
n = int(input())
x = ""
if n < 10 :
    x+="000"
elif n < 100 :
    x += "00"
elif n < 1000:
    x +="0"
if n % 400 == 0 or n % 4 == 0 and n % 100 != 0:
    n = f"12/09/{x+str(n)}"
else:
    n = f"13/09/{x+str(n)}"
print(n)


"masala-7"
n = int(input())
k,f =1,0
for z in range(n):
    k,f =k+f,k
print(f*2)


"masala-8"
n =list( map(int,input().split()))
print(sum(n)-max(n),sum(n)-min(n))


"masala-9"
a = list(map(int,input().split()))
for x in a :
    if a.count(x) == 1:
        print(x)


"masala-10"
x='Yes'    
s = int(input())
n =sum(map(int,input().split()))
if n<=s:
    x='No'
print(x)


"masala-11"
x = int(input())
n =list( map(int,input().split()))
n.remove(max(n))
print(max(n))


"masala-13"
n,k = map(int,input().split())
if n > 0 :
    k += 1
else:
    k = 1
print(k)


"masala-14"
mod =1000000007
def binpow(a,b,mod):
     ans= 0
     if (a <= 0):
         return 1
     if (a%2==0):
         ans = binpow(a/2,b,mod)
         return (ans*ans)%mod
     elif(a % 2 == 1):
         return binpow(a-1,b, mod)*b%mod
a , b = map(int, input().split())
print(int(binpow((a),(b+1),mod)))


"masala -19"
n,k=map(int,input().split())
print(k//n)


"masala-20"
n,k=map(int,input().split())
print(k%n)


"masala-21"
a,b,c=map(int,input().split())
print((a//2+a%2)+(b//2+b%2)+(c//2+c%2))


"masala-22"
print(int(input())//10)


"masala-23"
print(int(input())%10)


"masala-24"
h,m,s=map(int,input().split())
h1,m1,s1=map(int,input().split())
print(((h1*3600)+(m1*60)+s1)-((h*3600)+(m*60)+s))


"masala-25"
s=int(input())
print(f"{(s//3600)%24}:{((s%3600)//600)}{((s%3600)//60)%10}:{((s%3600)%60)//10}{((s%3600)%60)%10}")


"masala-28"
n = int(input())
for x in range(n):
    a,a2,b,b2 = map(int,input().split())
    print(b+b-a,b2+b2-a2)
    
    
"masala-39"   
n = int(input())
s = ""
for x in range(10,n+1):
    if x < 100:
        if n == x + int(str(x)[:]):
            s += str(x)+" "
    else:
        if n == x + int(str(x)[1:]):
            s+=str(x)+" "
print(s)


"masala-43"
n,k=map(int,input().split())
print(k,n)


"masala-44"
n = int(input())
if n % 400 == 0 or n % 4 == 0 and n % 100 != 0:
 	n = "Kabisa yili"
else:
   	n = "Kabisa yili emas"
print(n)


"masala-45"
a =int(input())
s=a*(a+1)//2
print(int(s))


"masala-47"
n=int(input())
for i in range(n):  
    print(bin(int(input())).count("1"))


"masala-48"
n = int(input())
s = 0
for x in range(1,n+1):
    for y in range(x):
        s += 1
        print(s,end=" ")
    print()


"masala-53"
a=int(input())
s=a*(a-3)//2
if a>3:
  print(s)
else:
  print("0")
  
  
"masala-54"  
print("Hasan"if int(input())%2else"Husan")


"masala-55"
n = int(input())
for i in range(n):
  d = int(input())
  print((d**3)+d)


"masala-58"
print(7-int(input()))

"masala -59"
print(int(input())**2)


"masala -61"
n=int(input())
a=1
if n>=1:
    s=round((2*a+(n-1)*4)*n//2)
print(s)


"masala -62"
n=int(input())
print((n*n+n+2)//2)


"masala -65"
a,b = map(int,input().split())
a = str(a)
b = str(b)
Multiplication = int(a, 2) * int(b, 2) 
print(Multiplication)


"masala -68"
m = input()  
n = list((map(int,input().split())))
ind = int(input())
n.sort()
print(n[ind-1])


"robo-71"
n = int(input())+1
a =n//2
print((n%2)+a) 


"masala -76"
a=sum(map(int,input().split()))
b = int(input())
if a<b:
    x=b-a
else:
    x=0
print(x)


"masala-82"
n = int(input())
if n % 2 ==0:
    n ="Second player"
else:
    n ="First player"
print(n)


"masala -93"
n=int(input())
for i in range(n):
  s=input()
  d=set(s)
  print(len(s)-len(d))


"masala -113"
n = int(input())
if n < 38:
    s = n
else:
    if n % 5 > 2 :
        s = ((n//5)*5) +5
    else:
        s = n
print(s)


"masala -119"
n = int(input())
if n % 4 != 0:
    n = -1
else:
    n = n // 2
print(n)


"masala -138"
x=int(input())
b=x**5+8*(x**4)-5*(x**3)+3*(x**2)+x-12
print(b)


"masala -139"
a=input()
x=input()
y=0
d=0
s=0
ch=0
p=0
j=0
for i in x:
    if i!=" ":
        i=int(i)
        if i==1:
            y+=1
        elif i==2:
            d+=1
        elif i==3:
            s+=1
        elif i==4:
            ch+=1
        else:
            p+=1
if y>=d and y>=s and y>=ch and y>=p:
    j=1
elif d>=y and d>=s and d>=ch and d>=p:
    j=2
elif s>=y and s>=d and s>=ch and s>=p:
    j=3
elif ch>=y and ch>=d and ch>=s and ch>=p:
    j=4
elif p>=y and p>=d and p>=s and p>=ch:
    j=5
print(j)


"masala-201"
n = int(input())
s = 0
if n % 2 == 0 :
    n = (n//2)+1
else:
    n =(n%2)+(n//2)
print(n)


"masala-203"
n =int(input())
print(2*n*(n+1)-1)


"masala-215"
n=int(input())
if n % 4 == 0 or n%4==3:
    s="B"
else:
    s="A"
print(s)


"masala-216"
n = int(input())
s = n // 10
i = n % 10
if i > 6:
    i = 2
elif i > 2:
    i = 1
else:
    i = 0
print((s*2)+i)


"masala-226"
n = int(input())
y = {}
for f in range(n):
    a = input().split()
    if a[0] in y.keys():
        y[a[0]] = y[a[0]] + int(a[-1])
    else:
        y[a[0]]=int(a[-1])
m = int(input())
for g in range(m):
    s = input()
    print(s,y[s])


"masala-229"
a,b = map(int,input().split())
ar = (a+b)/2.0
ge = pow(a*b,0.5)
if ar == ge:
    i = "="
elif ar > ge:
    i = ">"
else:
    i = "<"
print(i)


"masala-236"
a =int(input())
s = 0
if a < 0:
    for x in range(a,1):
        s+=x
    print(s+1)
else:
    for x in range(1,+a+1):
        s+=x
    print(s)


"masala-237"
n = int(input())
m = input().split()
sef = set(m)
print(sum([m.count(a) // 2 for a in sef if m.count(a)]))


"masala-238"
n=int(input())
a=list(map(int,input().split()))
k=0
s=0
q=0
while q<n-1:
  for j in range(q,n):
    if a[q]==a[j]:
      k+=1
      q=j
  q+=1
  if k>s:
    s=k
  k=0
print(s)


"masala-240"
n=int(input())
for i in range(n):
    a=int(input())
    a=(a//2)+1 if a%2 else a//2
    print(a)


"masala-250"
n=input()
s={'a': 1,'d': 1,'g': 1,'j': 1,'m': 1,'p': 1,'t': 1,'w': 1,'b': 2,'e': 2,'h': 2,'k': 2,'n': 2,'q': 2,'u': 2,'x': 2,'c': 3,'f': 3,'i': 3,'l': 3,'o': 3,'r': 3,'v': 3,'y': 3,'s': 4,'z': 4}
d=0
for i in n:
   if i == " ":
       d+=1
   else:    
       d+=s[i]   
print(d)


"masala-257"
print('NO'if'0'in input().strip('0')else'YES')


"masala-265"
a = list(map(int,input().split()))
print(a[0]*a[-1])


"masala-274"
n, k= map(int, input().split())
pul = list(map(int,input().split()))
supl = int(input()) 
del pul[k]
print(supl - (sum(pul)// 2))


"masala-293"
a = input()
print(len(a))
for i in a:
    print(bin(ord(i))[2:])
    

"robo-301"    
a = input()
b = list(map(int,input().split()))
a = b.copy()
b.sort()
if a == b:
    s="YES"
else:
    s="NO"
print(s)


"robo-302"
v = list(input())
h = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for z in h:
    print(z,v.count(z))
for y in h:
    print(y.upper(),v.count(y.upper()))


"masala-309"
n = int(input())
s =0
while n>1:
    s +=1
    n = n / 2
print(s)


" masala-367"
print(sum(map(int," ".join(input()).split())))


" masala-370"
num = int(input())
res = 0
table = [(1000, "M"),(900, "CM"),(500, "D"), (400, "CD"),(100, "C"),(90, "XC"),(50, "L"),(40, "XL"),(10, "X"),(9, "IX"),(5, "V"), (4, "IV"),(1, "I"),]
for cap, roman in table:
    d, m = num// cap, num%cap 
    res += roman * d
    num = m
print(res)   


"masala-372"
print(max(map(int,input().split())))


"masala-373"
n =input()
if len(n) == 6:
    if sum((lambda x :[ int(f) for f in x ])(n[:3])) == sum((lambda x :[ int(f) for f in x ])(n[3:])):
        v = "YES"
    else:
        v = "NO"
else:
    v = "NO"
print(v)


"masala-374"
a = list(map(int,input().split()))
print(max(a)-min(a))


"masala-375"
b = input()
n = list(map(int,input().split()))
x = n.copy()
for a in x:
    if a % 2 == 1:
        n.remove(a)
if n:
    s = max(n)
else:
    s = -1
print(s)


"masala-376"
n = int(input())
if n > 2 and n <= 5 :
    n = "Spring"
elif n > 5 and n <= 8:
    n ="Summer"
elif n > 8 and n <= 11 :
    n = "Autumn"
elif n > 11 and n <= 12 or n == 1 or n ==2:
    n ="Winter"
else:
    n = "Error"
print(n)


"masala-384"
n = int(input())
sat = n//100 
bist = (n%100)//20 
da = (n%20)//10 
pa = (n%10)//5
yak = (n%5)
print(sat+bist+da+pa+yak)


"masala-392"
n=int(input())
a=[int(i) for i in input().split()]
for i in a:
    print(i//2)
   
    
"masala-425"
input()
input()
print(1)


"masala-448"
a, b, c, x=map(int,input().split())
if (a*(x**2))+ (b*x) + c == 0:
    s="YES"
else:
    s="NO"
print(s)


"masala-467"
n,m = map(int,input().split())
print(-1 if m%2 else n+(m//2)+1)


"masala-474"   
print("Ali"if int(input())%2else"G'ani")


"masala-479"
a = str(int(input())/ (10000/100))
print(a.split(".")[0] if a.endswith(".0") else a)


"masala-483"
n, m= map(int, input().split())
s = 1
f = []
d = 1
for i in range(n):
    i = set(input().split())
    if i in f:
        d = 0
    f.append(i)
    if len(i) != 1:s = 0
print("YES" if s and d and len(f) < 10 else "NO")


"masala-492"
input()
print(1)


"masala-493"
f = int(input())
for x in range(f):
    m,a,k= list(map(int,input().split()))
    m = m - k
    a = a - k
    if m >= 0 and a >= 0:
        if a < m:
            s = "Azimjon"
        elif m < a:
            s = "Maqsud"
        else:
            s = "Draw!"
    elif m < 0 and a < 0:
        s = "Draw!"
    else:
        if m > a:
            s = "Maqsud"
        else:
            s = "Azimjon"
    print(s)
    
    
"masala-498"
print(0)


"masala-511"
a=input()
if int(a)>0:
	print(a)
else:
    if int(a) < -9:
        print(int(a[0:2])+int(a[2:]))
    else:
        print(a)


"masala-516"
a=list(map(int,input().split()))
a=(a[0]+a[1])-a[-1] if (a[0]+a[1])-a[-1] >=0 else 'Error'
print(a)


"masala-520"
print(1)


"masala-524"
x=int(input())
for i in range(x):
  input()
print(x)


"masala-530"
r = int(input())
rx = r ** 2
ry = r * r
if rx == ry:
    s = "=" 
elif rx > ry :
    s = ">"
else:
    s = "<"
print(s)


"masala-567"
a = input().split()
s = 0
if len(a) > 1:
    for x in a:
        s+=int(x)
else:   
    s = int(input()) * int(a[-1])
print(s)


"masala-573"
x,u=map(int,input().split())
print((24 -x)+u)


"masala-604"
print(ord(input()))


"masala-606"
j = 0
n = input()
d = len(n)-1
for x in n:
    x = int(x)
    j+=x*2**d     
    d-=1
print(j)


"masala-611"
print(2+int(input()))


"masala-613"
a = input()
b = sorted(list(map(int,input().split())))
s = ""
for i in b[-1:-4:-1]:
    s+=str(i)+" "
print(s)


"masala -707"
print(input())


"masala -789"
print(0if int(input())<5else 1)


"masala-794"
a,b =map(int,input().split())
v = (10000*a)/(b**2)
if v < 16:
    x ="Yuqori vazn yetishmasligi"
if 16 <= v < 18.5 :
    x ="Vazn yetishmasligi"
if 18.5 <= v <= 25 :
    x ="Ideal vazn"
if 25 < v <= 30 :
    x ="Ortiqcha vazn"
if 30 < v <= 35:
    x ="Semizlikning I darajasi"
if 35 < v <= 40 :
    x ="Semizlikning II darajasi"
if 40<v :
    x="Semizlikning III darajasi"
print(x)
 
   
"masala-805"
n = input()
a = eval(n.split("=")[0])
if n.endswith(str(int(a))):
    print(True)
else:
    print(False,int(a))


"masala-812"
print(int(input()[-1])%2)


"masala-813"
n = int(input())
d = 0
if n == 1000000000:
    d += 10
    n-=1
if n > 99999999:
    d += (n - 99999999) * 9
    n = 99999999  
if n > 9999999:
    d += (n - 9999999) * 8
    n = 9999999
if n > 999999:
    d += (n - 999999) * 7
    n = 999999
if n > 99999:
    d += (n - 99999) * 6
    n = 99999
if n > 9999:
    d += (n - 9999) * 5
    n = 9999
if n > 999:
    d += (n - 999) * 4
    n = 999
if n > 99:
    d += (n - 99) * 3
    n = 99
if n > 9:
    d += (n - 9) * 2
    n = 9     
for i in range(1,n+1):
    d += 1
print(d)


"masala-815"
print(45)


"masala-825"
s = input()
h =""
a = {"й":"q", "ц" : "w", "у":"e" , "к":"r", "е":"t", "н":"y","г":"u", "ш":"i", "щ":"o", "з":"p", "ф":"a", "ы":"s", "в":"d", "а":"f", "п":"g", "р":"h", "о":"j", "л":"k", "д":"l","я":"z", "ч":"x", "с":"c", "м" :"v", "и":"b",  "т":"n",  "ь":"m"," " : " " , "э" : "'" }
for d in s:
    if d.isupper():
        d=d.lower()
        h+=str((a[d])).upper()
    else:
        h+=a[d]
print(h)


"masala-860"
n = list(map(int,input().split()))
print((n[-1]-n[0])+1)


"masala-874"
n = input()
s = ""
ll = ""
for i in n:
    ll += i
    if int(ll) >= 65 and int(ll) <= 90:
        s += chr(int(ll))
        ll = ""
    elif int(ll) >= 97 and int(ll) <= 122:
        s += chr(int(ll))
        ll = ""   
print(s)
