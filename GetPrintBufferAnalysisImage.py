import sys
import lzma
import zlib

from opcua import ua
from constants import Diagraph
from ij4k import ij4k

ipaddr = sys.argv[1]
filename = sys.argv[2]
printer = ij4k(ipaddr)
result = printer.callMethod(
    Diagraph.OPCUA.Methods.GetPrintBufferAnalysisImageCompressed, 
    ua.Variant("", ua.VariantType.String), 
    ua.Variant(filename, ua.VariantType.String))
error = result[0]

if error == 0:
    compressed = bytes(result[2]);
    decompressed = zlib.decompress(compressed, bufsize=result[1])    

    with open(filename + ".PrintBufferAnalysis.bmp", "wb") as file:
        file.write(decompressed)
        
else:
    print("error: {}".format(error))

