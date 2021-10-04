from __future__ import print_function
import logging

import grpc
import sys

import dc_net_pb2
import dc_net_pb2_grpc



def ClientHello(self, request, context):
        return dc_net_pb2.HelloReply(message='Hello I am the CLient, %s!' % request.name)

def addClientToDCnet():
    if(dc_net_identifier == 0 & client_identifier == 0):
        return dc_net_pb2.DC_net(dc_net_identifier=0,client_identifier=0)


def init():
    ####setting all values in the DC_net message to zero.
    #then asking the server automatically to join the dc_net
    global dc_net_identifier
    global client_identifier
    dc_net_identifier = 0
    client_identifier = 0
    transmissionBit = 0
    timestamp = 0
    notification = 0
    localSum = 0


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = dc_net_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(dc_net_pb2.HelloRequest(name='you'))
        print("Greeter client received: " + response.message)
        #response = stub.SayHelloAgain(dc_net_pb2.HelloRequest(name='you'))
        #print("Greeter client received: " + response.message)
        #request = stub.ClientHello(dc_net_pb2.HelloReply(message='hi'))
        #print(request.message)
        DC_stub = dc_net_pb2_grpc.DC_roundStub(channel)
        #dc_request = DC_stub.SendLocalSum(dc_net_pb2.DC_net(dc_net_identifier=1,client_identifier=1,
            #transmissionBit=1,timestamp='14 Uhr',notification=1,localSum=4))
        #print(dc_request)
        request=DC_stub.addClientToDCnet(dc_net_pb2.DC_net(dc_net_identifier=0,client_identifier=0))
        if(request.client_identifier == 0):
            sys.exit(-1)

        dc_net_identifier = request.dc_net_identifier
        client_identifier = request.client_identifier
        print(dc_net_identifier)
        print(client_identifier)

        
#dc_net_pb2.DC_net(dc_net_identifier=1,client_identifier=1,
          #  transmissionBit=1,timestamp='14 Uhr',notification=1,localSum=4)


if __name__ == '__main__':
    logging.basicConfig()
    init()
    run()