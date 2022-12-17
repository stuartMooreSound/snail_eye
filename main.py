import machine 
import utime   
 
analogInputPin = machine.ADC(26) #set up access to analog pin
pwmOutputPin = machine.PWM(machine.Pin(16)) # GP16
pwmOutputPin.freq(100) # 100Hz 

while True:
    x = analogInputPin.read_u16()     
    y = (x*x*x*x)/(12.5e12) #or how about (x*x)/2.5e4
    y = min(65535, y)
    y = max(0, y)
    
    pwmOutputPin.duty_u16(int(y))     
    print("PWM: ",y)
    utime.sleep(0.2)


