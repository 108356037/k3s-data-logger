import paho.mqtt.client as mqtt
import logging
import time

logging.basicConfig(level=logging.DEBUG)
logger =  logging.getLogger()

class connector_abc():

    def __init__(self,):
        """
        pass in a dict (load in yaml),
        connection detail should be in the yaml,
        ex: api token, publish path......
        """
        raise NotImplementedError

    def connect(self):
        """
        this func connects to the server
        """
        raise NotImplementedError

    def payload_submit(self, payload):
        """
        submit payload back to server depend on the protocol,
        mqtt: publish
        http: post
        """
        raise NotImplementedError      


class mqtt_connack(connector_abc):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.client = mqtt.Client(client_id = self.client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    def on_message(self, client, userdata, msg):
        print(f"received message payload from {msg.topic} \n")
        print(json.dumps(json.loads(msg.payload), indent=4, sort_keys=True))
        print("="*79)
        #return msg.payload.decode("utf-8")

    def on_publish(self, client, userdata, mid):
        print(f"userdata: {userdata}, mid: {mid}") 


    def connect(self):
        if self.username and self.userpw:
            self.client.username_pw_set(self.username, self.userpw)
        try:
            self.client.connect(self.host, self.port, self.keepalive)
            print(f"connect to {self.host}:{self.port}")
        except err as exception:
            print(err)

    def payload_submit(self, payload):
        path = self.topic['Data'] + self.publish_path['dataBucket']
        try:
            self.client.loop_start()
            res = self.client.publish(path,payload,qos=1)
            res.wait_for_publish()
            print(f"is published: {res.is_published()}")
        except Exception as err:
            print(err)