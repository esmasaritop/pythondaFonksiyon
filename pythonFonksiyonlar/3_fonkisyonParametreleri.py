def changeName(n):
    n= 'ada'

name= 'Esma'

changeName(name)
print(name)

def change(n):
    n[0]= 'İstanbul'

sehirler= ['Elazıg', 'Malatya']

change(sehirler)
print(sehirler)


def add(a,b,c=0):  #hem 2 hem 3 parametreli bir fonksiyon oldu 
    return sum((a,b,c))
print(add(10,20))
print(add(10,3,2))

def add(*params):  #params sınırı olmayan parametre sayılı bir metotdur
    return sum((params))

print(add(10,20,30,40))

def displayUser(**args): # iki yıldız kullanmalıyız
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name = 'Esma', age = 2, city='İstanbul')
displayUser(name= 'Esma', age = 2, city='İstanbul', phone ='123456')
displayUser(name= 'Esma', age = 2, city='İstanbul',phone ='456789')

#ÖZETLE

def myfunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myfunc(10,'merhaba',30,40,'hello',60,key1='esma',key2='srtp',key3='hello',)

# bu fonksiyonda a b ve c değerleri sabit degerlerdir a b ve c tanımladıgımız icin ilk 3 değer ona gider
#sonra kw'a kadar olan degerler listeye gider, daha sonraki kelimeler kw a gider


