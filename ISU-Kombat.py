import sys #Yavaş yazdırma fonksiyonunda kullandığım modüllerin kütüphanesi.
import random #Random kütüphanesi.
import time #Zamanlayıcı kütüphanesi.

#İlk olarak, fonksiyonların tanıması için global olarak değişkenleri tanımlıyoruz.
oyuncu1=""
oyuncu2=""
can1=100
can2=100

#"İSTİNYE KOMBAT V1.0 HOŞGELDİNİZ" yazısını ekrana basıyoruz.
def istinye_kombat():           
    print("\n-------------------------------------------------------------------------------------------------------------------------")
    print("                      ___ ___ _____ ___ _  ___   _____   _  _____  __  __ ___   _ _____       _   __  ")
    print("                     |_ _/ __|_   _|_ _| \| \ \ / / __| | |/ / _ \|  \/  | _ ) /_\_   _| __ _/ | /  \ ")
    print("                      | |\__ \ | |  | || .` |\ V /| _|  | ' < (_) | |\/| | _ \/ _ \| |   \ V / || () |")
    print("  (@/**/#&(.         |___|___/ |_| |___|_|\_| |_| |___| |_|\_\___/|_|  |_|___/_/ \_\_|    \_/|_(_)__/         (@/**/#&(.              ")
    print(" #%. &&/& ,&(                                                                                                #%. &&/& ,&(            ")
    print(".%/  ,/ ( ,@/                   _  _  ___  ___  ___ ___ _    ___ ___ _  _ ___ ____                          .%/  ,/ ( ,@/            ")
    print("  ,*#@%%#/*                    | || |/ _ \/ __|/ __| __| |  |   \_ _| \| |_ _|_  /                            ,*#@%%#/*              ")
    print("   ,%@@#*.*                    | __ | (_) \__ \ (_ | _|| |__| |) | || .` || | / /                              ,%@@#*.*              ")
    print("                               |_||_|\___/|___/\___|___|____|___/___|_|\_|___/___|    ")
    print("\n--------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)

#https://gist.github.com/gnuton/3c7a46447d2be0aee0b2#file-slowprint-py-L4
#Yavaş yazdırma kod parçasını bu linkten aldım.
#Bir string'de ki bütün harfleri tek tek yazdırıyoruz.
def yavas_yazi1(alinan_yazi):
    for i in alinan_yazi + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1./20)
def yavas_yazi2(alinan_yazi,a,b):
    for i in alinan_yazi + a +b:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1./20)
def yavas_yazi3(alinan_yazi):
    for i in alinan_yazi:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(2./10)
def yavas_yazi4(alinan_yazi):
    for i in alinan_yazi +"\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1/70)

