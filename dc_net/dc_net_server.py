from concurrent import futures
import logging

import grpc
import random, time
from random import randrange
from operator import ixor

import dc_net_pb2
import dc_net_pb2_grpc

#messageStatus = 0 stands for empty message

counter = 0
clients = [] 
p = 0
g = 0
post = []
post = [0 for i in range(5)]
exchangeSeed = []
exchangeSeed = [0 for i in range(2)]
localSums = []
globalSums = []
dictionary = {}
transmissionBitCounter = 0
removed = 0



class Greeter(dc_net_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return dc_net_pb2.HelloReply(message='Hello Hello, %s!' % request.name)

    
    def SayHelloAgain(self, request, context):
        return dc_net_pb2.HelloReply(message='Hello again, %s!' % request.name)

    def ClientHello(self, request, context):
        return dc_net_pb2.HelloRequest(message='Hello I am the CLient, %s!' % request.message)

#stole it from https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True    

def initList(n):
    return [0 for i in range(n)]


                
class Server_DCnet(dc_net_pb2_grpc.DC_roundServicer):

    def SendLocalSum(self, request, context):
        global dictionary
        global counter
        global clients
        global transmissionBitCounter
        #transmissionBitCounter=0
        global removed
        removed = 0
        clientID = request.client_identifier
        localSum = request.localSum
        localSums.append(localSum)
        #transmissionBit=request.transmissionBit

        #transmissionBitCounter = transmissionBitCounter + transmissionBit
        dictionary[clientID] = True
        time.sleep(1)
        print("transmissionBiCounter "+str(transmissionBitCounter))
        print("dictionary" +str(dictionary))
        print(not all(value == True for value in dictionary.values()))
        if(not all(value == True for value in dictionary.values())):
            globalSum = sum(localSums)
            print("globalSum "+ str(globalSum))
            globalSums.append(globalSum)
            localSums.clear()
            for key in dictionary.copy():
                #this code is only triggered if one client doesnt send his local sum in a round
                #hence its deleted
                if dictionary[key] == False:
                    print("DELEEEEEETTTTTIIIIIIIIINNNNNNNNNGGGGGGGG" + str(key))
                    print("clients" +str(clients))
                    clients.remove(key)
                    print(len(clients))
                    counter = counter - 1
                    #send clientId (which is going to be deleted) to clients
                    print("deleting "+ str(key))
                    dictionary.pop(key) 
                    #if(all(value == True for value in dictionary.values())):
                    #    print("ich war hier")
                    #for i in dictionary.copy():
                    #    dictionary[i] = False  
                    print("dictionary"+str(dictionary))
                    print("key "+str(key))
                    removed = key
                    print("removed " +str(removed))

        time.sleep(1)
        if(all(value == True for value in dictionary.values())):
            print("ich war hier")
            for key in dictionary:
                dictionary[key] = False    

        if removed > 0:
            print("returned")
            return dc_net_pb2.Acknowlegde(MessageStatus=removed)

        print(str(dictionary[clientID]))
        print("localsum" + str(localSum))
        print("")
        print("counter "+ str(counter))
        print(len(localSums))
        if(len(localSums) is counter):
            
            globalSum = sum(localSums)
            print("globalSum "+ str(globalSum))
            globalSums.append(globalSum)
            localSums.clear()

            

        #if a new client wants to exchange Seeds notify neigboor
        print("client_identifier"+str(request.client_identifier))
        print("post[0] "+ str(post[0]))
        if(post[0] is request.client_identifier):
            print("1 is sended")
            return dc_net_pb2.Acknowlegde(MessageStatus=9999)
        return dc_net_pb2.Acknowlegde(MessageStatus=0)        


    def updateGlobalSum(self, request, context):
        clientID = request.client_identifier
        localSum = request.localSum

        lastGlobalSum = globalSums.pop()
        print("errorGlobalSum" + str(lastGlobalSum))
        
        lastGlobalSum = lastGlobalSum + localSum
        globalSums.append(lastGlobalSum)
        print("lastGlobalSum" + str(lastGlobalSum))

        return dc_net_pb2.Acknowlegde(MessageStatus=0)  

    #if dc_net_identifier and client identifier are 0 then the client is not in the dc_net and needs to be added.
    # dc_net_identifier and client identifier cant be zero
    def addClientToDCnet(self, request, context):
        if(request.dc_net_identifier != 0 or request.client_identifier != 0):
            #client is already in a dc_net
            print("addClientToDCnet already registered")
            return dc_net_pb2.Acknowlegde(MessageStatus=0)
        
        else:
            global clients 
            print("addClientToDCnet registering")
            if(len(clients) <10):
            #client wants to join dc_net
            # first client gets identifier 1 and second client gets identifier 2
                length = len(clients)+1
                print("lengtH"+str(length))
                clients.append(length)
            # this is implemented with only one dc_nets. if you want to run several dc_nets you need to implement a function for that.
                return dc_net_pb2.DC_net(dc_net_identifier=1,client_identifier=length)
            else:
                # there can be only 10 clients in a dc net. if there are more than 10 decline request
                return dc_net_pb2.DC_net(dc_net_identifier=0,client_identifier=0)
    
    def connectDCClients(self, request, context):
        dc_netID=request.dc_net_identifier
        clientID=request.client_identifier
        print("in function connect")
        #check if there are at least 2 clients in the dc_net
        if(len(clients)>1):
            #give client a random neighboor
            #print("len(clients)+1")
            print("CLIIIIIIIIIIIENNNTS"+str(clients))
            print(len(clients)+1)
            random=randrange(1,len(clients)+1)
            #print("random "+ str(random))
            #print(clients[random-1])
            #print(random)
            if(random != clientID):
                    #print("clients[random] ")
                    #print(clients[random-1])
                    #print(random)
                    #random is a new neighboor which is assigned randomly
                    return dc_net_pb2.DC_net(dc_net_identifier=dc_netID,client_identifier=random)
            else: 
                return dc_net_pb2.DC_net(dc_net_identifier=0,client_identifier=0)

            

        else:
            #if there is only one participant decline request, because there are no 2 clients that can be connected
            return dc_net_pb2.DC_net(dc_net_identifier=0,client_identifier=0)
    
    def getDiffieHellman(self, request, context):
        global p
        global g
        print("getDiffieHellman")
        #configure a public g and p
        if(p == 0 or g == 0):
            primes = [i for i in range(80000,100000) if is_prime(i)]
            p = random.choice(primes)
            #just a static number smaller than primes
            g = 42843
        return dc_net_pb2.DiffieHelman(p=p,g=g)

    def sync(self, request, context):
        t=time.localtime()
        print(t)

    def ExchangeSecretForDH(self, request, context):
        global post
        print("ExchangeSecretForDH")
        clientID = request.client_identifier
        openkey = request.secret
        neighboor = request.neighboor

        if(post[0] is 0):
            post[0] = neighboor
            #print("post[0]" + str(post[0]))
            post[1] = clientID
            post[2] = openkey
            #print("post[1]" + str(post[1]))
            return dc_net_pb2.Secret(secret=0)
            
        if((post[3] is 0) and clientID is post[0]):
            post[3] = clientID
            #print("post[2]" + str(post[2]))
            post[4] = openkey
            #print("post[3]" + str(post[3]))
            return dc_net_pb2.Secret(secret=post[2],client_identifier=post[1])

        if(neighboor == post[3]):  
            secret=post[4]
            post = initList(5)
            return dc_net_pb2.Secret(secret=secret)  

        else:
            #print("else:")
            return dc_net_pb2.Secret(secret=0)


    
        #if(post[0] is 0):
        #    post[0] = clientID
        #    print("post[0]" + str(post[0]))
        #    post[1] = openkey
        #    print("post[1]" + str(post[1]))
        #    return dc_net_pb2.Secret(secret=0)
            
        #if((post[2] is 0) and neighboor is post[0]):
        #    post[2] = clientID
        #    print("post[2]" + str(post[2]))
        #    post[3] = openkey
        #    print("post[3]" + str(post[3]))
        #    return dc_net_pb2.Secret(secret=post[1])

        #if(neighboor == post[2]):  
        #    secret=post[3]
        #    post = initList(4)
        #    return dc_net_pb2.Secret(secret=secret)  

        #else:
        #    print("else:")
        #    return dc_net_pb2.Secret(secret=0)        
    
    def ExchangePRNGSeed(self, request, context):
        global exchangeSeed
        global counter
        print("ExchangePRNGSeed")
        seed = request.PRNGSeed
        neighboor = request.neighboor
        #print("seed" +str(seed))
        #print("neighboor"+str(neighboor))
        #print("seed[0]"+ str(exchangeSeed[0]))
        client=request.client_identifier
        if(exchangeSeed[0] is 0):
            exchangeSeed[0] = client
            exchangeSeed[1] = seed
            return dc_net_pb2.Seed(PRNGSeed=exchangeSeed[1])
        if(exchangeSeed[0] == neighboor):
            returnseed=exchangeSeed[1]
            exchangeSeed = initList(2)
            #increment user counter since a user is now "fully" registered
            if(counter == 0):
                counter = counter + 2
            else:
                counter = counter+1
            return dc_net_pb2.Seed(PRNGSeed=returnseed)
        else:
            return dc_net_pb2.Seed(PRNGSeed=0)
        


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dc_net_pb2_grpc.add_DC_roundServicer_to_server(Server_DCnet(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()