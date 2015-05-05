# mach-O-parser

This is my attempt to write a tool-set that would emulate the functionality of 'otool' in Python.

```
(mach-O-parser)┌[rotlogix@partygoblin] [/dev/ttys000]
└[~/Development/python/mach-O-parser]> python mach-0-parser.py NSUserDefaultsExample
[2015-05-05 16:39:13.113525] Loading Universal Binary: NSUserDefaultsExample
[2015-05-05 16:39:13.113659] Found (2) architectures
[2015-05-05 16:39:13.113790] Successfully loaded architecture!
---------------------------------------------------------------------------
Magic	CPU	CPU Subtype
-----	---	------------------
64	ARM	CPU_SUBTYPE_ARM_V7

[2015-05-05 16:39:13.113938] Successfully loaded architecture!
---------------------------------------------------------------------------
Magic	CPU	CPU Subtype
-----	---	------------------
```
