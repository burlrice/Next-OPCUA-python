import sys

from constants import Diagraph
from ij4k import ij4k

printer = ij4k(sys.argv[1])

result = printer.callMethod(Diagraph.OPCUA.Methods.GetStoredMessageList)
error = result[0]

if len(error) == 0:
    for i in result[1]:
        print(i)
else:
    print(error)
