#fonksiyon oluşturmak icin gerekli anaktar kelime def daha sonra fonksiyon adı ():
def sayHello(name='user'): # name parametresi girilmezse user yazsın demek
  print('Hello '+ name)

sayHello('ESMA') # fonksiyon adını direk yazıp çağırıyoruz
sayHello() #parametre gondermessek name yerine 'user' kelimesi gecmis olur
sayHello('Emre')



def total(num1,num2):
    return num1+num2  # return girdiğimiz için bunu bir değişkene atayıp öyle yazdırmamız gerekiyor

result= total(3,4)
print(result)


def yasHesapla(dogumYili):
    return 2024-dogumYili

ageEsma=yasHesapla(2004)
ageEmre=yasHesapla(2013)
ageHasan=yasHesapla(1972)

print(ageHasan,ageEmre,ageEsma)


def emekliligeKacYilKaldi(dogumYili,isim):
    '''
    DOCSTRİNG: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum Yili
    OUTPUT: Hesaplanan yil bilgisi
    '''
    yas=yasHesapla(dogumYili)
    emeklilik=65-yas

    if emeklilik > 0 :
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emeklisiniz')


emekliligeKacYilKaldi(2004,'Esma')


