from track_sensor import TrackSensor
from timer import Timer
from google_form import Form
from school import School
from format_string import format_string


class TrackTimer(TrackSensor, Timer, Form):
    def __init__(self, start_pin, finish_pin, track):
        TrackSensor.__init__(self, start_pin, finish_pin)
        Timer.__init__(self)
        Form.__init__(self)

        self.track = track

        self.is_started = False
        self.is_finished = False

        self.school_code = None
        self.team = None

    @property
    def school_name(self):
        return School.getName(self.school_code)

    def on_start(self):
        if not self.is_started:
            self.is_started = True

            self.start()

            print(format_string("Start", self.track, self.school_name, self.team))

    def on_finish(self):
        if (not self.is_finished) and self.is_started:
            self.is_finished = True

            self.finish()

            print(
                format_string(
                    "Finish", self.track, self.school_name, self.team, self.duration
                )
            )
            self.submit(self.school_code, self.team, self.track, self.duration)


if __name__ == "__main__":

    from signal import pause

    START_PIN = 20
    FINISH_PIN = 21

    School.printSchoolList()
    track_timer = TrackTimer(START_PIN, FINISH_PIN, "A")

    school_code = input("school_code: ")
    team = input("Team (1-3): ")
    track_timer.school_code = school_code
    track_timer.team = team

    print("Racing Timer:")
    print(track_timer.status_message())

    if track_timer.ready:
        print("\nProgramme ready\n")
        track_timer.when_start = track_timer.on_start
        track_timer.when_finish = track_timer.on_finish
        pause()

    print("Lasers are not detected")
