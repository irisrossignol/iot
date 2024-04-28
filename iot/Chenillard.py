from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps

pinNumber = 17 # declaration d'une variable pinNumber à 17
led1 = Pin(pinNumber, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17 
                                   #et on prescise que c'est une pin de sortie de courant (OUT)
pinNumber = 14
led2 = Pin(pinNumber, mode=Pin.OUT)  
                                  
pinNumber = 10 
led3 = Pin(pinNumber, mode=Pin.OUT)
                                   

while True:          # boucle infini
    led1.toggle()     
    utime.sleep(0.2)    
    led1.toggle()
    led2.toggle()    
    utime.sleep(0.2)    
    led2.toggle()
    led3.toggle()     
    utime.sleep(0.2)    
    led3.toggle()
    
    #led.on()          # allume la led 
    #led.off()         # eteind la led 

