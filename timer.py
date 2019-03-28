from time import time


class Timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = time()

    def finish(self):
        self.end_time = time()

    @property
    def duration(self):
        return self.end_time - self.start_time
