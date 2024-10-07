import asyncio
import os
from grpclib.server import Server
from schema.square import SquareBase, Number, Result

class SquareService(SquareBase):
    async def get_square(self, request: Number, context) -> Result:
        square = request.value ** 2
        print(f"SquareService: Received request for {request.value}. Returning {square}.")
        return Result(value=square)

async def serve():
    print("SquareServer: Starting...")

    server = Server([SquareService()])
    await server.start("[::]:50051")

    print("SquareServer: Server started at 50051.")
    await server.wait_closed()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    asyncio.run(serve())
