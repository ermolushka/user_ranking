import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from utils import rank_users


class TestRanking(object):

    """
    Test if file is ranking calculations are correct

    """
    def test_ranking_ok(self):

        assert rank_users("customers.txt") == "{4: 'Ian Kehoe', 5: 'Nora Dempsey', 6: 'Theresa Enright', 8: 'Eoin Ahearn', 11: 'Richard Finnegan', 12: 'Christina McArdle', 13: 'Olive Ahearn', 15: 'Michael Ahearn', 17: 'Patricia Cahill', 23: 'Eoin Gallagher', 24: 'Rose Enright', 26: 'Stephen McArdle', 28: 'Charlie Halligan', 29: 'Oliver Ahearn', 30: 'Nick Enright', 31: 'Alan Behan', 39: 'Lisa Ahearn'}"

    """
    Test if file is ranking calculations are correct for invalid input format

    """
    def test_ranking_bad(self):

        assert rank_users("fake_customers.txt") == "{}"
