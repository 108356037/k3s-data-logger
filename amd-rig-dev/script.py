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
    "--host", help="mqtt broker ip", type=str)
parser.add_argument(
    "--port", help="mqtt broker port", type=str)
parser.add_argument(
    "--topic", help="the topic to subscribe/publish to", type=str)
parser.add_argument(
    "--path", help="the path to subscribe/publish to", type=str)
parser.add_argument(
    "--client_id", help="mqtt client id, if not given, will generate a random one", type=str)
parser.add_argument(
    "--username", help="mqtt client username", type=str)
parser.add_argument(
    "--userpw", help="mqtt client user password", type=str)
parser.add_argument(
    "--freq", help="the frequency you want to publish", type=str, default="1.0")

args = parser.parse_args()

mqttc = conn.mqtt_connack_noyaml(args.host, int(args.port), args.topic, args.path, args.client_id, args.username, args.userpw)
mqttc.init_mqttc()
mqttc.connect()
mqttc.client.loop_start()

print(args.topic)

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
