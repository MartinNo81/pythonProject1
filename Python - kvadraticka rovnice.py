print("vypocet kvadraticke rovnice")
a = float(input("zadej cislo a:"))
b = float(input("zadej cislo b:"))
c = float(input("zadej cislo c:"))
d=b**2 - 4*a*c
if d==0:
   vystup1 = (-b/2*a)
   print("rovnice ma jedno reseni!\nkoren rovnice:{0}".format(vystup1))
elif d>0:
    vystup1=(-b+d**1/2)/2*a
    vystup2=(-b-d**1/2)/2*a
    print("rovnice na 2 reseni!\nkoreny rovnice:{0},{1}".format(vystup1, vystup2))
else:
   print("rovnice nema reseni!")