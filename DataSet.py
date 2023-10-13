import sys;

from datetime import datetime
from lxml import etree
from opcua import ua
from constants import Diagraph
from ij4k import ij4k

ipaddr =sys.argv[1]
messageName = sys.argv[2];

printer = ij4k(ipaddr)
result = printer.callMethod(Diagraph.OPCUA.Methods.RecallMessage, messageName)
error = result[0]

if len(error) == 0:
    document = etree.fromstring(result[1], etree.XMLParser(recover=True))

    for i in document.xpath('//ProductObject//Variables//DataSet//ColumnValues//Column'):
        if 'Value' in i.attrib:
            i.attrib['Value'] = "TODO {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            pass
        
    prd = etree.tostring(document, pretty_print=True, xml_declaration=True).decode()
    error = printer.callMethod(Diagraph.OPCUA.Methods.PrintPrd, ua.Variant(prd, ua.VariantType.String), ua.Variant(1, ua.VariantType.Int32))

    if len(error) > 0:
        print("{} failed with {}".format(Diagraph.OPCUA.Methods.PrintPrd), error)
