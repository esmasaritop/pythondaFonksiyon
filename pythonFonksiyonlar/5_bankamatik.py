# Bankamatik uygulaması

EsmaHesap={
    'ad':'Esma Sarıtop',
    'hesapNo':'12345',
    'bakiye':3000,
    'ekHesap':2000
}

EmreHesap= {
    'ad':'Emre Sarıtop',
    'hesapNo':'56789',
    'bakiye':5000,
    'ekHesap':1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye']-=miktar
        print('paranızı alabilirsiniz.')
        bakiyeSorgulama(hesap)
    else:
        toplam= hesap['bakiye']+ hesap['ekHesap']

        if (toplam>= miktar):
            ekHesapKullanimi= input('ek hesap kullanılsın mi ? (e/h)')

            if ekHesapKullanimi=='e':
                ekHesapKullanilacakMiktar= miktar- hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-=ekHesapKullanilacakMiktar
                print('paranızı alabilirsiniz')
                bakiyeSorgulama(hesap)

            else:
                print(f"{hesap ['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır. " )

        else:
            print('Üzgünüz bakiye yetersiz')
            bakiyeSorgulama(hesap)


def bakiyeSorgulama(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır. ")


bakiyeSorgulama(EsmaHesap)
paraCek(EsmaHesap,4000)
paraCek(EsmaHesap,100)





