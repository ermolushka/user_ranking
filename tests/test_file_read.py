import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from utils import read_txt


class TestFile(object):

    """
    Test if file is correct and we get a correct output

    """
    def test_file_ok(self):

        assert read_txt('customers.txt') == {12: ['52.986375', '-6.043701', 'Christina McArdle'],
                                             1: ['51.92893', '-10.27699', 'Alice Cahill'],
                                             2: ['51.8856167', '-10.4240951', 'Ian McArdle'],
                                             3: ['52.3191841', '-8.5072391', 'Jack Enright'],
                                             28: ['53.807778', '-7.714444', 'Charlie Halligan'],
                                             7: ['53.4692815', '-9.436036', 'Frank Kehoe'],
                                             8: ['54.0894797', '-6.18671', 'Eoin Ahearn'],
                                             26: ['53.038056', '-7.653889', 'Stephen McArdle'],
                                             27: ['54.1225', '-8.143333', 'Enid Gallagher'],
                                             6: ['53.1229599', '-6.2705202', 'Theresa Enright'],
                                             9: ['52.2559432', '-7.1048927', 'Jack Dempsey'],
                                             10: ['52.240382', '-6.972413', 'Georgina Gallagher'],
                                             4: ['53.2451022', '-6.238335', 'Ian Kehoe'],
                                             5: ['53.1302756', '-6.2397222', 'Nora Dempsey'],
                                             11: ['53.008769', '-6.1056711', 'Richard Finnegan'],
                                             31: ['53.1489345', '-6.8422408', 'Alan Behan'],
                                             13: ['53', '-7', 'Olive Ahearn'],
                                             14: ['51.999447', '-9.742744', 'Helen Cahill'],
                                             15: ['52.966', '-6.463', 'Michael Ahearn'],
                                             16: ['52.366037', '-8.179118', 'Ian Larkin'],
                                             17: ['54.180238', '-5.920898', 'Patricia Cahill'],
                                             39: ['53.0033946', '-6.3877505', 'Lisa Ahearn'],
                                             18: ['52.228056', '-7.915833', 'Bob Larkin'],
                                             24: ['54.133333', '-6.433333', 'Rose Enright'],
                                             19: ['55.033', '-8.112', 'Enid Cahill'],
                                             20: ['53.521111', '-9.831111', 'Enid Enright'],
                                             21: ['51.802', '-9.442', 'David Ahearn'],
                                             22: ['54.374208', '-8.371639', 'Charlie McArdle'],
                                             29: ['53.74452', '-7.11167', 'Oliver Ahearn'],
                                             30: ['53.761389', '-7.2875', 'Nick Enright'],
                                             23: ['54.080556', '-6.361944', 'Eoin Gallagher'],
                                             25: ['52.833502', '-8.522366', 'David Behan']}

    """
    Check if file doesn't match our structure
    """
    def test_file_bad(self):

        assert read_txt("fake_customers.txt") == {0: [0, 0, "test"]}