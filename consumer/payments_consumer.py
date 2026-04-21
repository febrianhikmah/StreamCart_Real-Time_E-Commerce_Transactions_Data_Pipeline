from kafka import KafkaConsumer
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from load.payments_loader import insert_payment
from config.kafka_config import KAFKA_BROKER, TOPIC_PAYMENTS

consumer = KafkaConsumer(
    TOPIC_PAYMENTS,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='payments-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def process_payment(data):
    print("\n📥 PAYMENTS DATA:")
    print(data)
    insert_payment(data)
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
            process_payment(data)
     
# buka ini jika ingin jalankan secara parsial            
# run()