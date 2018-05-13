import configparser
import datetime
from util.util import Util
from chart.chart import Chart

config = configparser.ConfigParser()
config.read('scheduling.ini')


def configuration_check():
    utilization = 0
    processes = config['Processes']
    number_of_task = len(processes)

    for i, p in enumerate(processes):
        utilization += int(processes[p].split(',')[0]) / int(processes[p].split(',')[1])

    if config['Scheduling']['Name'] == 'rm':

        U = number_of_task * ((2 ** (1 / number_of_task)) - 1)

        if utilization < U:
            print('Tasks are schedulable.\n {0} < {1}\n\n'.format(utilization, U))
            return True
        else:
            return False
    elif config['Scheduling']['Name'] == 'edf':
        if utilization < 1:
            print('Tasks are schedulable.\n {0} < 1\n\n'.format(utilization))
            return True
        else:
            return False


if configuration_check() == False:
    raise 'Tasks are not schedulable'

if config['Scheduling']['Name'] == 'rm':
    from algorithm.rm.algorithm import Scheduling
elif config['Scheduling']['Name'] == 'edf':
    from algorithm.edf.algorithm import Scheduling


class Main:
    def __init__(self):
        """
        Initialization of result file
        Creates instance according to conf file
        """
        Util.reset_file()
        self.selected_algorithm = Scheduling(config['Processes'], config['Scheduling']['Deadline'])


scheduling = Main()
scheduling.selected_algorithm.run()  # Algorithm is started

# Draws gantt chart according to result.txt
gantt = Chart('result.txt',
              'chart/img/gantt_{0}_{1}.svg'.format(config['Scheduling']['Name'], datetime.datetime.now().microsecond))
gantt.create_chart()
