from track_sensor import TrackSensor
from timer import Timer
from google_form import Form
from school import School
from format_string import format_string


class TrackTimer:
    def __init__(self, start_pin, finish_pin, track):
        self.is_started = False
        self.is_finished = False
        self.track = track
        self.form = Form()
        self.track_sensor = TrackSensor(start_pin, finish_pin)
        self.timer = Timer()

        self.school_code = None
        self.team = None

    @property
    def school_name(self):
        return School.getName(self.school_code)

    @property
    def when_start(self):
        return self.track_sensor.when_start

    @when_start.setter
    def when_start(self, value):
        self.track_sensor.when_start = value

    @property
    def when_finish(self):
        return self.track_sensor.when_finish

    @when_finish.setter
    def when_finish(self, value):
        self.track_sensor.when_finish = value

    @property
    def duration(self):
        return self.timer.duration

    @property
    def ready(self):
        return self.track_sensor.ready

    @property
    def sensor_status(self):
        return self.track_sensor.status_message

    def start(self):
        if not self.is_started:
            self.is_started = True

            self.timer.start()

            print(format_string("Start", self.track, self.school_name, self.team))

    def finish(self):
        if (not self.is_finished) and self.is_started:
            self.is_finished = True

            self.timer.finish()

            print(
                format_string(
                    "Finish", self.track, self.school_name, self.team, self.duration
                )
            )
            self.form.submit(self.school_code, self.team, self.track, self.duration)


if __name__ == "__main__":

    from signal import pause

    START_PIN = 20
    FINISH_PIN = 21

    School.printSchoolList()
    track = "A"
    track_timer = TrackTimer(START_PIN, FINISH_PIN, track)

    school_code = input("school_code: ")
    team = input("Team (1-3): ")
    track_timer.school_code = school_code
    track_timer.team = team

    print("Left Racing Timer:")
    print(track_timer.sensor_status)

    if track_timer.ready:
        print("\nProgramme ready\n")
        track_timer.when_start = track_timer.start
        track_timer.when_finish = track_timer.finish
        pause()

    print("Lasers are not detected")
