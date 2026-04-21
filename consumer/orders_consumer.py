from kafka import KafkaConsumer
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from load.orders_loader import insert_order
from config.kafka_config import KAFKA_BROKER, TOPIC_ORDERS

consumer = KafkaConsumer(
    TOPIC_ORDERS,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='orders-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def process_order(data):
    print("\n📥 ORDER DATA:")
    print(data)
    insert_order(data)
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
            process_order(data)
            
# buka ini jika ingin jalankan secara parsial
# run()