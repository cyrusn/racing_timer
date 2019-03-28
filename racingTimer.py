from gpiozero import LightSensor, Button
from time import time
from signal import pause
from timer import Timer


if __name__ == '__main__':
    CHARGE_TIME_LIMIT = 0.005
    THRESHOLD = 0.05
    QUEUE_LEN = 1
    
    START_L_PIN = 20
    FINISH_L_PIN = 21

    START_R_PIN = 23
    FINISH_R_PIN = 24


    start_L_sensor = LightSensor(START_L_PIN, threshold=THRESHOLD, charge_time_limit=CHARGE_TIME_LIMIT, queue_len=QUEUE_LEN)
    finish_L_sensor = LightSensor(FINISH_L_PIN, threshold=THRESHOLD, charge_time_limit=CHARGE_TIME_LIMIT, queue_len=QUEUE_LEN)

    start_R_sensor = LightSensor(START_R_PIN, threshold=THRESHOLD, charge_time_limit=CHARGE_TIME_LIMIT, queue_len=QUEUE_LEN)
    finish_R_sensor = LightSensor(FINISH_R_PIN, threshold=THRESHOLD, charge_time_limit=CHARGE_TIME_LIMIT, queue_len=QUEUE_LEN)

    print('Left: Start: {}, Finish: {}'.format(start_L_sensor.light_detected, finish_L_sensor.light_detected))
    print('Right: Start: {}, Finish: {}\n'.format(start_R_sensor.light_detected, finish_R_sensor.light_detected))
    
    while (
        start_L_sensor.light_detected and 
        finish_L_sensor.light_detected and
        start_R_sensor.light_detected and 
        finish_R_sensor.light_detected
    ):
        timer_L = Timer()
        timer_R = Timer()
        print('Programme started')
        
        start_L_sensor.when_dark = timer_L.start
        finish_L_sensor.when_dark = timer_L.finish
        
        start_R_sensor.when_dark = timer_R.start
        finish_R_sensor.when_dark = timer_R.finish
        
        pause()
   
    print('Lasers are not detected')
   