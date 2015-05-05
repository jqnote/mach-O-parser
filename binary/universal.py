__author__ = 'rotlogix'

from ctypes import *
from binascii import unhexlify

from datetime import datetime
from enums.MachOEnums import Magic
from binary import macho
from utils.terminal import Colorize
c = Colorize()

"""

ctypes uses the native byte order (BigEndian | LittleEndian) for Structures and Unions.  To build structures
with non-native byte order, you can use on of the BigEndianStructure, LittleEndianStructure, etc.

Bit fields in structures and unions

It is possible to create structures and unions containing bit fields.  Bit fields are only possible for integer fields
, the width is specified as the third item in the _fields_ tuple

"""


class UniversalHeader(BigEndianStructure):

    """
    Create 'FAT' header structure from universal binary

    fat_header:

        - magic: Fixed value (0xCAFEBABE)
        - nfat_arch: Number of architectures present in the binary

    """

    _fields_ = [

        ('magic', c_uint),
        ('nfat_arch', c_uint)
    ]


class UniversalArch(BigEndianStructure):

    """
    Create 'FAT' architecture structure from universal binary

    fat_arch:

        - cputype: Cpu type <mach/machine.h>
        - cpusubtype: Machine specifier from <mach/machine.h>
        - offset: Offset of this architecture inside of the binary
        - size: Size of the inner binary
        - align: Alignment-Page boundary

    """

    _fields_ = [

        ('cputype', c_uint),
        ('cpusubtype', c_uint),
        ('offset', c_uint),
        ('size', c_uint),
        ('align', c_uint)
    ]


class UNIVERSAL(object):

    def __init__(self, binary):

        # Binary should already be a byte-array

        self.fat_header = None
        self.binary = binary
        self.binaries = list()

        if self.binary:
            # Create FAT header structure
            self.construct_fat()
        else:
            print(c.warning("[{0}] Binary was not loaded!".format(datetime.now())))

    def construct_fat(self):

        """
        Construct the FAT header and architecture sections
        """
        self.fat_header = UniversalHeader.from_buffer_copy(self.binary)

        # For each architecture listed in the universal binary
        print(c.logging("[{0}] Found ({1}) architectures".format(datetime.now(), self.fat_header.nfat_arch)))

        for archs in range(self.fat_header.nfat_arch):
            try:
                header = UniversalArch.from_buffer_copy(self.binary[8:])
                construct_binary = self.binary[header.offset:header.offset+header.size]
                if construct_binary[:4] == unhexlify(Magic.BIG_ENDIAN.value) or unhexlify(Magic.LITTLE_ENDIAN.value):
                    print(c.logging("[{0}] Successfully loaded architecture!".format(datetime.now())))
                    self.binaries.append(macho.MACHO(construct_binary))
            except Exception as e:
                # 04/30/2015
                # Need to figure out what exceptions will fire here
                raise e


