from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config.kafka_config import KAFKA_BROKER, TOPIC_PAYMENTS

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

PAYMENT_METHODS = ["e-wallet", "bank_transfer", "credit_card", "cod"]
STATUS = ["pending", "completed", "failed"]

def generate_payment():
    return {
        "event_type": "payment_made",
        "payment_id": f"PAY{random.randint(1000,9999)}",
        "order_id": f"ORD{random.randint(1000,9999)}",  # dummy random order_id
        "amount": random.randint(100000, 5000000),
        "method": random.choice(PAYMENT_METHODS),
        "status": random.choice(STATUS),
        "paid_at": datetime.now().isoformat()
    }

running = True 
def run():
    global running
    while running:
        payment = generate_payment()
        producer.send(TOPIC_PAYMENTS, value=payment)
        print(f"📨[PAYMENT MADE] {payment}")
        time.sleep(4)