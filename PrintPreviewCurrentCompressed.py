import sys
import lzma
import zlib

from opcua import ua
from constants import Diagraph
from ij4k import ij4k

ipaddr = sys.argv[1]
filename = sys.argv[2]
printer = ij4k(ipaddr)
result = printer.callMethod(Diagraph.OPCUA.Methods.PrintPreviewCurrentCompressed, ua.Variant(1, ua.VariantType.Int32))
error = result[0]

if len(error) == 0:
    compressed = bytes(result[2]);
    decompressed = zlib.decompress(compressed, bufsize=result[1])    

    with open(filename, "wb") as file:
        file.write(decompressed)
        
else:
    print("error: {}".format(error))

