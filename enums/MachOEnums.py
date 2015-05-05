__author__ = 'rotlogix'

from enum import Enum

"""
Common Enum types for mach-O-parser
"""


class Flags(Enum):

    CPU_I386 = 0x7
    CPU_64 = (CPU_I386 | 0x3)
    CPU_ARM = 12


class Magic(Enum):

    LITTLE_ENDIAN = b'cefaedfe'
    BIG_ENDIAN = b'feedface'


class ARM(object):

    """
    http://llvm.org/docs/doxygen/html/Support_2MachO_8h_source.html
    """

    subtypes = {

        'CPU_SUBTYPE_ARM_AL': 0,
        'CPU_SUBTYPE_ARM_V4T': 5,
        'CPU_SUBTYPE_ARM_V6': 6,
        'CPU_SUBTYPE_ARM_V5': 7,
        'CPU_SUBTYPE_ARM_V5TEJ': 7,
        'CPU_SUBTYPE_ARM_XSCALE': 8,
        'CPU_SUBTYPE_ARM_V7': 9,
        'CPU_SUBTYPE_ARM_V7S': 11,
        'CPU_SUBTYPE_ARM_V7K': 12,
        'CPU_SUBTYPE_ARM_V6M': 14,
        'CPU_SUBTYPE_ARM_V7M': 15,
        'CPU_SUBTYPE_ARM_V7EM': 16
    }