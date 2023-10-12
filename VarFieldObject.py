import sys

from xml.dom import expatbuilder

filename = sys.argv[1]
find = sys.argv[2]
replace = sys.argv[3]

document = expatbuilder.parse(filename, False)

for i in document.getElementsByTagName('FieldObject'):
    if (i.attributes["xsi:type"].value == 'VarFieldObject') and i.attributes['Data'].value == find:
        i.attributes['Data'].value = replace
        
with open(filename, "w") as file:
    file.write(document.toxml())