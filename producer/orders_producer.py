from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config.kafka_config import KAFKA_BROKER, TOPIC_ORDERS


# init producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# 🛍️ product catalog
PRODUCTS = [
    {"product_id": "PRD1", "name": "Laptop", "price": 8000000},
    {"product_id": "PRD2", "name": "Mouse", "price": 150000},
    {"product_id": "PRD3", "name": "Keyboard", "price": 300000},
    {"product_id": "PRD4", "name": "Headset", "price": 500000},
    {"product_id": "PRD5", "name": "Monitor", "price": 2000000},
]

def generate_order():
    product = random.choice(PRODUCTS)
    quantity = random.randint(1, 3)

    return {
        "event_type": "order_created",  # 🔥 penting buat event-driven
        "order_id": f"ORD{random.randint(1000,9999)}",
        "user_id": f"USR{random.randint(1,100)}",
        "product": {
            "product_id": product["product_id"],
            "name": product["name"],
            "price": product["price"]
        },
        "quantity": quantity,
        "total_amount": product["price"] * quantity,
        "payment_method": random.choice(["e-wallet", "bank_transfer", "cod"]),
        "status": "created",  # ✅ FIX (tidak random lagi)
        "created_at": datetime.now().isoformat()
    }
    

running = True
def run():
    global running
    while running:
        order = generate_order()
        producer.send(TOPIC_ORDERS, value=order)
        print(f"📨[ORDER CREATED] {order}")
        time.sleep(4)
