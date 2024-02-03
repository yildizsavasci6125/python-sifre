import random
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input ("Parolanın uzunluğunu giriniz."))
yeni_sifre= "5
"
for i in range(uzunluk):
    yeni_sifre+=random.choice(karakter)
print("Sizin için uygun şifre" , *yeni_sifre)    
    
