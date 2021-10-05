# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dc_net_pb2 as dc__net__pb2


class GreeterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/DCnetPackage.Greeter/SayHello',
                request_serializer=dc__net__pb2.HelloRequest.SerializeToString,
                response_deserializer=dc__net__pb2.HelloReply.FromString,
                )
        self.SayHelloAgain = channel.unary_unary(
                '/DCnetPackage.Greeter/SayHelloAgain',
                request_serializer=dc__net__pb2.HelloRequest.SerializeToString,
                response_deserializer=dc__net__pb2.HelloReply.FromString,
                )
        self.ClientHello = channel.unary_unary(
                '/DCnetPackage.Greeter/ClientHello',
                request_serializer=dc__net__pb2.HelloReply.SerializeToString,
                response_deserializer=dc__net__pb2.HelloReply.FromString,
                )


class GreeterServicer(object):
    """The greeting service definition.
    """

    def SayHello(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloAgain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClientHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=dc__net__pb2.HelloRequest.FromString,
                    response_serializer=dc__net__pb2.HelloReply.SerializeToString,
            ),
            'SayHelloAgain': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHelloAgain,
                    request_deserializer=dc__net__pb2.HelloRequest.FromString,
                    response_serializer=dc__net__pb2.HelloReply.SerializeToString,
            ),
            'ClientHello': grpc.unary_unary_rpc_method_handler(
                    servicer.ClientHello,
                    request_deserializer=dc__net__pb2.HelloReply.FromString,
                    response_serializer=dc__net__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DCnetPackage.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.
    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DCnetPackage.Greeter/SayHello',
            dc__net__pb2.HelloRequest.SerializeToString,
            dc__net__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHelloAgain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DCnetPackage.Greeter/SayHelloAgain',
            dc__net__pb2.HelloRequest.SerializeToString,
            dc__net__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClientHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DCnetPackage.Greeter/ClientHello',
            dc__net__pb2.HelloReply.SerializeToString,
            dc__net__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DC_roundStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendLocalSum = channel.unary_unary(
                '/DCnetPackage.DC_round/SendLocalSum',
                request_serializer=dc__net__pb2.DC_net.SerializeToString,
                response_deserializer=dc__net__pb2.Acknowlegde.FromString,
                )
        self.addClientToDCnet = channel.unary_unary(
                '/DCnetPackage.DC_round/addClientToDCnet',
                request_serializer=dc__net__pb2.DC_net.SerializeToString,
                response_deserializer=dc__net__pb2.DC_net.FromString,
                )
        self.connectDCClients = channel.unary_unary(
                '/DCnetPackage.DC_round/connectDCClients',
                request_serializer=dc__net__pb2.DC_net.SerializeToString,
                response_deserializer=dc__net__pb2.DC_net.FromString,
                )


class DC_roundServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendLocalSum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addClientToDCnet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def connectDCClients(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DC_roundServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendLocalSum': grpc.unary_unary_rpc_method_handler(
                    servicer.SendLocalSum,
                    request_deserializer=dc__net__pb2.DC_net.FromString,
                    response_serializer=dc__net__pb2.Acknowlegde.SerializeToString,
            ),
            'addClientToDCnet': grpc.unary_unary_rpc_method_handler(
                    servicer.addClientToDCnet,
                    request_deserializer=dc__net__pb2.DC_net.FromString,
                    response_serializer=dc__net__pb2.DC_net.SerializeToString,
            ),
            'connectDCClients': grpc.unary_unary_rpc_method_handler(
                    servicer.connectDCClients,
                    request_deserializer=dc__net__pb2.DC_net.FromString,
                    response_serializer=dc__net__pb2.DC_net.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DCnetPackage.DC_round', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DC_round(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendLocalSum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DCnetPackage.DC_round/SendLocalSum',
            dc__net__pb2.DC_net.SerializeToString,
            dc__net__pb2.Acknowlegde.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addClientToDCnet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DCnetPackage.DC_round/addClientToDCnet',
            dc__net__pb2.DC_net.SerializeToString,
            dc__net__pb2.DC_net.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def connectDCClients(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DCnetPackage.DC_round/connectDCClients',
            dc__net__pb2.DC_net.SerializeToString,
            dc__net__pb2.DC_net.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
