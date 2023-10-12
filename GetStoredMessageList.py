import sys

from opcua import Client
from constants import Diagraph

client = Client("opc.tcp://{}:{}".format(sys.argv[1], Diagraph.OPCUA.Port))
client.connect()

method = client.get_node("{};s={}".format(Diagraph.OPCUA.Namespace, Diagraph.OPCUA.Methods.GetStoredMessageList))
node = client.get_node(Diagraph.OPCUA.ObjectId)
result = node.call_method(method)
error = result[0]

if len(error) == 0:
    for i in result[1]:
        print(i)
else:
    print(error)

client.disconnect()