#Burada, kullanıcılardan isimleri alıyoruz.
def isimler(oyuncu1,oyuncu2):
    kontrol1=True
    while(kontrol1):
        print("\n")
        yavas_yazi1(" --------- İlk Kahraman ---------")
        yavas_yazi2("Lütfen kahramanınızın adını yazınız : ","","") 
        oyuncu1=input()
        #Aldığımız input değerinin ilk önce her harfini küçültüyoruz, daha sonra baş harfini büyültüyoruz ve yanlarındaki boşlukları siliyoruz.
        oyuncu1=oyuncu1.lower()
        oyuncu1=oyuncu1.capitalize()
        oyuncu1=oyuncu1.strip()
        #Doğru kullanıcı girdisi kontrol ediliyor.
        if oyuncu1.isnumeric()==True or oyuncu1=="":
            print("\n---------------------------------")
            yavas_yazi2("Lütfen isminizi doğru giriniz !","","")
            print("\n---------------------------------\n")
            kontrol1=True
        else:
            print("\n----------------------------------------------")
            yavas_yazi2("İlk Kahraman Seçildi ! Merhaba, ",oyuncu1," !")
            print("\n----------------------------------------------\n")
            time.sleep(1)
            kontrol1=False
    kontrol=True
    while(kontrol):
        yavas_yazi1("  ------- İkinci Kahraman -------")
        yavas_yazi2("Lütfen kahramanınızın adını yazınız : ","","") 
        oyuncu2=input()
        #Aldığımız input değerinin ilk önce her harfini küçültüyoruz, daha sonra baş harfini büyültüyoruz ve yanlarındaki boşlukları siliyoruz.
        oyuncu2=oyuncu2.lower()
        oyuncu2=oyuncu2.capitalize()
        oyuncu2=oyuncu2.strip()
        #Doğru kullanıcı girdisi kontrol ediliyor.
        if oyuncu2.isnumeric()==True or oyuncu2=="":
            print("\n---------------------------------")
            yavas_yazi2("Lütfen isminizi doğru giriniz !","","")
            print("\n---------------------------------\n") 
        else:
            #Oyuncu1 ile oyuncu2'nin aynı karakter olup olmadığı kontrol ediliyor.
            if oyuncu1==oyuncu2:
                print("\n--------------------------------------------------")
                yavas_yazi2(oyuncu1," karakteri alındı, lütfen tekrar deneyiniz.","")
                print("\n--------------------------------------------------\n")
                kontrol=True
            else:
                print("\n----------------------------------------------")
                yavas_yazi2("İkinci Kahraman Seçildi ! Merhaba, ",oyuncu2," !")
                print("\n----------------------------------------------\n")
                time.sleep(2)
                kontrol=False  
    return oyuncu1,oyuncu2

#Aldığımız oyuncular arasında yazı tura atıyoruz.
def yazı_tura(oyuncu1,oyuncu2):
    def yazi_tura_resim():
        print("\n")
        print("                      ▓▓▓▓▓▓▓▓▓▓     ") 
        print("                   ▓▓            ▓▓   ")  
        print("                ▓▓       ▓▓         ▓▓ ") 
        print("                ▓▓       ▓▓  ▓▓     ▓▓")
        print("                ▓▓       ▓▓▓▓       ▓▓")
        print("                ▓▓     ▓▓▓▓         ▓▓")
        print("                ▓▓   ▓▓  ▓▓    ▓    ▓▓")
        print("                ▓▓       ▓▓   ▓▓    ▓▓")
        print("                  ▓▓     ▓▓▓▓▓    ▓▓  ")
        print("                    ▓▓          ▓▓ ")   
        print("                      ▓▓▓▓▓▓▓▓▓▓")
        print("   __   ___    _______          _____ _   _ ___    _   ")
        print("   \ \ / /_\  |_  /_ _|  ____  |_   _| | | | _ \  /_\  ")
        print("    \ V / _ \  / / | |  |____|   | | | |_| |   / / _ \ ")
        print("     |_/_/ \_\/___|___|          |_|  \___/|_|_\/_/ \_\ \n")
        time.sleep(3)
    yazi_tura_resim()
    #Yazı-Tura resmini çağırıyoruz.
    time.sleep(1)
    yavas_yazi3("Yazı-Tura atılıyor...\n")
    
    #Random modülünü kullanarak oyuncu listesinden rastgele bir oyuncuyu seçip onun yeni değişken ismini secilen_kisi olarak değiştiriyoruz.
    #Bundan dolayı secilen_kisi=oyuncu1 ise secilmeyen_kisi=oyuncu2 olmuş oluyor.
    liste=[oyuncu1,oyuncu2]
    secilen_kisi=random.choice(liste)
    if secilen_kisi==oyuncu1:
        secilmeyen_kisi=oyuncu2
        print("\n------------------------------")
        yavas_yazi2(secilen_kisi,", oyuna önce başlayacak !","")
        print("")
        print("------------------------------\n")
        time.sleep(2)
    elif secilen_kisi==oyuncu2:
        secilmeyen_kisi=oyuncu1
        print("\n------------------------------")
        yavas_yazi2(secilen_kisi,", oyuna önce başlayacak !","")
        print("")
        print("------------------------------\n")
        time.sleep(2)

    return secilen_kisi,secilmeyen_kisi

