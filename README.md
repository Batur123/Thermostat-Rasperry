# Raspberry Pi 4 Adjustable Thermostat Project<br>
Mandatory School Intern Project <br>
## Prerequisites <br>
Raspberry Pi 4 <br>
Jumper Cables (M-F) (M-M) <br>
DHT11 Humidity & Temperature Sensor <br>
Green,Yellow,Blue,Red LED Light <br>
2 x Large Button <br>
1 x Small Button <br>
3 x 23 Ohm (Red-Red-Black-Gold) Resistor <br>
1 x 10.50000k Ohm (Brown-Red-Orange-Gold) Resistor <br>

## Python Libraries <br>
RPi.GPIO as GPIO <br>
time <br>
board <br>
dht11 <br>
socket <br>

## GPIO Pin Connections <br>
Raspberry Pin-2 (5v)-> Breadboard + (Red Line)<br>
Raspberry Pin-6 (GND)-> Breadboard – (Blue Line)<br>
Raspberry Pin-7 (GPIO-4)-> DHT11 Data Pin<br>
Raspberry Pin-11 (GPIO-17)-> 23 Ohm Resistor-> Red Led (+) (Long Leg)<br>
Raspberry Pin-13 (GPIO-27)-> 23 Ohm Resistor-> Green Led (+) (Long Leg)<br>
Raspberry Pin-15 (GPIO-22)-> 23 Ohm Resistor-> Blue Led (+) (Long Leg)<br>
Raspberry Pin-29 (GPIO-5)-> Big Button-1 VCC<br>
Raspberry Pin-31 (GPIO-6)-> Small Button-1 VCC<br>
Raspberry Pin-36 (GPIO-16)-> Big Button-2 VCC<br>
Raspberry Pin-37 (GPIO-26)-> 23 Ohm Resisor-> Yellow Led (+) (Long Leg)<br>
Red Led (-) (Short Leg)-> Breadboard (-) (Blue Line)<br>
Green Led (-) (Short Leg)-> Breadboard (-) (Blue Line)<br>
Blue Led (-) (Short Leg)-> Breadboard (-) (Blue Line)<br>
Yellow Led (-) (Short Leg)-> Breadboard (-) (Blue Line)<br>
DHT11 VCC-> Breadboard (+) (Red Line)<br>
DHT11 GND-> Breadboard (-) (Blue Line)<br>
Big Button-1 GND-> Breadboard (-) (Blue Line)<br>
Small Button-1 GND-> Breadboard (-) (Blue Line)<br>
Big Button-2 GND-> Breadboard (-) (Blue Line)<br>

