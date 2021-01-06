import scipy.stats
import joblib
import time
import yaml
import json
import utils.connect_mods as conn
import utils.payload_construct_mods as paystruct

with open('device_config.yaml') as f:  
    data = yaml.load(f, Loader=yaml.FullLoader)


a = conn.mqtt_connack(**data['mqtt']['oringpaas'])
a.connect()
a.client.loop_start()

while True:
    sim_data = {}
    cols = ['DO', 'BOD', 'SS', 'Nitrogen']
    for i in range(4):
        _kde = "./sim_kdes/kde"+str(i)+".pkl"
        kde = joblib.load(_kde)
        _data = kde.resample(1).T[:,0]
        sim_data[cols[i]] = str(round(_data[0],2))
    
    a.payload_submit(json.dumps({"id":"fullDataPackt","value":str(sim_data)}))
    time.sleep(5.0)
