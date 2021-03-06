from model.process import Process
from util.util import Util


class Scheduling:
    def __init__(self, processes, deadline):
        self.processes = Scheduling.init_processes(processes)
        self.priority = self.init_priority()
        self.deadline = int(deadline)
        self.time = 0

    @staticmethod
    def init_processes(processes):
        """
        Initialization of processes
        :param processes:
        :return:
        """
        p_arr = []

        for index, p in enumerate(processes):
            process = Process(index, p, processes[p].split(',')[0], processes[p].split(',')[1],
                              processes[p].split(',')[2])
            p_arr.append(process)

        return p_arr

    def init_priority(self):
        """
        Sets initial values of priority
        The process with the least number of remaining deadline has the highest priority
        :return:
        """
        arr = []
        priority_dict = dict()

        for p in self.processes:
            priority_dict[p.id] = int(p.remaining_deadline)

        for key, value in sorted(priority_dict.items(), key=lambda value: value[1]):
            arr.append(key)

        return arr

    def update_priority(self):
        """
        Remaining deadline is updated
        :return:
        """
        for i, p in enumerate(self.processes):
            if p.remaining_deadline >= 0:
                self.processes[i].remaining_deadline -= 1

    def setup_period(self):
        """
        Period of processes are checked  for setting up ready flag and removing working time
        :return:
        """
        for i, p in enumerate(self.processes):
            if self.time % p.period == 0:
                self.processes[i].ready = True
                self.processes[i].working_time = 0
                self.processes[i].remaining_deadline = self.processes[i].final_deadline

    def select_process(self):
        """
        Next process which will be executed, is selected
        :return:
        """
        result = -1
        last_min_remaining_deadline = 0

        for i, p in enumerate(self.processes):
            if self.processes[i].working_time < self.processes[i].final_execution_time:
                if last_min_remaining_deadline == 0 or self.processes[i].remaining_deadline < last_min_remaining_deadline:
                    last_min_remaining_deadline = self.processes[i].remaining_deadline
                    result = i

        return result

    def execute_process(self, idx):
        """
        Executing process ...
        :param idx:
        :return:
        """
        if idx != -1:
            self.processes[idx].working = True
            self.processes[idx].working_time += 1
            Util.write('{0},{1},{2}\n'.format(self.processes[idx].name, self.time, (self.time + 1)))

    def run(self):
        """
        The algorithm runs until the time of the last date in the conf file
        :return:
        """
        while self.time <= self.deadline:
            self.setup_period()
            self.execute_process(self.select_process())
            self.time += 1
            self.update_priority()
