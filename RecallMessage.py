import sys;

from constants import Diagraph
from ij4k import ij4k

printer = ij4k(sys.argv[1])

result = printer.callMethod(Diagraph.OPCUA.Methods.RecallMessage, "Database.next")
error = result[0]

if len(error) == 0:
    print(result[1])
else:
    print(error)