class Process:
    def __init__(self, idx, name, time, period, dead_line=0):
        self.id = idx
        self.name = name
        self.final_execution_time = int(time)
        self.working_time = 0
        self.period = int(period)
        self.working = False
        self.ready = True
        self.remaining_deadline = int(dead_line)
        self.final_deadline = int(dead_line)

    def print(self):
        print('Name = {0}\nTime = {1}\nPeriod = {2}\nId = {3}'.format(self.name, self.final_execution_time, self.period, self.id))
