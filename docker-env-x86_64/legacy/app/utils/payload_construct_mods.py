import datetime

import paho.mqtt.client as mqtt


class payload_constructer_abc():

    def __init__(self):
        self.payload = {}


    def provide_timestamp(self):
        ISOTIMEFORMAT = '%Y/%m/%d %H:%M:%S'
        t = datetime.datetime.now().strftime(ISOTIMEFORMAT)
        return t

    def construct_payload(self):
        pass


class container_checker(payload_constructer_abc):

    def __init__(self, **kwargs):
        super().__init__()
        self.payload.update(kwargs)

    def construct_payload(self):
        self.payload['value']['timestamp'] = self.provide_timestamp()

    def stringfy_value(self):
        buffer = (self.payload['value']).copy()
        self.payload['value'] = str(buffer)
