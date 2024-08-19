import random
logo = '''
$$$$$$$$\  $$$$$$\   $$$$$$\                         
\__$$  __|$$  __$$\ $$  __$$\                        
   $$ |   $$ /  $$ |$$ /  \__|                       
   $$ |   $$$$$$$$ |\$$$$$$\                         
   $$ |   $$  __$$ | \____$$\                        
   $$ |   $$ |  $$ |$$\   $$ |                       
   $$ |   $$ |  $$ |\$$$$$$  |                       
   \__|   \__|  \__| \______/                        
                                                     
                                                     
                                                     
$$\   $$\  $$$$$$\   $$$$$$\  $$$$$$\ $$$$$$$$\      
$$ | $$  |$$  __$$\ $$  __$$\ \_$$  _|\__$$  __|     
$$ |$$  / $$ /  $$ |$$ /  \__|  $$ |     $$ |        
$$$$$  /  $$$$$$$$ |$$ |$$$$\   $$ |     $$ |        
$$  $$<   $$  __$$ |$$ |\_$$ |  $$ |     $$ |        
$$ |\$$\  $$ |  $$ |$$ |  $$ |  $$ |     $$ |        
$$ | \$$\ $$ |  $$ |\$$$$$$  |$$$$$$\    $$ |        
\__|  \__|\__|  \__| \______/ \______|   \__|        
                                                     
                                                     
                                                     
$$\      $$\  $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$\  
$$$\    $$$ |$$  __$$\ $$ | $$  |$$  __$$\ $$  __$$\ 
$$$$\  $$$$ |$$ /  $$ |$$ |$$  / $$ /  $$ |$$ /  \__|
$$\$$\$$ $$ |$$$$$$$$ |$$$$$  /  $$$$$$$$ |\$$$$$$\  
$$ \$$$  $$ |$$  __$$ |$$  $$<   $$  __$$ | \____$$\ 
$$ |\$  /$$ |$$ |  $$ |$$ |\$$\  $$ |  $$ |$$\   $$ |
$$ | \_/ $$ |$$ |  $$ |$$ | \$$\ $$ |  $$ |\$$$$$$  |
\__|     \__|\__|  \__|\__|  \__|\__|  \__| \______/ 
'''
print(logo)
def tas_kagit_makas_ADINIZ_SOYADINIZ():

    
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print(" ")
    print("Kurallar: Taş makası yener, makas kağıdı yener, kağıt ise taşı yener. Kullanıcı ve bilgisayarın cevabı aynı olursa beraberlik gerçekleşir!")
    print(" ")
    print("İlk iki turu kazanan oyunun galibi olur.")
    print(" ")
    print("Oyundan çıkmak için 'q' tuşuna basabilirsiniz.")
    print(" ")
    
    tas = '''  
        _______
    ---'   ____)  
          (_____)  
          (_____)  
          (____)
    ---.__(___)  
    '''
    
    kagit = '''  
        _______
    ---'   ____)____  
              ______)  
              _______)  
             _______)
    ---.__________)  
    '''
    
    makas = '''  
        _______
    ---'   ____)____  
              ______)  
           __________)  
          (____)
    ---.__(___)  
    '''
    
    while True:
        secenekler = ["taş", "kağıt", "makas"]
        ascii_sanat = {"taş": tas, "kağıt": kagit, "makas": makas}
        oyuncu_galibiyet = 0
        bilgisayar_galibiyet = 0
        tur_sayisi = 0

        while oyuncu_galibiyet < 2 and bilgisayar_galibiyet < 2:
            oyuncu_secimi = input("Taş, kağıt, makas seçeneklerinden birini seçin: ").lower()
            
            if oyuncu_secimi == 'q':
                print("Oyundan çıkılıyor...")
                return
            
            if oyuncu_secimi not in secenekler:
                print("Geçersiz bir seçenek girdiniz, lütfen tekrar deneyin.")
                continue
            
            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
            print(f"Oyuncunun seçimi:\n{ascii_sanat[oyuncu_secimi]}")
            print(f"Bilgisayarın seçimi:\n{ascii_sanat[bilgisayar_secimi]}")

            if oyuncu_secimi == bilgisayar_secimi:
                print(f"Berabere! ({oyuncu_secimi} - {bilgisayar_secimi})")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                oyuncu_galibiyet += 1
                print(f"Tur galibi: Oyuncu")
                print(f"Oyuncu skoru-{oyuncu_galibiyet} || Bilgisayar Skoru-{bilgisayar_galibiyet}")
            else:
                bilgisayar_galibiyet += 1
                print(f"Tur galibi: Bilgisayar")
                print(f"Oyuncu skoru-{oyuncu_galibiyet} || Bilgisayar Skoru-{bilgisayar_galibiyet}")            
            tur_sayisi += 1

        if oyuncu_galibiyet == 2:
            print(f"Oyunu oyuncu kazandı! Toplam oynanan tur: {tur_sayisi}")
        else:
            print(f"Oyunu bilgisayar kazandı! Toplam oynanan tur: {tur_sayisi}")

        tekrar_oyna = input("Başka bir oyun oynamak ister misiniz? (Evet için 'e', Hayır için 'h'): ").lower()


        if tekrar_oyna != 'e':
            print("Oyun sona erdi. Teşekkürler!")
            break

tas_kagit_makas_ADINIZ_SOYADINIZ()
