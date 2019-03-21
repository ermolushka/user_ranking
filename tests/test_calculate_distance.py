import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from utils import compute_distance


class TestDistance(object):

    """
    Test if file is distance calculations are correct

    """
    def test_distance_ok(self):

        assert compute_distance(52.986375, -6.043701, 53.339428, -6.257664, "Christina McArdle") == [36.271572836813576, 'Christina McArdle']

    """
    Test if file is distance calculations are correct for invalid input format

    """
    def test_distance_bad(self):

        assert compute_distance("ssd", "aaa", 53.339428, -6.257664, "Christina McArdle") == [0, 0]
