import RPi.GPIO as GPIO #Pin
import time #Time
import board
import dht11
import socket
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

# Setup Led Pins
GPIO.setup(17, GPIO.OUT) #Red Led
GPIO.setup(27, GPIO.OUT) #Green Led
GPIO.setup(22, GPIO.OUT) #Blue Led
GPIO.setup(26, GPIO.OUT) #Yellow Led

# Setup Button Pins
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Button Boolean Variables
Sicaklik = 25
AyarlamaModu = True
Arttir = False
Azalt = False
AcKapat = False
Breakit = False
TempBool = True
global Pressed2
Pressed2 = False

#Client-Server Bilgileri
TCP_IP = '192.168.0.30'
TCP_PORT = 5900
#MESSAGE = b'deneme2333'

# Led Functions
def RedLight():
        GPIO.output(17, True)
        time.sleep(0.5)
        GPIO.output(17, False)
        time.sleep(0.5) 

def GreenLight():
    GPIO.output(27, True)
    time.sleep(1)
    GPIO.output(27, False)
    time.sleep(1)

def BlueLight():
   GPIO.output(22, True)
   time.sleep(1)
   GPIO.output(22, False)
   time.sleep(1)

def YellowLight():
   GPIO.output(26, True)
   time.sleep(1)
   GPIO.output(26, False)
   time.sleep(1)
   
#DHT11 Sensor Function
def TempSensor(TempKontrol):
    while TempKontrol:
            instance = dht11.DHT11(pin = 4)
            result = instance.read()
            
            if not GPIO.input(6):
                if not Pressed2:
                 print('_________________________________')
                 print("Sıcaklık ayarlama moduna geçiliyor.")
                 print('_________________________________')
                 pressed = True
                 SıcaklıkAyarlamaModu(True)
                 # button not pressed (or released)
                else:
                  pressed = False
                  time.sleep(0.1)
            
    #         time.sleep(3.0)
            try:
                if result.is_valid():
                    print("Sıcaklık: %-3.1f C" % result.temperature)
                    print("Nem: %-3.1f %%" % result.humidity)

                    print("DHT11 Sıcaklık:", result.temperature , "Ayarlı Sıcaklık:" , Sicaklik)
                    MessageString = "DHT11 Sicaklik:"+ str(result.temperature) + "-Ayarli Sicaklik:" + str(Sicaklik) 
                    Message = bytes(MessageString,'utf8')
                    if result.temperature < Sicaklik:
                        print("Oda sıcaklığı ayarladığınız sıcaklıktan düşük.")
                        RedLight()
                    elif result.temperature > Sicaklik-5 and result.temperature < Sicaklik+5:
                        print("Stabil")
                        GreenLight()
                    else:
                        print("Sıcaklıkta aşma meydana geldi. Oda sıcaklığı, ayarladığınız sıcaklığın üstüne çıktı.")
                        BlueLight()
                        
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((TCP_IP, TCP_PORT))
                    s.send(Message)
                    s.close()               
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

def SıcaklıkAyarlamaModu(AyarlamaModuTemp):
    global Sicaklik
    print("Sıcaklık ayarlama modundasınız. Sensör bu sırada çalışmayacaktır.")
    while AyarlamaModuTemp:           
                if not GPIO.input(5):
                  if not pressed:
                     Sicaklik = Sicaklik - 5
                     print('_________________________________')
                     print('Sıcaklığı azalttınız.')
                     print('Mevcut Sıcaklık: ' , Sicaklik)
                     print('_________________________________')
                     pressed = True
                     time.sleep(1)
                else:
                  pressed = False
                  time.sleep(1)
              
                if not GPIO.input(6):
                  if not pressed:
                     print('_________________________________')
                     print("Sıcaklık ayarlama modundan çıkılıyor.")
                     print('_________________________________')
                     pressed = True
                     AyarlamaModuTemp = False
                     time.sleep(1)
                     TempSensor(True)
                else:
                  pressed = False
                  time.sleep(1)
              
                if not GPIO.input(16):
                  if not pressed:
                     Sicaklik = Sicaklik + 5
                     print('_________________________________')
                     print('Sıcaklığı arttırdınız.')
                     print('Mevcut Sıcaklık: ' , Sicaklik)
                     print('_________________________________')
                     pressed = True
                else:
                  pressed = False
                  time.sleep(1)
# Program çalışınca buton modu otomatik açılacak. Buton modunda sıcaklık ayarları yapıp tekrar
# ortadaki butona basacağız. Böylece buton modundan çıkıp, sensörü çalıştırmış olacağız.
Sicaklik = 20
RedLight()
print("Ayarlanabilir Termostat programı çalıştırıldı.")
print("______________________________________________")
SıcaklıkAyarlamaModu(True)
TumIsiklariKapat()
   # print("Çıkış Yapıldı")

print("Çıkış")

