from __future__ import print_function
import logging

import grpc
import sys
import time, sched
from random import randrange
import random
import csv

import dc_net_pb2
import dc_net_pb2_grpc

neighboor = []
neighboor = [0 for i in range(10)]
#counter counts neighboors
counter = 0
dc_net_identifier = 0
client_identifier = 0
a = 0
Seeds = []
Seeds = [0 for i in range(10)]
rows = []
dataCounter = 1
plus = True

def ClientHello(self, request, context):
        return dc_net_pb2.HelloReply(message='Hello I am the CLient, %s!' % request.name)

def addClientToDCnet():
    if(dc_net_identifier == 0 & client_identifier == 0):
        return dc_net_pb2.DC_net(dc_net_identifier=0,client_identifier=0)

def getSecret(prime):
    return randrange(1,prime-1)

def getSeed():
    return randrange(1,100000)

def calculateOpenKey(prime,generator,random):
    return pow(generator, random, prime)

def getNeighboor(DC_stub):
    while(True):
            #counter counts the neighboors in a DC_net
            if(counter == 0):
                addNeighboor=DC_stub.connectDCClients(dc_net_pb2.DC_net(dc_net_identifier=dc_net_identifier,client_identifier=client_identifier))
                time.sleep(2)
                print("NeighboorID: ")
                print(addNeighboor)
                print(addNeighboor.dc_net_identifier)
                if(addNeighboor.dc_net_identifier != 0 or addNeighboor.client_identifier != 0):
                    print("in break")
                    return addNeighboor

def LookForNeighboorKey(DC_stub,last_neighboor,openKey):
    while(True):
            neighboorKey= DC_stub.ExchangeSecretForDH(dc_net_pb2.Secret(client_identifier=client_identifier,secret=openKey,neighboor=last_neighboor))
            if(neighboorKey.secret != 0):
                print("break")
                return neighboorKey
            time.sleep(2)

def calculatePrivateSessionKey(openKeyA,openKeyB,prime):
    return pow(openKeyA, openKeyB, prime)

def roundFunction(randomNumber):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    print(t.tm_sec)
    #synchronize the clients so that they send the function at the same time
    while((t.tm_sec % 10) != 9):
        t = time.localtime()
        #hier würde ich einmal pro sekunde schauen, ob ein neuer client sich registrieren möchte
        print("time " + str(t.tm_sec))
        time.sleep(1)

    return LocalSum(randomNumber)

def getElectricityData(n):

    if len(rows) == 0:
        file = open('csv/strom_2.csv')
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)

    tlist = list(zip(*rows))
    #get column of electricity consumption
    tlist=tlist[3]
    #return nte element of column. casted to int to remove plus sign.
    return int(tlist[n])

        
def LocalSum(randomNumber):
    #get actual electricity data from csv
    global dataCounter
    electricityConsumption=getElectricityData(dataCounter)
    print("electricityConsumption "+str(electricityConsumption))
    dataCounter = dataCounter + 1
    if(plus is True):
        return electricityConsumption + randomNumber
    else:
        return electricityConsumption - randomNumber


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
    neighboor[counter] = 0


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    global client_identifier
    global dc_net_identifier
    global counter
    global a
    global Seeds
    global plus
    with grpc.insecure_channel('localhost:50051') as channel:
        DC_stub = dc_net_pb2_grpc.DC_roundStub(channel)
        
        if(client_identifier == 0):
            print("addClient")
            request=DC_stub.addClientToDCnet(dc_net_pb2.DC_net(dc_net_identifier=dc_net_identifier,client_identifier=client_identifier))

        dc_net_identifier = request.dc_net_identifier
        client_identifier = request.client_identifier
        print("clientID: ")
        print(client_identifier)

        addNeighboor = getNeighboor(DC_stub)
        #save new neighboor
        neighboor.append(addNeighboor.client_identifier)
        counter = counter+1
        
        #get server prime and generator
        pg = DC_stub.getDiffieHellman(dc_net_pb2.Empty())

        print("pg.p " + str(pg.p))
        print("pg.g "+ str(pg.g))
        if(a is 0):
            a=getSecret(pg.p)

        openKey = calculateOpenKey(pg.p,pg.g,a)
        print("openKey")
        print(openKey)
        #give the last added neighboor into ExchangeSecretForDH
        #print("neighboor pop"+ str(neighboor.pop()))
        last_neighboor=neighboor[-1]
        print(last_neighboor)
       
        neighboorKey = LookForNeighboorKey(DC_stub,last_neighboor,openKey)
        
        print("neighboorKey "+ str(neighboorKey))
        print("key" + str(openKey))
        print("prime" + str(pg.p))
        sessionKey= calculatePrivateSessionKey(neighboorKey.secret,a,pg.p)
        print("sessionKey" + str(sessionKey))
        print("registered")

        seed=getSeed()
        encryptedSeed=seed ^ sessionKey
        print("encryptedseed" + str(encryptedSeed))
        print("seed")
        print(seed)
        
        while(True):
            exchangedSeed=DC_stub.ExchangePRNGSeed(dc_net_pb2.Seed(client_identifier=client_identifier,PRNGSeed=encryptedSeed,neighboor=last_neighboor))
            if(exchangedSeed.PRNGSeed != 0):
                decryptedSeed = exchangedSeed.PRNGSeed ^ sessionKey
                print("decryptedSeed" + str(decryptedSeed))
                print("seed" + str(seed))
                if(decryptedSeed == seed):
                    plus = False
                    print("seedBranch" + str(seed))
                    random.seed(seed)
                if((decryptedSeed != seed)):
                    plus = True
                    seed=decryptedSeed
                    print("decryptedSeed "+str(decryptedSeed))
                    random.seed(seed)
                print("exchangedSeedBreak")
                break
            time.sleep(2)
        
        print("exchangedSeed")
        print(seed)

        randomNumber = random.getrandbits(15)

        Seeds.append(last_neighboor)
        Seeds.append(seed)
        Seeds.append(randomNumber)
        Seeds.append(plus)

        print(randomNumber)
        #round function starts
        if(client_identifier != 0):
            print("roundFunction")
            while(True):
                for(i in Seeds):
                    
                localSum = roundFunction(randomNumber)
                t = str(time.localtime())
                print("localSum" + str(localSum))
                response=DC_stub.SendLocalSum(dc_net_pb2.DC_net(dc_net_identifier=dc_net_identifier, client_identifier=client_identifier, transmissionBit=1,timestamp=t,localSum=localSum))
                #nach neuem Partner suchen
                if(response is 1):
                    print("lookforneighboor")
                    newNeighboor = LookForNeighboorKey(DC_stub,0,openKey)
                print("localsum sended")
                randomNumber = random.getrandbits(15)
                print(randomNumber)
        
        
        
        

        
#dc_net_pb2.DC_net(dc_net_identifier=1,client_identifier=1,
          #  transmissionBit=1,timestamp='14 Uhr',notification=1,localSum=4)


if __name__ == '__main__':
    logging.basicConfig()
    init()
    run()