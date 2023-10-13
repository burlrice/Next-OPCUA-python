import sys

from opcua import ua
from constants import Diagraph
from ij4k import ij4k

ipaddr = sys.argv[1]
printer = ij4k(ipaddr)
result = printer.callMethod(Diagraph.OPCUA.Methods.GetStatusInformation, ua.Variant(1, ua.VariantType.Int32))
error = result[0]

if len(error) == 0:
    print(result)
    print("State: {}".format(result[1]))
    print("Message: {}".format(result[2]))
    print("Line speed: {}".format(result[3]))
    print("Count: {}".format(str(result[4][0]).split(':')[1]))
    print("Consumable: {}".format(", ".join(result[5])))
    print("Errors: {}".format(", ".join(result[6])))
    print("Warnings: {}".format(", ".join(result[7])))
else:
    print("error: {}".format(error))
