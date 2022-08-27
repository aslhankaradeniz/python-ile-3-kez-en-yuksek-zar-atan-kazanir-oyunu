import random
from time import time
import time
puan1=0
puan2=0

print("oyuna hoş geldiniz ")
time.sleep(0.8)
oyuncu1=input("lütfen oyuncu1 kullanıcı adınızı giriniz: ")

oyuncu2=input("lütfen oyuncu2 kullanıcı adını giriniz:  ")


while(True):
 
    oyuncu1=random.randint(1,6)
    oyuncu2=random.randint(1,6)
    print("oyuncu1 zar atış sonucu: ",oyuncu1)
    print("oyuncu2 zar atış sonucu: ",oyuncu2)
    if (oyuncu1<oyuncu2):
            print("2. oyuncu + puan kazanacak")
            puan2=puan2+1
            print("oyuncu2 puan: ",puan2)
            print("oyuncu1 puan: ",puan1)
            


    elif(oyuncu1>oyuncu2):
            print("1.oyuncu + puan kazanacak")
            puan1=puan1+1
            print("oyuncu2 puan: ",puan2)
            print("oyuncu1 puan: ",puan1)
            
    else:
            print("Sonuç berabere")
            print("oyuncu2 puan: ",puan2)
            print("oyuncu1 puan: ",puan1)
            
    if((puan1==3)|(puan2==3)):
        break

if (puan1==3) :
        print("oyuncu1 oyunu kazandı")
elif(puan2==3):
        print("oyuncu2 oyunu kazandı")
else:
        print("yeniden deneyin")
       