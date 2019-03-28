from gpiozero import LightSensor, Button
from time import time
from signal import pause
from timer import Timer
from racingTimer import RacingTimer

if __name__ == '__main__':

    START_L_PIN = 20
    FINISH_L_PIN = 21

    START_R_PIN = 23
    FINISH_R_PIN = 24
   
    left_racing_timer = RacingTimer(START_L_PIN, FINISH_L_PIN)
    right_racing_timer = RacingTimer(START_R_PIN, FINISH_R_PIN)

    print("Left Racing Timer:")
    left_racing_timer.status_message()
    
    print('Right Racing Timer:')
    right_racing_timer.status_message()
    
    while (
        left_racing_timer.ready and right_racing_timer.ready
    ):
        timer_L = Timer()
        timer_R = Timer()
        print('Programme started')
        
        left_racing_timer.start = timer_L.start
        left_racing_timer.finish = timer_L.finish
        
        right_racing_timer.start = timer_R.start
        right_racing_timer.finish = timer_R.finish
        
        pause()
   
    print('Lasers are not detected')
   