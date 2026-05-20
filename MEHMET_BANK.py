import random
import os

def ekrani_temizle():
    # Windows için 'cls', Mac ve Linux için 'clear' komutunu çalıştırır
    os.system('cls' if os.name == 'nt' else 'clear')
RENK_KIRMIZI = "\033[91m"  # Hatalar ve uyarılar için
RENK_SARI = "\033[93m"     # Bilgi alma ve inputlar için
RENK_MAVI = "\033[94m"     # Başlıklar için
RENK_TURKUAZ = "\033[96m"  # Menü seçenekleri için
RENK_SIFIRLA = "\033[0m"    # Rengi normale döndürmek için (ŞART!)
class müsteri:
 def __init__(self,ad,soyad,tc_no,sifre ,dogum_tarihi,anne_soyad,tel_no,bakiye=0,borc=0):
        self.ad=ad
        self.soyad=soyad
        self.tc_no=tc_no
        self.sifre=sifre
        self.dogum_tarihi=dogum_tarihi
        self.anne_soyad=anne_soyad
        self.tel_no=tel_no
        self.bakiye=bakiye
        self.borc=borc
        if self.bakiye<50000:
              self.eksi_limit=10000
        elif self.bakiye>=50000 and self.bakiye<=100000:
              self.eksi_limit=50000
        elif self.bakiye>100000 and self.bakiye<=500000:
              self.eksi_limit=100000
        else:
              self.eksi_limit=200000


 def Bakiye_görüntüle(self):
   print(self.ad)
   print(f"mevcut bakiyeniz{self.bakiye}tl dir")
   print(f"mevcut borcunuz:{self.borc}tl dir")

 def Para_cekme(self,miktar):
    self.miktar=miktar
    if miktar <= 0:
            print("Geçersiz miktar!")
            return
    if miktar<=self.bakiye:
            self.bakiye -= miktar
            print(f"{miktar} TL başarıyla çekildi. Kalan ana bakiye: {self.bakiye} TL")
            
        
    elif miktar <= (self.bakiye + self.eksi_limit):
            fark = miktar - self.bakiye
            print(f"\n[UYARI] Yetersiz Ana Bakiye! Bu işlem için ana bakiyenizden hariç {fark} TL eksi bakiyenizden kullanılacaktır.")
            onay = input("Eksi bakiyeden çekilmesini onaylıyor musunuz? (E/H): ")
            
            if onay.upper() == "E":
                self.borc+=fark
                self.bakiye -= miktar 
                print(f"\n{miktar} TL başarıyla çekildi!")
                print(f"Güncel Bakiyeniz: {self.bakiye} TL (Eksi bakiyedesiniz)")
            else:
                print("İşlem kullanıcı tarafından iptal edildi.")
                
    
    else:
            maks_cekebilir = self.bakiye + self.eksi_limit
            print(f"\nHata: Yetersiz bakiye ve limit! Eksi bakiye dahil çekebileceğiniz maksimum tutar: {maks_cekebilir} TL'dir.")
            
 def Para_yatirma(self,miktar):
        self.miktar=miktar
        if miktar>0:
            self.bakiye +=miktar
            print(f"{miktar} basarili bir sekilde  yatırılmıstır toplam bakiyeniz{self.bakiye}")
        else:
               print("lütfen gecerli bir yatirilicak deger giriniz ")
   
 def Senet_odemesi(self,miktar):
    
      self.miktar=miktar
      if miktar>self.bakiye:
            print("yetersiz bakiye işlem gercekleştirilemedi")
      elif miktar>self.borc:
            print(f"borcunuzdan daha fazla odeme yapamaısnız borcunuz {self.borc } tl dir ")
      else:
            self.bakiye-=miktar
            self.borc-=miktar
            print(f" borcunuzdan {miktar} senet odemesi yapıldı kalan borc{self.borc} kalan bakiye {self.bakiye} ")
 def Haciz_kaldirma_işlemi(self,miktar):
       self.miktar=miktar
       if miktar>self.bakiye:
             print(f" haciz işleminiz {miktar} tl dir ama  bakiyeniz {self.bakiye} oldugu icin odeme yapılamamıstırn")
       elif  miktar>self.borc:
             print(f"gergınden fazla odeme yapamaısnız yapmaınız gereken odeme {self.borc} tl dir odemeniz gercekelstırlemedı ")
       else:  
             self.bakiye-=miktar
             self.borc-=miktar
             print(f"odemeiz gercekelestirilii{miktar} tl kalan bakiyeniz{self.bakiye} tl dir")
 def Ödemeler(self,kurumadi,miktar):
       self.kurumadi=kurumadi
       self.miktar=miktar
       if miktar>self.bakiye:
             print(f"hesabınızdaki bakiye yeterli degildir odemniz{self.borc} tl iken bakiyeniz{self.bakiye} tl dir")
       elif miktar>self.borc:
             print(f" gercgınden fazla odeme yapamaısınız {self.borc} tl iken siz {miktar} kadar yatırmaya calsıtınız ")
       else: 
             self.bakiye-=miktar
             self.borc-=miktar
             print(f" odemeniz{self.kurumadi} kurumuna  basarili bir şekilde yapılmıstır {self.bakiye} niz kalmıstır guncel borc {self.borc} tl  dir ")

       pass
 def yurt_disina_para_transferi(self,ıban ,miktar):
     yurt_disi_komisyon_ucreti=50
     self.miktar=miktar
     self.ıban=ıban
     maliyet=miktar +yurt_disi_komisyon_ucreti
     if maliyet>self.bakiye:
           print(f"hesabinizda gerekli bakiye bulunmadıgından dolayuı işlem gerceklestirilemeiyor {maliyet} tl iken bakiye {self.bakiye} işleminizi gerceklestirebilmek icin {maliyet-self.bakiye} tl kadar daha  paranız olması gerekir")
     else: 
           self.bakiye-=maliyet
           print(f" {self.ıban} ıbanına {self.miktar} kadar para gonderılmıstır bu işlemden {yurt_disi_komisyon_ucreti} kadar komisyon kesılmıstır ve kalan bakıyenız :{self.bakiye} dir" )

 def finansal_veriler(self):
       if self.borc==0:
             print(f" borcunuz:{self.borc} kadar oldugu icin  kredi notunuz cok iyidir ")
       elif self.bakiye>self.borc:
             print(f" bakiyeniz:{self.bakiye} borcunuzdan:{self.borc} dan fazla oldugu icin kredn notunuz normal")
       else:
             print(f"borcunuz :{self.borc}  bakiyenizden :{self.bakiye} yüksek oldugu icin kredi notunuz riskilidir ")
 def kod_işlemleri(self,miktar):
      self.miktar=miktar
      if miktar>0 and self.bakiye>miktar:
       self.bakiye-=miktar
       print(f"qr kodunuz uretıldi hesabınızdan{self.miktar} kadar para cekilmistir kalan bakiyeniz {self.bakiye}")
      elif  miktar<=0:
            print("lutfen sifirdan buyuk bir bakiye giriniz")
      else:
            print(f" hesabınzda yeterli bakiye bulunamadı{self.bakiye} varken siz {self.miktar} kadar para cekmek istediniz lutfen tekrar deneyınız ")

 def hesaplama_araclari(self):
       print("----------taksitlendirme hesaplayıcı----------- ")
       if self.borc==0:
             print("mevcut bir borc olamdıgı icin hesaplma yapılamadı ")
       elif self.borc<10000:
             print(f"borcunuzu  4 ayda her  {(self.borc)/4} sekilde veya 2 ayda her ay  {(self.borc)/2}  odeyecek şsekilde taksitlendirebilirniz")
       elif self.borc>10000 and self.borc<50000:
              print(f"borcunuzu  6 ayda her  {(self.borc)/6} sekilde veya 2 ayda her ay  {(self.borc)/2}  odeyecek şsekilde taksitlendirebilirniz")
       else:
             print(f"borcunuzu  8 ayda her  {(self.borc)/8} sekilde veya 2 ayda her ay  {(self.borc)/2}  odeyecek şsekilde taksitlendirebilirniz")
 
 def diger_işlemler(self):
       print("sifre degistirme ekrani")
       eski_sifre=input("lütfen eski sifrenizi giriniz")
       if eski_sifre==self.sifre:
             yeni_sifre=input("lütfen yeni sifrenizi giriniz")
             yeni_sifre_tekrari=input("luten tekrar yeni sifreyi giriniz")
             if yeni_sifre==yeni_sifre_tekrari:
                   print("sifreniz basarili bir sekilde degistilimistir")
             else:
                   print(f" yeni sifre ve yeni sifre tekrari ayni degi yeni sife={yeni_sifre} yeni sifre tekrari ise{yeni_sifre_tekrari}")
       else:
             print("mecvut sifrenizi yanis giridniz ")




 def sifremi_unuttum(self):
       print("------sifre degistirme ekranı ")
       girilen_tc=input("tc kimlik numarasını giriniz")
       girilen_dogum=input("dogum tarihinizi giriniz( gun -ay -yıl seklınde )")
       girilen_soyad=input("annenizin kızlık soyadini giriniz")
       girilen_tel=input("telefon numarsını giriniz")
       if (girilen_tc == self.tc_no and 
            girilen_dogum == self.dogum_tarihi and 
            girilen_soyad.lower() == self.anne_soyad.lower() and 
            girilen_tel == self.tel_no):
            print("kimlik bilgileriniz dogrulandı")
            sms_kodu=random.randint(100000,999999)#! 6 haneli rastgele bir sms urettiyoruz
            print(f"lutfen {self.tel_no} numarali telefonuza gonderılen 6 haneli kodu girniz ") 
            gelen_sms=input(" kodu giriniz")
            if gelen_sms == sms_kodu:
                print("\n Kod Doğrulandı! Yeni şifre belirleme ekranına yönlendiriliyorsunuz.")
                yeni_sifre = input("Yeni şifrenizi giriniz: ")
                yeni_sifre_tekrar = input("Yeni şifrenizi tekrar giriniz: ")
                
                if yeni_sifre == yeni_sifre_tekrar:
                    self.sifre = yeni_sifre
                    print("Şifreniz başarıyla sıfırlanmış ve güncellenmiştir! Giriş yapabilirsiniz.")
                else:
                    print("Hata: Şifreler uyuşmuyor. İşlem iptal edildi.")
            else:
                print("Hata: Doğrulama kodunu yanlış girdiniz! Güvenlik nedeniyle işlem iptal edildi.")
                
       else:
            print("Hata: Girdiğiniz kimlik bilgileri sistemdeki verilerle uyuşmuyor!")

 def kartsis_işlemler(self):
       print("----------kartsiz islemler menüsü---------")
       girilen_tc=input("tc nizi tekrar giriniz")
       if girilen_tc==self.tc_no:
        print(f"Sayın {self.ad} {self.soyad}, kartsız girişiniz onaylandı.")
        print(f"Güncel toplam borcunuz: {self.borc} TL'dir.")
       else:
            print(f"Hata: Sistemde kayıtlı{girilen_tc} TC Kimlik Numarası bulunamadı")

