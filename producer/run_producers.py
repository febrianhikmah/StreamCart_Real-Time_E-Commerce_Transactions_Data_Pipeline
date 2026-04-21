from orders_producer import run as orders_run, running as orders_running
from payments_producer import run as payments_run, running as payments_running
from shippings_producer import run as shippings_run, running as shippings_running
import threading
import time
import orders_producer
import payments_producer
import shippings_producer

threads = [
    threading.Thread(target=orders_run),
    threading.Thread(target=payments_run),
    threading.Thread(target=shippings_run)
]

try:
    for t in threads:
        t.start()
    while True:
        time.sleep(2)  # main thread tetap alive
except KeyboardInterrupt:
    print("\n[*] Stopping all producers...")
    # ubah flag jadi False supaya loop berhenti
    orders_producer.running = False
    payments_producer.running = False
    shippings_producer.running = False

    for t in threads:
        t.join()  # tunggu semua thread berhenti
    print("[*] All stopped gracefully")