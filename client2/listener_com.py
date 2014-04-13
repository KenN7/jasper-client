#/bin/python

import zmq

class Listen:
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect("ipc:///tmp/listener")
        self.socket.setsockopt(zmq.SUBSCRIBE, b'')

    def __iter__(self):
        while True:
            yield self.socket.recv_json()
