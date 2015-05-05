__author__ = 'rotlogix'


if __name__ == '__main__':

    # 04/30/2015
    # Create suitable argument parser

    import sys
    from load import *
    from datetime import datetime

    # Terminal colors
    from utils.terminal import Colorize
    c = Colorize()

    try:
        if len(sys.argv) != 2:
            print(c.logging('[{0}] Usage: python mach-O-parser.py /path/to/binary'.format(datetime.now())))
            sys.exit(0)
        else:
            load = LOAD(sys.argv[1])
            load.check_type()
    except KeyboardInterrupt:
        print(c.logging('[{0}] CTRL+C'.format(datetime.now())))
    except Exception as e:
        print(c.warning('[{0}] Exception!'.format(datetime.now())))
        raise e