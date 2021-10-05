from concurrent import futures
import logging

import grpc
from random import randrange

import dc_net_pb2
import dc_net_pb2_grpc

#messageStatus = 0 stands for empty message

counter = 0
clients = [] 
clients = [0 for i in range(10)]




class Greeter(dc_net_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return dc_net_pb2.HelloReply(message='Hello Hello, %s!' % request.name)

    
    def SayHelloAgain(self, request, context):
        return dc_net_pb2.HelloReply(message='Hello again, %s!' % request.name)

    def ClientHello(self, request, context):
        return dc_net_pb2.HelloRequest(message='Hello I am the CLient, %s!' % request.message)
                
class Server_DCnet(dc_net_pb2_grpc.DC_roundServicer):

    def SendLocalSum(self, request, context):
        print("Hello")
        localSum = request.localSum
        print(localSum)
        if localSum == 4:
            return dc_net_pb2.Acknowlegde(MessageStatus=44)
        else:
            return dc_net_pb2.Acknowlegde(MessageStatus=1)
    
    #if dc_net_identifier and client identifier are 0 then the client is not in the dc_net and needs to be added.
    # dc_net_identifier and client identifier cant be zero
    def addClientToDCnet(self, request, context):
        if(request.dc_net_identifier != 0 or request.client_identifier != 0):
            #client is already in a dc_net
            print("addClientToDCnet already registered")
            return dc_net_pb2.Acknowlegde(MessageStatus=0)
        
        else:
            global counter
            global clients 
            print("addClientToDCnet registering")
            if(counter <10):
            #client wants to join dc_net
            # first client gets identifier 1 and second client gets identifier 2
                clients[counter] = counter +1
                counter = counter +1
            # this is implemented with only one dc_nets. if you want to run several dc_nets you need to implement a function for that.
                return dc_net_pb2.DC_net(dc_net_identifier=1,client_identifier=counter)
            else:
                # there can be only 10 clients in a dc net. if there are more than 10 decline request
                return dc_net_pb2.DC_net(dc_net_identifier=0,client_identifier=0)
    
    def connectDCClients(self, request, context):
        dc_netID=request.dc_net_identifier
        clientID=request.client_identifier
        print("in function connect")
        #get length of clients over the counter variable
        if(counter>1):
            random=randrange(1,counter+1)
            print(clients[random-1])
            print(random)
            if(clients[random-1] != clientID):
                    print(clients[random-1])
                    print(random)
                    return dc_net_pb2.DC_net(dc_net_identifier=dc_netID,client_identifier=random)
            else: 
                return dc_net_pb2.DC_net(dc_net_identifier=0,client_identifier=0)

            

        else:
            #if there is only one participant decline request, because there are no 2 clients that can be connected
            return dc_net_pb2.DC_net(dc_net_identifier=0,client_identifier=0)
            

        



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dc_net_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    dc_net_pb2_grpc.add_DC_roundServicer_to_server(Server_DCnet(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()