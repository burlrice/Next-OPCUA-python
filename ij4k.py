from opcua import Client
from constants import Diagraph

class ij4k:
    def __init__ (self, ipaddr):
        self.client = Client("opc.tcp://{}:{}".format(ipaddr, Diagraph.OPCUA.Port))
        self.client.connect()
        
    def __del(self):
        self.client.disconnect()

    def callMethod(self, methodName, *args):
        method = self.client.get_node("{};s={}".format(Diagraph.OPCUA.Namespace, methodName))
        node = self.client.get_node(Diagraph.OPCUA.ObjectId)
        
        if (len(args) == 0):
            return node.call_method(method)
        else:
            return node.call_method(method, *args)
        