from kafka import KafkaConsumer
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from load.shippings_loader import insert_shipping
from config.kafka_config import KAFKA_BROKER, TOPIC_SHIPPINGS

consumer = KafkaConsumer(
    TOPIC_SHIPPINGS,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='shippings-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def process_shipping(data):
    print("\n📥 SHIPPINGS DATA:")
    print(data)
    insert_shipping(data)
    print("\n📥 Data sudah masuk ke databases")
    
running = True

def run():
    global running

    print("🛒 Orders Consumer jalan...")

    while running:
        for message in consumer:
            if not running:
                break

            data = message.value

            process_shipping(data)

# buka ini jika ingin jalankan secara parsial
# run()