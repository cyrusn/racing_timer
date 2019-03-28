from gpiozero import Button
from signal import pause

class MyButton:
    def __init__(self, pin):
        self.button = Button(pin)
    
    @property
    def when_custom_pressed(self):
        return self.button.when_pressed 
        
    @when_custom_pressed.setter
    def when_custom_pressed(self, value):
        self.button.when_pressed = value
        

if __name__ == "__main__":
    button = MyButton(16)
    
    def sayHello():
        print('hello')
        
    button.when_custom_pressed = sayHello
    
    pause()