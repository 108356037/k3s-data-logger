import os
import scipy.stats
import joblib
import time
import yaml
import json
import argparse
import utils.connect_mods as conn
import utils.payload_construct_mods as paystruct

parser = argparse.ArgumentParser()


parser.add_argument(
    "--customize", help="customize the port/host/topic of mqtt broker", type=bool)
parser.add_argument(
    "--topic", help="the topic to subscribe/publish to", type=str)
parser.add_argument(
    "--path", help="the path to subscribe/publish to", type=str)
parser.add_argument(
    "--host", help="mqtt broker ip", type=str)
parser.add_argument(
    "--port", help="the port to connect mqtt broker", type=str)
parser.add_argument(
    "--freq", help="the frequency you want to publish", type=str, default="5.0")
args = parser.parse_args()

with open('device_config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

mqttc = conn.mqtt_connack(**data['mqtt']['oringpaas'])

if args.customize:
    mqttc.username = None
    mqttc.userpw = None
    mqttc.host = args.host
    mqttc.port = int(args.port)
    mqttc.topic = args.topic
    mqttc.publish_path = args.path

mqttc.connect()
mqttc.client.loop_start()

while True:
    sim_data = {}
    cols = ['DO', 'BOD', 'SS', 'Nitrogen']
    for i in range(4):
        _kde = "./sim_kdes/kde"+str(i)+".pkl"
        kde = joblib.load(_kde)
        _data = kde.resample(1).T[:, 0]
        sim_data[cols[i]] = str(round(_data[0], 2))

    mqttc.payload_submit(json.dumps(
        {"id": "fullDataPackt", "value": str(sim_data)}))
    print(json.dumps({"id": "fullDataPackt", "value": str(sim_data)}))
    time.sleep(float(args.freq))
