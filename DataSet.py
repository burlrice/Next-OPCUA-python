import sys;
from lxml import etree

from constants import Diagraph
from ij4k import ij4k

printer = ij4k(sys.argv[1])

result = printer.callMethod(Diagraph.OPCUA.Methods.RecallMessage, "Database.next")
error = result[0]

if len(error) == 0:
    document = etree.fromstring(result[1], etree.XMLParser(recover=True))

    for i in document.xpath('//ProductObject//Variables//DataSet//ColumnValues//Column'):
        if 'Value' in i.attrib:
            print("{}: {}".format(i.attrib['Name'], i.attrib['Value']))
        else:
            print(i.attrib['Name'])
