class Timer:
    def __init__(self):
        self.init()
        
    def init(self):
        self.start_trigger_count = 0
        self.finish_trigger_count = 0
        self.start_time = 0
        self.end_time = 0
        
    def start(self):
        if self.start_trigger_count == 0:
            print('Start')
            self.start_time = time()
            self.start_trigger_count += 1
        
    def finish(self):
        if self.finish_trigger_count == 0:
            print('Finish')
            self.end_time = time()
            self.finish_trigger_count += 1
            print(self.time_difference)
            quit()
        
    @property
    def time_difference(self):
        return self.end_time - self.start_time
    