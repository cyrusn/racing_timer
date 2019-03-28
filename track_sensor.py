from gpiozero import LightSensor
from time import time
from timer import Timer

CHARGE_TIME_LIMIT = 0.01  # default to 0.01
THRESHOLD = 0.1  # default to 0.1
QUEUE_LEN = 1  # defaults to 5


class TrackSensor:
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
        start_sensor_message = "{:<15}{start:>15}".format(
            "Start:", start="OK" if self.start_ready else "Fail"
        )

        finish_sensor_message = "\n{:<15}{finish:>15}".format(
            "Finish:", finish="OK" if self.finish_ready else "Fail"
        )

        return start_sensor_message + finish_sensor_message


if __name__ == "__main__":
    from signal import pause

    start_pin = 20
    finish_pin = 21

    def startMessage():
        print("start")

    def finishMessage():
        print("finish")

    sensor = TrackSensor(start_pin, finish_pin)

    message = sensor.status_message
    print(message)

    sensor.when_start = startMessage
    sensor.when_finish = finishMessage

    pause()

