# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from grpc_server import trades_pb2


class FetcherServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FetchTrades = channel.unary_unary(
            "/fetcher.v1.FetcherService/FetchTrades",
            request_serializer=trades_pb2.FetchTradesRequest.SerializeToString,
            response_deserializer=trades_pb2.FetchTradesResponse.FromString,
        )
        self.StopFetchTrades = channel.unary_unary(
            "/fetcher.v1.FetcherService/StopFetchTrades",
            request_serializer=trades_pb2.Empty.SerializeToString,
            response_deserializer=trades_pb2.StopFetchTradesResponse.FromString,
        )


class FetcherServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FetchTrades(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StopFetchTrades(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_FetcherServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "FetchTrades": grpc.unary_unary_rpc_method_handler(
            servicer.FetchTrades,
            request_deserializer=trades_pb2.FetchTradesRequest.FromString,
            response_serializer=trades_pb2.FetchTradesResponse.SerializeToString,
        ),
        "StopFetchTrades": grpc.unary_unary_rpc_method_handler(
            servicer.StopFetchTrades,
            request_deserializer=trades_pb2.Empty.FromString,
            response_serializer=trades_pb2.StopFetchTradesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "fetcher.v1.FetcherService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class FetcherService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FetchTrades(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/fetcher.v1.FetcherService/FetchTrades",
            trades_pb2.FetchTradesRequest.SerializeToString,
            trades_pb2.FetchTradesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def StopFetchTrades(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/fetcher.v1.FetcherService/StopFetchTrades",
            trades_pb2.Empty.SerializeToString,
            trades_pb2.StopFetchTradesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
