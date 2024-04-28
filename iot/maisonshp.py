import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json
from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import time # importe dans le code la lib qui permet de gerer le temps
import random

pwm_ledrouge = PWM(Pin(10,mode=Pin.OUT))
pwm_ledrouge.freq(1_000)
pwm_ledvert = PWM(Pin(9,mode=Pin.OUT))
pwm_ledvert.freq(1_000)
pwm_ledbleu = PWM(Pin(8,mode=Pin.OUT))
pwm_ledbleu.freq(1_000)    

house = {
    'Gryffindor' : [23000,0,0],
    'Slytherin' : [0,23000,0],
    'Ravenclaw' : [0,0,23000],
    'Hufflepuff' : [23000,2000,0]
}

perso = [
    "https://hp-api.onrender.com/api/character/9e3f7ce4-b9a7-4244-b709-dae5c1f1d4a8"
    "https://hp-api.onrender.com/api/character/d5c4daa3-c726-426a-aa98-fb40f3fba816"
    "https://hp-api.onrender.com/api/character/8f9aa40b-5d7c-441e-ad32-4564ecda3b70"
    "https://hp-api.onrender.com/api/character/3569d265-bd27-44d8-88e8-82fb0a848374"
]

personnage = random.choice(perso)

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'Iphone de Iris (2)'
password = 'azertyuiop'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://hp-api.onrender.com/api/character/3569d265-bd27-44d8-88e8-82fb0a848374"
# http  ton IP  ton port  route 1  sous-route
while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        maison = r.json()[0]["house"]
        # print(r.json()["name"]) # traite sa reponse en Json
        print(r.json()[0]["house"])
        # print(personnage(r.json()[0]["house"]))
        r.close() # ferme la demande
        utime.sleep(1)
        pwm_ledrouge.duty_u16(house[maison][0])
        pwm_ledvert.duty_u16(house[maison][1])
        pwm_ledbleu.duty_u16(house[maison][2])


    except Exception as e:
        print(e)



