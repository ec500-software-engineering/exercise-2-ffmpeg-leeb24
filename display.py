from ascii_graph import Pyasciigraph
from ascii_graph.colors import *
from ascii_graph.colordata import vcolor
import threading

class DisplayHandler(object):

    '''
    :developer: Byoungsui Lee && Seunghee Lee
    This class receives numerical data from sensor readers and
    encodes the data for a display technology

    The displayhandler obejct will take in a object containing the vital data.
    Then it will parse the data into three catagories ( blood oxygen, blood pressure, pulse)
    Each of these parsed data will be the input for the three display methods.

    :param oxy: uint32_t value of blood oxygen level;
    returns: void function ( displays blood oxygen level )
    :raises keyError: raises an exception

    :param systolic: uint32_t value of blood pressure;
    :param diatolic: uint32_t value of blood pressure;
    returns: void function ( displays blood pressure level )
    :raises keyError: raises an exception

    :param pulse: uint32_t value of blood pulse;
    returns: void function ( displays pulselevel )
    :raises keyError: raises an exception
    '''

    def display_blood_oxygen(self, oxy):
        pass

    def display_blood_pressure(self, systolic, diastolic):
        pass

    def display_blood_pulse(self, pulse):
        pass


class TextTerminalDisplay(DisplayHandler):
    '''
    :developer: N/A
    A simple derived class which will print data to the terminal (stdout)
    '''

    def __init__(self):
        self._cur_oxygen = 0
        self._cur_systolic = 0
        self._cur_diastolic = 0
        self._cur_pulse = 0
        self._graph_lock = threading.Lock()
        self._graph = Pyasciigraph()

    def display_blood_oxygen(self, oxy):
        self._cur_oxygen = oxy
        self.display_graph()

    def display_blood_pressure(self, systolic, diastolic):
        self._cur_diastolic = diastolic
        self._cur_systolic = systolic
        self.display_graph()

    def display_blood_pulse(self, pulse):
        self._cur_pulse = pulse
        self.display_graph()

    def display_graph(self):
        #print('Thread {}: waiting for lock'.format(threading.get_ident()))
        pattern = [Gre, Blu, Red]
        
        self._graph_lock.acquire(blocking=True)
        data = vcolor([('Heart Rate', self._cur_pulse), ('SYS mmHg kPa', self._cur_systolic),
                ('DIA mmHg kPa', self._cur_diastolic), ('Oxygen Saturation', self._cur_oxygen)],pattern)

        for graph_line in self._graph.graph('VITAL READINGS', data):
            print(
                graph_line
            )
        #print('Thread {}: releasing lock'.format(threading.get_ident()))
        self._graph_lock.release()



