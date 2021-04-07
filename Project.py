#Kütüphaneler
import RPi.GPIO as GPIO 
import time 
import board
import dht11

#PIN Modları
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED Işıkları için PIN Ayarlama
GPIO.setup(17, GPIO.OUT) #Red Led (GPIO 17 Pin)
GPIO.setup(27, GPIO.OUT) #Green Led (GPIO 27 Pin)
GPIO.setup(22, GPIO.OUT) #Blue Led (GPIO 22 Pin) 
GPIO.setup(26, GPIO.OUT) #Yellow Led (GPIO 26 Pin)

# Butonlar için PIN Ayarlama
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # 1.Buton (GPIO 5 Pin)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) # 2. Ortadaki Buton (GPIO 6 Pin)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # 3.Buton (GPIO 16 Pin)

# Değişkenler
Sicaklik = 25
AyarlamaModu = True
Arttir = False
Azalt = False
AcKapat = False
Breakit = False
TempBool = True
global Pressed2
Pressed2 = False
    
# Led Işığı Fonksiyonları
# Kırmızı -> Uyarı
# Yeşil -> Stabil
# Mavi -> Aşmış
# Sarı -> Hata


#Kırmızı Işık Fonksiyonu
#Kırmızı Işığı Yakıp Söndürür
def RedLight(check):
    if check == 0:
        for i in range(3):
            GPIO.output(17, True)
            GPIO.output(17, False)
    else:
        GPIO.output(17, True)
        time.sleep(0.5)
        GPIO.output(17, False)
        time.sleep(0.5) 
    
#Yeşil Işık Fonksiyonu
#Yeşil Işığı Yakıp Söndürür
def GreenLight():
    GPIO.output(27, True)
    time.sleep(1)
    GPIO.output(27, False)
    time.sleep(1)
    print("Yeşil Işık")

#Mavi Işık Fonksiyonu
#Mavi Işığı Yakıp Söndürür
def BlueLight():
   GPIO.output(22, True)
   time.sleep(1)
   GPIO.output(22, False)
   time.sleep(1)
   print("Mavi Işık")

#Sarı Işık Fonksiyonu
#Sarı Işığı Yakıp Söndürür
def YellowLight():
   GPIO.output(26, True)
   time.sleep(1)
   GPIO.output(26, False)
   time.sleep(1)
   print("Sarı Işık")
   
#DHT11 Sıcaklık ve Nem Sensörü Fonksiyonu
def TempSensor():
    
    while True:
        Kontrol = True
        if Kontrol: 
            instance = dht11.DHT11(pin = 4)
            result = instance.read()
            
            if not GPIO.input(6):
                if not Pressed2:
                 print('_________________________________')
                 print("Sıcaklık ayarlama moduna geçiliyor.")
                 print('_________________________________')
                 pressed = True
                 AyarlamaModu = True
                 Kontrol = True
                 # return eklencek. While döngüsünü bitirmek için
                 # button basılmadı
                else:
                  pressed = False
                  time.sleep(0.1)
            
    #         time.sleep(3.0)
            try:
                if result.is_valid():
                    print("Sıcaklık: %-3.1f C" % result.temperature)
                    print("Nem: %-3.1f %%" % result.humidity)
                    if result.temperature < 25:
                        RedLight(1)
                    elif result.temperature > 25 and result.temperature < 35:
                        GreenLight()
                    else:
                        BlueLight()
                else:
                    YellowLight()
            except RuntimeError as error:
                print(error.args[0])
                YellowLight()
                #time.sleep(2.0)
                continue
            except Exception as error:
                YellowLight()
                dhtDevice.exit()
                raise error
    #         time.sleep(3.0)
        else:
            break


# __Main__
RedLight(1) #Deneme amaçlı bir kez kırmızı ışık yakılır.

while True:
    if AyarlamaModu:
        if TempBool:
         print("Sıcaklık ayarlama modundasınız. Sensör bu sırada çalışmayacaktır.")
         TempBool = False
        else:
        #TempSensor()
        # buton basıldı
            if not GPIO.input(5):
              if not pressed:
                 Sicaklik = Sicaklik - 5
                 print('_________________________________')
                 print('Sıcaklığı azalttınız.')
                 print('Mevcut Sıcaklık: ' , Sicaklik)
                 print('_________________________________')
                 pressed = True
                # button basılmadı
            else:
              pressed = False
              time.sleep(0.1)
              
            if not GPIO.input(6):
              if not pressed:
                 print('_________________________________')
                 print("Sıcaklık ayarlama modundan çıkılıyor.")
                 print('_________________________________')
                 pressed = True
                 AyarlamaModu = False
                # button basılmadı
            else:
              pressed = False
              time.sleep(0.1)
              
            if not GPIO.input(16):
              if not pressed:
                 Sicaklik = Sicaklik + 5
                 print('_________________________________')
                 print('Sıcaklığı arttırdınız.')
                 print('Mevcut Sıcaklık: ' , Sicaklik)
                 print('_________________________________')
                 pressed = True
                # button basılmadı
            else:
              pressed = False
              time.sleep(0.1)

    else:
        TempSensor()
        
print("Çıkış yapıldı.")

