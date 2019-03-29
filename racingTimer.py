from gpiozero import LightSensor, Button
from time import time
from timer import Timer

CHARGE_TIME_LIMIT = 0.005
THRESHOLD = 0.05
QUEUE_LEN = 1


class RacingTimer:
    def __init__(self, start_pin, finish_pin):
        self.start_sensor = LightSensor(
            start_pin,
            threshold=THRESHOLD,
            charge_time_limit=CHARGE_TIME_LIMIT,
            queue_len=QUEUE_LEN,
        )
        self.finish_sensor = LightSensor(
            finish_pin,
            threshold=THRESHOLD,
            charge_time_limit=CHARGE_TIME_LIMIT,
            queue_len=QUEUE_LEN,
        )

    @property
    def start_ready(self):
        return self.start_sensor.light_detected

    @property
    def finish_ready(self):
        return self.finish_sensor.light_detected

    @property
    def ready(self):
        return self.start_ready and self.finish_ready

    @property
    def when_start(self):
        return self.start_sensor.when_dark

    @when_start.setter
    def when_start(self, value):
        if not self.ready:
            self.finish_sensor.when_dark = None
        else:
            self.start_sensor.when_dark = value

    @property
    def when_finish(self):
        return self.finish_sensor.when_dark

    @when_finish.setter
    def when_finish(self, value):
        if not self.ready:
            self.finish_sensor.when_dark = None
        else:
            self.finish_sensor.when_dark = value

    @property
    def status_message(self):
        return "Start: {}\nFinish: {}".format(self.start_ready, self.finish_ready)


if __name__ == "__main__":
    from signal import pause

    start_pin = 20
    finish_pin = 21

    def startMessage():
        print("start")

    def finishMessage():
        print("finish")

    racingTimer = RacingTimer(start_pin, finish_pin)

    message = racingTimer.status_message
    print(message)

    racingTimer.when_start = startMessage
    racingTimer.when_finish = finishMessage

    pause()

