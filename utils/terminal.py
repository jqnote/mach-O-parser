__author__ = 'rotlogix'

from blessings import Terminal


class Colorize(object):

    """
    Colorize print statements based on functionality i.e. logging, warnings, errors
    """

    def __init__(self):
        self.T = Terminal()

    def logging(self, data):

        """
        Logging
        """
        return self.T.yellow(data)

    def warning(self, data):

        """
        Warning
        """
        return self.T.red(data)