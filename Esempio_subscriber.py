import paho.mqtt.client as mqtt_client

def on_connect(client, userdata, flags, rc, properties):
  print('Connected. result code = '+str(rc))

def on_message(client, userdata, msg):
  print(msg.topic +' '+msg.payload.decode('utf-8'))

client =mqtt_client.Client(client_id="2",callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(host='127.0.0.1', port=1884)
client.subscribe('ifts/axel/esempio/1')
client.loop_forever()