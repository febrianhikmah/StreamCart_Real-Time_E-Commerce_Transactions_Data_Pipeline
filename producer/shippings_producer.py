from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config.kafka_config import KAFKA_BROKER, TOPIC_SHIPPINGS

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

CARRIERS = ["JNE", "TIKI", "POS Indonesia", "Gojek", "Grab"]
STATUS = ["pending", "shipped", "delivered"]

def generate_shipping():
    return {
        "event_type": "shipment_created",
        "shipment_id": f"SHP{random.randint(1000,9999)}",
        "order_id": f"ORD{random.randint(1000,9999)}",  # dummy random order_id
        "carrier": random.choice(CARRIERS),
        "status": random.choice(STATUS),
        "shipped_at": datetime.now().isoformat()
    }

running = True
def run():
    global running
    while running:
        shipping = generate_shipping()
        producer.send(TOPIC_SHIPPINGS, value=shipping)
        print(f"📨[SHIPMENT CREATED] {shipping}")
        time.sleep(4)