aktif_musteri=None

while(True):
    ekrani_temizle()
    print(RENK_KIRMIZI +"""
===================================================================
  __  __ ______ _    _ __  __ ______ _______   ____             _  
 |  \/  |  ____| |  | |  \/  |  ____|__   __| |  _ \           | | 
 | \  / | |__  | |__| | \  / | |__     | |    | |_) | __ _ _ __| | __
 | |\/| |  __| |  __  | |\/| |  __|    | |    |  _ < / _` | '__| |/ /
 | |  | | |____| |  | | |  | | |____   | |    | |_) | (_| | |  |   < 
 |_|  |_|______|_|  |_|_|  |_|______|  |_|    |____/ \__,_|_|  |_|\_\
                                                                   
                     DİJİTAL BANKACILIK SİSTEMİ
==================================================================="""+RENK_SIFIRLA )
    
    print(RENK_TURKUAZ + "="*80)
    print(RENK_TURKUAZ + "\n")
    if aktif_musteri!=None:
         print(f"Aktif Oturum: {aktif_musteri.ad.upper()} {aktif_musteri.soyad.upper()}")
    else:
        print("Aktif Oturum: GİRİŞ YAPILMADI") 
          
    print("\nLÜTFEN YAPMAK İSTEDİGİNİZ İŞLEMİ SECİNİZ ".center(80))
    print("0--- YENİ MÜSTERİ KAYDİ YAPMA--- ".center(80))
    print("1---PARA CEKME---" .center(80))
    print("2---PARA YATİRMA---".center(80))
    print("3---BAKİYE SORGULAMA ".center(80))
    print("4---SENET ÖDEMESİ--- ".center(80))
    print("5--- HACİZ KALDIRMA İŞLEMLERİ--".center(80))
    print("6---ÖDEMELER---".center(80))
    print("7---YURT DISINA PARA TRANSFERİ--".center(80))
    print("8---FİNANSAL VERİLER--".center(80))
    print("9---QR KOD İŞLEMLERİ--".center(80))
    print("10--- HESAPLAMA ARACLARI---".center(80))
    print("11--- DİĞER İŞLEMLER---".center(80))
    print("12--- KARTSİZ İŞLEMLER---".center(80))
    print("13---UNUTULAN ŞİFREYİ DEGİSTİRME EKRANİ".center(80))
    print("14--- CIKIS".center(80))
    print("========================================" + RENK_SIFIRLA)
    secim= int(input("LÜTFEN SECİMİNİZİ YAPINIZ"))
   
    hesap_zorunlu_secenekler = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13]
    if secim in hesap_zorunlu_secenekler and aktif_musteri == None:
        print("\n uyari!!! bankamızda henüz bir hesabınız bulunmamaktadır!")
        print("Para çekme, yatırma, sorgulama gibi  işlemler için önce '0' ile kayıt olmalısınız.")
        continue 
  
    match secim:
     case 0:
            print("\n[YENİ HESAP AÇMA EKRANI]")
            ad = input("Adınız: ")
            soyad = input("Soyadınız: ")
            tc_no = input("TC Kimlik Numaranız (11 Hane): ")
            sifre = input("Hesabınız için 4 haneli bir şifre belirleyin: ")
            dogum_tarihi = input("Doğum Tarihiniz (GG/AA/YYYY): ")
            anne_soyad = input("Annenizin kızlık soyadı: ")
            tel_no = input("Telefon Numaranız: ")
            bakiye = int(input("Hesaba ilk etapta yatırılacak nakit tutarı: "))
            borc = int(input("Varsa bankamıza olan mevcut borcunuz (Yoksa 0): "))
            print(f"\nHesabınız başarıyla oluşturuldu! Hoş geldiniz, Sayın {ad} {soyad}.")   
            aktif_musteri = müsteri(ad, soyad, tc_no, sifre, dogum_tarihi, anne_soyad, tel_no, bakiye, borc)
            input("\nMenüye dönmek için Enter'a basın...")
             
     case 1:
          print("PARA CEKME İSLEMİNE HOSGELDİNİZ")
          işlem=int(input("LÜTFEN CEKMEK İSTEDİGİNİZ TUTARİ GİRİNİZ"))
          aktif_musteri.Para_cekme(işlem)
          aktif_musteri.Bakiye_görüntüle()
          input("\nMenüye dönmek için Enter'a basın...")
     case 2:
          print("PARA YATIRMA İSLEMİNE HOSGELDİNİZ")
          işlem=int(input("LÜTFEN YATIRMAK İSTEDİGİNİZ TUTARİ GİRİNİZ"))
          aktif_musteri.Para_yatirma(işlem)
          aktif_musteri.Bakiye_görüntüle()
          input("\nMenüye dönmek için Enter'a basın...")
     case 3:
            print(" BAKİYE SORGULAMA İSLEMİNE HOSGELDİNİZ")
            aktif_musteri.Bakiye_görüntüle()
     case 4:
           print(f"SENET ÖDEMESİ İŞLEMİNE HOŞGELDİNİZ")
           işlem=input("lütfen işlem yapmak istedginiz senet tutarını giriniz")
           aktif_musteri.Senet_odemesi(int(işlem))
     case 5:
           print("haciz kaldırma işlemi")
           işlem=int(input("lütfen işlem yapmak istediginiz tutarı gırınız "))
           aktif_musteri.Haciz_kaldirma_işlemi(işlem)
     case 6:
              print("ödemeler")
              kurum=input("lütfen ödeme yapacagınız kurumun adını giriniz")
              işlem=int(input("lütfen işlem turtarını giriniz"))
              aktif_musteri.Ödemeler(kurum,işlem)
     case 7:
             print("yurt dişi para transeferi")
             iban=input("lutfen ulusalrarası iban numarasını giriniz")
             işlem=int(input("lütfen işlem turtarıunı giriniz"))
             aktif_musteri.yurt_disina_para_transferi(iban,işlem)
     case 8:
                aktif_musteri.finansal_veriler()
     case 9:
             print("qr kod ile para cekme ye hosagledınız")
             işlem=int(input("lutfen ilem ttarini giriniz "))
             aktif_musteri.kod_işlemleri(işlem)
     case 10:
                aktif_musteri.hesaplama_araclari()
     case 11:
            aktif_musteri.diger_işlemler()
     case 12:
                print("\n[KARTSIZ İŞLEM GİRİŞİ]")
                tc = input("Lütfen 11 haneli TC Kimlik Numaranızı giriniz: ")
                aktif_musteri.kartsis_işlemler(tc)
     case 13:
                aktif_musteri.sifremi_unuttum()
     case 14:
            print("uygulamdan ciktiniz iyi gunler dileriz")
            break
     case _:
                print("LÜTFEN İSTENİLEN DEGER ARALIGINDA BİR SAYİ GİRİNİZ")
