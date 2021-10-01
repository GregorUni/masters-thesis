from __future__ import print_function
import logging

import grpc

import dc_net_pb2
import dc_net_pb2_grpc

def ClientHello(self, request, context):
        return dc_net_pb2.HelloReply(message='Hello I am the CLient, %s!' % request.name)


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
        dc_request = DC_stub.SendLocalSum(dc_net_pb2.DC_net(dc_net_identifier=1,client_identifier=1,
            transmissionBit=1,timestamp='14 Uhr',notification=1,localSum=4))
        print(dc_request)
        
#dc_net_pb2.DC_net(dc_net_identifier=1,client_identifier=1,
          #  transmissionBit=1,timestamp='14 Uhr',notification=1,localSum=4)


if __name__ == '__main__':
    logging.basicConfig()
    run()