#Oyuncuların canlarını ve canlarını temsil eden çizgileri ekrana yazdırıyoruz.
def canlar_ve_sopalar (secilen_kisi,secilmeyen_kisi,can1,can2):
    #İsimler arası boşluğu, seçilen kişinin str uzunluğuna göre bir sayıdan çıkartıp bunu boşlukla çarpıyoruz.
    #Bunu yapmamızın nedeni, bir kullanıcı örneğin berkay caglar girerse uzunluğuna göre aradaki boşluk mesafesini ölçüyoruz.
    isim_arasi_bosluk = (75 - len(secilen_kisi)) * " "
    
    sopalar1="█"*(can1//2)
    sopalar2="█"*(can2//2)

    #Uzun uğraşlar sonucunda (yaklaşık 1 hafta), bu formülü bulduk. Yukarıda verdiğimiz sopalar değişkeninin uzunluğuna göre aradaki boşluğu sürekli esşit tutuyoruz.
    #Eğer can 3 haneli ise else kısmına giriyor, eğer 2 haneli ise if, 1 haneli ise elif kısmına giriyor.     
    if 10 <= can1 <= 99:
        can1_bosluk = (67 - len(sopalar1)) * " "
    elif can1 < 10:
        can1_bosluk = (68 - len(sopalar1)) * " "
    else:
        can1_bosluk = (66 - len(sopalar1)) * " "

    #Secilen kisi ve secilmeyen kisiyi yukarıdaki formüle göre aradaki boşlukla beraber yazdırıyoruz.
    print(secilen_kisi,isim_arasi_bosluk,secilmeyen_kisi,"\n")

    #HP,Sopalar ve bosluğu burada yazdırıyoruz.
    #Format modülü ile {} içine atıyoruz.
    print("HP=[{}]:{}".format(can1,sopalar1),can1_bosluk,"HP=[{}]:{}".format(can2,sopalar2))
    return can1,can2

#Oyuncular birbirine belli bir şans yüzdesi ile saldırıyor.
def saldırı(can1,can2,secilen_kisi):
    kontrol7=True
    while(kontrol7):
        print("\n--------------------------------------------------")
        yavas_yazi2(secilen_kisi,", lütfen saldırı miktarınızı giriniz: (1-50)","")
        print("")
        print("--------------------------------------------------")
        yavas_yazi3("Miktar: ")
        saldırı=input()
        #Arasında ki boşlukları siliyoruz (strip).
        saldırı=saldırı.strip()
        #Saldırı miktarını int mi diye kontrol ediyoruz.
        if saldırı.isnumeric()==False or saldırı=="":
            print("\n---------------------------------")
            yavas_yazi2("Lütfen geçerli bir sayı giriniz !","","")
            print("\n---------------------------------")
            time.sleep(1)
            kontrol7=True
        else:
            #Eğer saldırı=int(saldırı) ise bu while'dan çıkartıyoruz.
            saldırı=int(saldırı)
            kontrol7=False
        kontrol8=True
        while(kontrol8):
            if saldırı==str(saldırı):
                if saldırı.isnumeric()==False or saldırı=="":
                    kontrol8=False
            
            elif saldırı>50 or saldırı <1:
                #1 ile 50 arasında yazılmış mı diye kontrol ediyoruz.
                print("\n-----------------------------------------------")
                yavas_yazi2("Lütfen '1' ile '50' arasında bir sayı giriniz !","","")
                print("\n-----------------------------------------------")
                time.sleep(1)
                kontrol7=True
                kontrol8=False
            else:
                kontrol7=False
                kontrol8=False
    #Burada sans değişkenimize rastgele 1 ile 100 arasında bir değişken atanıyor.
    #Bu değişken bizim şansımız oluyor. Eğer şansımız oranımızdan küçükse saldırı başarıyla gerçekleşiyor.
    #Eğer değilse başarısız oluyor.
    sans=random.randint(1,100)
    #Oran= Bizim saldırıyı kazanma yüzdemiz.
    oran=100-saldırı
    if oran>sans:
        can2=can2-saldırı
        if can2<0:
            can2=0
        print("\n-----------------")
        yavas_yazi2("Saldırı başarılı!","","")
        print("\n-----------------\n")
        time.sleep(1)
        return can2
    else:
        print("\n------------------")
        yavas_yazi2("Saldırı Başarısız!","","")
        print("\n------------------\n")
        time.sleep(1)
        return can2

#Oyuncuları yer değiştiriyoruz.
def oyuncu_degisikligi(secilen_kisi,secilmeyen_kisi,can1,can2):
    #Burada secilen kisi adlı değişkeni boş bir "temp" değişkenine atıyoruz.
    #Çünkü bu değişkenin kaybolmasını istemiyoruz.
    #Daha sonra secilen kisi ile secilmeyen kisiyi yer değiştiriyoruz.
    #"Temp" değişkenine eklediğimiz secilen kisiyi secilmeyen kisi yerine aktarıyoruz.
    temp=secilen_kisi
    secilen_kisi=secilmeyen_kisi
    secilmeyen_kisi=temp

    #Yukarıdaki işlemlerin aynısını canlar için de yapıyoruz.
    temp2=can1
    can1=can2
    can2=temp2
    return secilmeyen_kisi,secilen_kisi,can1,can2

#Burada, canların 0'dan küçük olup olmadığını kontrol ediyoruz.
def can_kontrol(can1,can2,secilen_kisi,secilmeyen_kisi):
    if can1<=0:
        print("\n")
        #Boşluklarda yaptığımız gibi oyun sonunda ki sharpları da aynı hizada ve oyuncu ismine göre eşit hizalıyoruz.
        oyun_sonu_sharp2 = (156 - len(secilmeyen_kisi)) * "#"
        yavas_yazi4(oyun_sonu_sharp2)
        oyun_sonu_sharp = (67 - len(secilmeyen_kisi)) * "#"
        #Can1 0 dan küçük olduğu durumda secilmeyen kisi kazanıyor.
        yavas_yazi4(oyun_sonu_sharp+" "+secilmeyen_kisi+" oyunu kazanmıştır ! "+oyun_sonu_sharp)
        yavas_yazi4(oyun_sonu_sharp2)
        time.sleep(2)
        return False
    elif can2<=0:
        print("\n")
        #Boşluklarda yaptığımız gibi oyun sonunda ki sharpları da aynı hizada ve oyuncu ismine göre eşit hizalıyoruz.
        oyun_sonu_sharp2 = (156 - len(secilen_kisi)) * "#"
        yavas_yazi4(oyun_sonu_sharp2)
        oyun_sonu_sharp = (67 - len(secilen_kisi)) * "#"
        #Can2 0 dan küçük olduğu durumda secilen kisi kazanıyor.
        yavas_yazi4(oyun_sonu_sharp+" "+secilen_kisi+" oyunu kazanmıştır ! "+oyun_sonu_sharp)
        yavas_yazi4(oyun_sonu_sharp2)
        time.sleep(2)
        return False
    else:
        return True

#Burada, oyunculara tekrar oynamak isteyip istemediklerini soruyoruz.
def tekrar_isteği(can1,can2):
    kontrol10=True
    while(kontrol10):
        print("\n-------------------------------")
        yavas_yazi2("Tekrar oynamak ister misiniz?","","\n")
        yavas_yazi2("     1-) EVET 2-) HAYIR","","")
        print("\n-------------------------------\n")
        yavas_yazi3("Seciminiz : ")
        secim=input()
        #Secimin ilk olarak bütün harflerini büyültüyoruz, daha sonra yanlarında ki boşlukları siliyoruz.
        secim=secim.upper()
        secim=secim.strip()
        if secim=="EVET" or secim=="1":
            #Oyunu yeniden başlatacağımız zaman canları tekrardan ilk durumuna getiriyoruz.
            can1=100
            can2=100
            print("\n")
            yavas_yazi3("Oyun yeniden başlatılıyor...\n")
            time.sleep(1)
            kontrol10=False
            return True,can1,can2
        elif secim=="HAYIR" or secim=="2":
            #Oyunu sonlandırıp kullanıcılara teşekkür ediyoruz.
            print("\n----------------------------------------")
            yavas_yazi2("Oyunumuzu oynadığınız için teşekkürler !","","")
            print("\n----------------------------------------\n")
            #Oyun aniden kapanmasın diye kullanıcıdan bir girdi alıyoruz.
            wait=input()
            kontrol10=False
            return False,can1,can2
        else:
            print("\n----------------------------------")
            yavas_yazi2("Lütfen seçiminizi doğru yapınız !!","","")
            print("\n----------------------------------")
            time.sleep(1)
            kontrol10=True

#Burada, yukarıda yazdığımız bütün fonksiyonları çağırıp onları belirli bir döngüye sokuyoruz.
def ana_fonk(oyuncu1,oyuncu2,can1,can2):
    istinye_kombat()
    #İlk olarak isimler fonksiyonunu çağırıp kullanıcılardan bilgileri alıyoruz.
    (oyuncu1,oyuncu2)=isimler(oyuncu1,oyuncu2)
    kontrol9=True
    while(kontrol9):
        #Buradaki döngü oyun bittikten sonra kullanıcılar tekrar oyuna devam etmek istediğinde döndürülen yer.
        #Yazı tura fonksiyonunu çağırıp return ettiğimiz secilen ve secilmeyen kisileri eşitliyoruz.
        (secilen_kisi,secilmeyen_kisi)=yazı_tura(oyuncu1,oyuncu2)
        #Canlar ve sopalar fonksiyonunu çağırıp retrun ettiğimiz can1 ve can2 ye eşitliyoruz.
        (can1,can2)=canlar_ve_sopalar(secilen_kisi,secilmeyen_kisi,can1,can2)
        kontrol6=True
        while(kontrol6):
            #Bu döngü ise saldırı durumunun sürekli olarak tekrar etmesini sağlıyor
            #Secilen ilk kişiden saldırı miktarını gireceği "saldırı" fonksiyonunu çağırıyoruz ve bunu can2'ye eşitliyoruz.
            (can2)=saldırı(can1,can2,secilen_kisi)
            #Daha sonra oyuncuları değiştirdiğimiz fonksiyonu çağırıp bunları yeni değerlerine atıyoruz.
            (secilmeyen_kisi,secilen_kisi,can1,can2)=oyuncu_degisikligi(secilen_kisi,secilmeyen_kisi,can1,can2)
            #Tekrardan canlar ve sopalar fonksiyonunu çağırıyoruz.
            (can1,can2)=canlar_ve_sopalar(secilen_kisi,secilmeyen_kisi,can1,can2)
            #Burada da döngü devam ettiği sürece canları kontrol ediyoruz. Eğer bir kullanıcı kaybederse buradaki döngüyü durduruyoruz.
            kontrol6=can_kontrol(can1,can2,secilen_kisi,secilmeyen_kisi)
        #Burada kontrol9 döngüsüne ne olacağını kullanıcı "Evet" veya "Hayır" diyerek seçiyor.
        #"Evet" derse tekrar başlıyor, "Hayır" derse oyunu bitiriyor.
        kontrol9,can1,can2=tekrar_isteği(can1,can2)

#Burada bütün fünksiyonları çağırdığımız ana fonksiyonumuzu çağırıyoruz.
ana_fonk(oyuncu1,oyuncu2,can1,can2)