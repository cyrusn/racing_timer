from signal import pause
from track_timer import TrackTimer
from google_form import Form
from functools import reduce
from school import School
from sys import stderr


def ready(tracks):
    timers = [track["timer"] for track in tracks]
    return reduce((lambda x, y: x.ready and y.ready), timers)


def setTimersInfo(tracks):
    for timer in [track["timer"] for track in tracks]:
        School.printList()

        school_code = ""
        while school_code.upper() not in ["A", "B", "C", "D"]:
            school_code = input("School Code of Track {}: ".format(timer.track))
        timer.school_code = school_code

        team = 0
        while int(team) not in [1, 2, 3]:
            team = input("Team (1-3): ")
        timer.team = team
        print("{:=<30}".format(""))


def checkSensorStatus(tracks):
    if not ready(tracks):
        for timer in [track["timer"] for track in tracks]:
            message = "Track {}\n{}".format(timer.track, timer.sensor_status)
            if timer.ready:
                print(message)
            else:
                print(message, file=stderr)
            print("{:=<30}".format(""))
        exit(0)


def initTimers(tracks):
    for track in tracks:
        start_pin = track["start_pin"]
        finish_pin = track["finish_pin"]
        track["timer"] = TrackTimer(start_pin, finish_pin, track["name"])


def listen_events(tracks):
    while ready(tracks):
        print("Programme is ready.\n")

        for timer in [track["timer"] for track in tracks]:
            timer.when_start = timer.on_start
            timer.when_finish = timer.on_finish

        pause()


if __name__ == "__main__":

    tracks = [
        {"name": "A", "start_pin": 23, "finish_pin": 24, "timer": None},
        {"name": "B", "start_pin": 20, "finish_pin": 21, "timer": None},
    ]

    initTimers(tracks)
    checkSensorStatus(tracks)
    setTimersInfo(tracks)
    listen_events(tracks)
