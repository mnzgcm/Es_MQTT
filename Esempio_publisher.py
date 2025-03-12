import paho.mqtt.client as mqtt_client
import time

def on_connect(client, userdata, flags, rc, properties):
  print('Connected. result code = '+str(rc))

client =mqtt_client.Client(client_id="1",callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.connect(host='127.0.0.1', port=1884)
client.loop_start()
msg = str.encode('prova1', 'utf-8')
while(True):
  client.publish('ifts/axel/esempio/1', msg)
  time.sleep(1)