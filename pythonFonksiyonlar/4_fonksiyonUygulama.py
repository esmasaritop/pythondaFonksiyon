#1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın

def yazdir(kelime,adet):
    print(kelime*adet)

yazdir('Merhaba \n',10)

#2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye ceviren fonk yazın

def listeyeCevir(*params):

    list= []
    for param in params:
        list.append(param)

    return list

result= listeyeCevir(10,20,30,'merhaba')

print(result)

#3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun

def asalSayilariBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi > 1:
            for i in range(2,sayi):
                if (sayi % i ==0):
                    break
                else:
                    print(sayi)

sayi1=int(input('sayı 1: '))
sayi2=int(input('sayı 2: '))

asalSayilariBul(sayi1,sayi2)
