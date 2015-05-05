__author__ = 'rotlogix'

from ctypes import *
from utils.terminal import Colorize
c = Colorize()

from datetime import datetime
from enums.MachOEnums import Magic, Flags, ARM

"""
http://samhuri.net/posts/2010/01/basics-of-the-mach-o-file-format/
"""


class HEADER(Structure):

    """
    mach_header:

        - magic: 0xFEEDFACE or a 32-bit binary, 0xFEEDFACF for a 64-bit binary
        - cputype: CPU Type
        - filetype: FileType(Executable, Library, Core Dump, Kernel Extension)
        - ncmds:
        - sizeofcmds: Number and size of commands
        - flags: Flags reserved for the dynamic linker

    """

    _fields_ = [
        ('magic', c_uint),
        ('cputype', c_uint),
        ('cpusubtype', c_uint),
        ('filetype', c_uint),
        ('ncmds', c_uint),
        ('sizeofcmds', c_uint),
        ('flags', c_uint)
    ]


class MACHO(object):

    def __init__(self, binary):

        self.binary = binary
        self.macho_header = None
        self.magic = None
        self.cpu = None
        self.cpusubtype = None

        if binary:
            self.construct_macho()
            print(c.logging('-' * 75 + '\n' + 'Magic\tCPU\tCPU Subtype\n-----\t---\t------------------\n{0}\t{1}\t{2}\n'
                            .format(self.magic, self.cpu, self.cpusubtype)))
        else:
            print(c.warning("[{0}] Could not construct Mach-O binary!".format(datetime.now())))

    def construct_macho(self):

        """
        Construct the Mach-O binary
        """

        # Create Mach-0 header structure

        self.macho_header = HEADER.from_buffer_copy(self.binary)
        if self.macho_header:
            try:
                self.set_arch()
                self.set_cpu()
            except Exception as e:
                raise e

    def set_arch(self):

        """
        Set Architecture
        """

        if self.macho_header.magic == Magic.BIG_ENDIAN.value:
            self.magic = 32
        else:
            self.magic = 64

    def set_cpu(self):

        """
        Set CPU Type and CPU Subtype
        """

        if self.macho_header.cputype == Flags.CPU_ARM.value:
            self.cpu = 'ARM'
            # Set CPU Subtype
            for k, v in ARM.subtypes.items():
                if self.macho_header.cpusubtype == v:
                    self.cpusubtype = k
        elif self.macho_header.cputype == Flags.CPU_I386.value:
            self.cpu = 'X86'
        elif self.macho_header.cputype == Flags.CPU_64.value:
            self.cpu = 'X86-64'