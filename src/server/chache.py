from server_pb2_grpc import WebBackServicer, add_WebBackServicer_to_server
from server_pb2 import Confirmation
from concurrent.futures import ThreadPoolExecutor

import src.libs.models.actual_weather as contracts
import src.libs.models.weather_reader as saver

import grpc


class Service(WebBackServicer):
    def AddWeather(self, request, context):
        """
            Got tocken, id, weather
            Saving data
            return is succed saving
        """

        print("saved weather")
        return Confirmation(succed=True)


def execute_server():
    """
    Just run server :)
    """

    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_WebBackServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
