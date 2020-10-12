import machine
import json
import umqtt.simple as mqtt
from time import sleep, time
import rackspaceiot
import os

def read_pem(ext):
    for fname in filter(lambda x:x.endswith((ext)), fnames):
        with open(fname) as f:
            contents = f.read()
    return contents

# config
thing_id = 'team_name' #all lowercase, _ separator, no special chars
company_name = 'your_company_name'
endpoint = 'aws_iot_endpoint_dns_hostname'

publish_rate = 5 # seconds between publishing messages
fnames = os.listdir()
cert = read_pem('.crt')
key = read_pem('.key')
topic = "iotsample/%s/%s/data" % (company_name, thing_id)

client = mqtt.MQTTClient(thing_id,endpoint,ssl = True, ssl_params = {'key': key,'cert': cert})

while True:
    client.connect()
    '''
    data = {
        "thingId": thing_id,
        "time": time(),
        "temperature": foo,
        "humidity": bar,
        "light": baz
    }
    '''
    data = {'message': "Hello World from %s" % thing_id}

    client.publish(topic, json.dumps(data))
    print("published to topic %s: %s" % (topic, data))
    client.disconnect()
    sleep(publish_rate)