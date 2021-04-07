#Libraries
import RPi.GPIO as GPIO 
import time 
import board
import dht11

#PIN Modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED Light PINS
GPIO.setup(17, GPIO.OUT) #Red Led (GPIO 17 Pin)
GPIO.setup(27, GPIO.OUT) #Green Led (GPIO 27 Pin)
GPIO.setup(22, GPIO.OUT) #Blue Led (GPIO 22 Pin) 
GPIO.setup(26, GPIO.OUT) #Yellow Led (GPIO 26 Pin)

# Button PINS
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # First Buton (GPIO 5 Pin)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Second Buton (GPIO 6 Pin)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Third Buton (GPIO 16 Pin)

# Variables
Sicaklik = 25 #temperature
AyarlamaModu = True #configmode boolean
Arttir = False #increment
Azalt = False #decrement
AcKapat = False #openclose
Breakit = False #breakit
TempBool = True 
global Pressed2
Pressed2 = False
    
# Led Functions
# Red -> Warning
# Green -> Stabile
# Blue -> Over
# Yellow -> Error

#Red Light Function
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
    
#Green Light Function
def GreenLight():
    GPIO.output(27, True)
    time.sleep(1)
    GPIO.output(27, False)
    time.sleep(1)
    print("Green")

#Blue Light FUnction
def BlueLight():
   GPIO.output(22, True)
   time.sleep(1)
   GPIO.output(22, False)
   time.sleep(1)
   print("Blue")

#Yellow Light Function
def YellowLight():
   GPIO.output(26, True)
   time.sleep(1)
   GPIO.output(26, False)
   time.sleep(1)
   print("Yellow")
   
#DHT11 Temp Sensor
def TempSensor():
    
    while True:
        Kontrol = True
        if Kontrol: 
            instance = dht11.DHT11(pin = 4)
            result = instance.read()
            
            if not GPIO.input(6):
                if not Pressed2:
                 print('_________________________________')
                 print("Configuration Mode ON")
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
                    print("Temp: %-3.1f C" % result.temperature)
                    print("Humidity: %-3.1f %%" % result.humidity)
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
RedLight(1) 

while True:
    if AyarlamaModu:
        if TempBool:
         print("You are now in configuration mode. Sensor will not work.")
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
        
print("Exit1")

