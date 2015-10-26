#!/usr/bin/env python
#
# Load a system.map file (generated by 'nm')
# so that you can play with symbols
#
import sys

from ramooflax.core   import VM, CPUFamily, log
from ramooflax.utils  import SymTab, SymParser

##
## Main
##
if len(sys.argv) < 2:
    print "give me 'system.map"
    sys.exit(1)

peer = "172.16.131.128:1337"
vm = VM(CPUFamily.Intel, peer)

log.setup(info=True, fail=True,
          gdb=False, vm=True,
          brk=True,  evt=False)

# load kernel symbols
vm.symbols = SymTab(SymParser().from_system_map(sys.argv[1]))

vm.attach()
vm.stop()

print vm.symbols[vm.cpu.code_location()]

log("info", "ready!")
vm.interact2(dict(globals(), **locals()))
