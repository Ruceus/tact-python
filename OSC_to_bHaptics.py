from time import sleep
from bhaptics import better_haptic_player as player
from bhaptics.better_haptic_player import BhapticsPosition
from pythonosc.dispatcher import Dispatcher
from typing import List
import asyncio
from pythonosc.osc_server import AsyncIOOSCUDPServer

class OSC_To_bHaptics:

    def __init__(self, ip, port, loopPauseInterval, bHapticsSuiteActivationDurationMillis):
        print('init OSC to bHaptics instance...')
        self.ip = ip
        self.port = port
        self.loopPauseInterval = loopPauseInterval
        self.bHapticsActivationDurationMillis = bHapticsSuiteActivationDurationMillis

        # create variables for received values
        # self.example_max_front = [50,50,50,50,50,50,50,50,100,100,100,100,100,100,100,100,20,20,20,20]
        # self.example_max_back = [20,20,20,20,100,100,100,100,20,20,20,20,50,50,50,50,100,100,100,100]

        # store values sent from max
        self.max_front = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.max_back = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # create coordinates to address the vest matrix correctly
        self.x = [0.0, 0.33, 0.66, 1.0, 0.0, 0.33, 0.66, 1.0, 0.0, 0.33, 0.66, 1.0, 0.0, 0.33, 0.66, 1.0, 0.0, 0.33, 0.66, 1.0]
        self.y = [0.0, 0.0, 0.0, 0.0, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.75, 0.75, 0.75, 0.75, 1, 1, 1, 1]

        # init bhaptics player connection
        print('initializing player')
        player.initialize()
        
        # configure dispatcher
        print('configuring dispatcher')
        self.dispatcher = Dispatcher()
        self.dispatcher.map("/max_front", self.set_max_front)
        self.dispatcher.map("/max_back", self.set_max_back)

        asyncio.run(self.init_main())


    #
    def set_max_front(self, address: str, *osc_arguments: List):
        self.max_front = list(osc_arguments)
        print("Set max_front: " + str(self.max_front))
        for i in range(20):
            self.max_front[i] = int(self.max_front[i] * 100)


    #
    def set_max_back(self, address: str, *osc_arguments: List):
        self.max_back = list(osc_arguments)
        print("Set max_back: " + str(self.max_back))
        for i in range(20):
            self.max_back[i] = int(self.max_back[i] * 100)


    #
    async def loop(self):
        print('in loop...')
        while True:
            print(str(self.max_front) + '; '+ str(self.max_back))

            player.submit_path("frontFramePath", BhapticsPosition.VestFront.value, [
                {"x": self.x[0], "y": self.y[0], "intensity": self.max_front[0]},
                {"x": self.x[1], "y": self.y[1], "intensity": self.max_front[1]},
                {"x": self.x[2], "y": self.y[2], "intensity": self.max_front[2]},
                {"x": self.x[3], "y": self.y[3], "intensity": self.max_front[3]},
                {"x": self.x[4], "y": self.y[4], "intensity": self.max_front[4]},
                {"x": self.x[5], "y": self.y[5], "intensity": self.max_front[5]},
                {"x": self.x[6], "y": self.y[6], "intensity": self.max_front[6]},
                {"x": self.x[7], "y": self.y[7], "intensity": self.max_front[7]},
                {"x": self.x[8], "y": self.y[8], "intensity": self.max_front[8]},
                {"x": self.x[9], "y": self.y[9], "intensity": self.max_front[9]},
                {"x": self.x[10], "y": self.y[10], "intensity": self.max_front[10]},
                {"x": self.x[11], "y": self.y[11], "intensity": self.max_front[11]},
                {"x": self.x[12], "y": self.y[12], "intensity": self.max_front[12]},
                {"x": self.x[13], "y": self.y[13], "intensity": self.max_front[13]},
                {"x": self.x[14], "y": self.y[14], "intensity": self.max_front[14]},
                {"x": self.x[15], "y": self.y[15], "intensity": self.max_front[15]},
                {"x": self.x[16], "y": self.y[16], "intensity": self.max_front[16]},
                {"x": self.x[17], "y": self.y[17], "intensity": self.max_front[17]},
                {"x": self.x[18], "y": self.y[18], "intensity": self.max_front[18]},
                ],
                self.bHapticsActivationDurationMillis)
            
            player.submit_path("backFramePath", BhapticsPosition.VestBack.value, [
                {"x": self.x[0], "y": self.y[0], "intensity": self.max_back[0]},
                {"x": self.x[1], "y": self.y[1], "intensity": self.max_back[1]},
                {"x": self.x[2], "y": self.y[2], "intensity": self.max_back[2]},
                {"x": self.x[3], "y": self.y[3], "intensity": self.max_back[3]},
                {"x": self.x[4], "y": self.y[4], "intensity": self.max_back[4]},
                {"x": self.x[5], "y": self.y[5], "intensity": self.max_back[5]},
                {"x": self.x[6], "y": self.y[6], "intensity": self.max_back[6]},
                {"x": self.x[7], "y": self.y[7], "intensity": self.max_back[7]},
                {"x": self.x[8], "y": self.y[8], "intensity": self.max_back[8]},
                {"x": self.x[9], "y": self.y[9], "intensity": self.max_back[9]},
                {"x": self.x[10], "y": self.y[10], "intensity": self.max_back[10]},
                {"x": self.x[11], "y": self.y[11], "intensity": self.max_back[11]},
                {"x": self.x[12], "y": self.y[12], "intensity": self.max_back[12]},
                {"x": self.x[13], "y": self.y[13], "intensity": self.max_back[13]},
                {"x": self.x[14], "y": self.y[14], "intensity": self.max_back[14]},
                {"x": self.x[15], "y": self.y[15], "intensity": self.max_back[15]},
                {"x": self.x[16], "y": self.y[16], "intensity": self.max_back[16]},
                {"x": self.x[17], "y": self.y[17], "intensity": self.max_back[17]},
                {"x": self.x[18], "y": self.y[18], "intensity": self.max_back[18]},
            ],
            self.bHapticsActivationDurationMillis)

            await asyncio.sleep(self.loopPauseInterval)


    async def init_main(self):
        print('connecting to UDP server with ip: {ip} listening on port {port}')
        server = AsyncIOOSCUDPServer((self.ip, self.port), self.dispatcher, asyncio.get_event_loop())
        transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving
        await self.loop()  # Enter main loop of program

        print('loop ended, closing.')
        transport.close()  # Clean up serve endpoint
# END OF CLASS


instance = OSC_To_bHaptics("127.0.0.1", 8002, 0.05, 100)