import ubinascii
import machine
import json
import umqtt.simple as mqtt
from time import sleep
import rackspaceiot
import os

def read_pem(ext):
    for fname in filter(lambda x:x.endswith((ext)), fnames):
        with open(fname) as f:
            contents = f.read()
    return contents

fnames = os.listdir()
thingId = ubinascii.hexlify(machine.unique_id())
publish_rate = 5 # seconds between publishing messages
topic = 'rackspaceiot'
endpoint = 'REPLACE_WITH_YOUR_ENDPOINT'
cert = read_pem('.crt')
key = read_pem('.key')

client = mqtt.MQTTClient(thingId,endpoint,ssl = True, ssl_params = {'key': key,'cert': cert})

while True:
    client.connect()
    data = {'message': "Hello World from %s" % thingId}
    client.publish(topic, json.dumps(data))
    print("published to topic %s: %s" % (topic, data))
    client.disconnect()
    sleep(publish_rate) 