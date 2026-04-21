from orders_consumer import run as orders_run, running as orders_running
from payments_consumer import run as payments_run, running as payments_running
from shippings_consumer import run as shippings_run, running as shippings_running
import threading
import time
import orders_consumer
import payments_consumer
import shippings_consumer


threads = [
    threading.Thread(target=orders_run),
    threading.Thread(target=payments_run),
    threading.Thread(target=shippings_run)
]

try:
    print("🚀 Starting all consumers...\n")

    for t in threads:
        t.start()

    while True:
        time.sleep(2)  # keep main thread alive

except KeyboardInterrupt:
    print("\n🛑 Stopping all consumers...")

    # stop flag
    orders_consumer.running = False
    payments_consumer.running = False
    shippings_consumer.running = False

    for t in threads:
        t.join()

    print("✅ All consumers stopped gracefully")