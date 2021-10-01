from addressbook_pb2 import DESCRIPTOR
import dc_net_pb2
import sys

def TestFillingOfFieds(DC_net):
  DC_net.dc_net_identifier = int(input("Enter your DC_net ID number: "))
  DC_net.client_identifier = int(input("Enter your DC_net Client ID: "))
  DC_net.timestamp = input("Enter the Time: ")
  DC_net.localSum = int(input("Enter your localSum: "))


#Main procedure

#if len(sys.argv) != 2:
    
#  sys.exit(-1)

DC_net = dc_net_pb2.DC_net()

TestFillingOfFieds(DC_net)
print("DC_net Identifier",DC_net.dc_net_identifier)
print("DC_net Client Identifier", DC_net.client_identifier)

