from time import time


class Timer:
    def __init__(self):
        self.is_started = False
        self.is_finished = False
        self.start_time = 0
        self.end_time = 0

    def start(self):
        if not self.is_started:
            self.start_time = time()
            self.is_started = True

    def finish(self):
        if not self.is_finished:
            self.end_time = time()
            self.is_finished = True

    @property
    def time_difference(self):
        return self.end_time - self.start_time

