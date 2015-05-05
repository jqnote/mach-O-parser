__author__ = 'rotlogix'

from binascii import unhexlify
from datetime import datetime

# Import Colorize class from utils package
from utils.terminal import Colorize
c = Colorize()

from binary import universal


class LOAD(object):

    # 04/30/2015
    # Add Support for regular ole' Mach-O binaries

    def __init__(self, rawFile):
        self.rawFile = rawFile
        self.binary = None

        try:
            with open(self.rawFile, 'rb') as rf:
                self.binary = bytearray(rf.read())
                rf.close()
        except IOError:
            print(c.warning('[{0}] Unable to load binary!'.format(datetime.now())))

    def check_type(self):

        """
        Check binary type (Universal | Mach-O)
        """

        # Check for binary type: (Universal | Mach-O)
        if self.binary[:4] == unhexlify(b'cafebabe'):
            print(c.logging('[{0}] Loading Universal Binary: {1}'.format(datetime.now(), self.rawFile)))
            universal.UNIVERSAL(self.binary)