# 🚀 STREAMCART: REAL-TIME E-COMMERCE DATA PIPELINE (KAFKA + POSTGRESQL)
## ✨ Gambaran Umum

Proyek ini merupakan implementasi real-time data pipeline yang mensimulasikan aliran transaksi pada sistem e-commerce.

Proyek ini berangkat dari pertanyaan:

>“Bagaimana cara memproses data transaksi e-commerce secara real-time dari berbagai event (order, payment, shipping) hingga tersimpan rapi di database?”

Untuk menjawabnya, saya membangun pipeline berbasis event streaming menggunakan Apache Kafka, yang mampu menangani aliran data secara asynchronous dan scalable.

Pipeline ini mencakup proses end-to-end mulai dari data generation, streaming, processing, hingga storage ke PostgreSQL.
---
## ⚙️ Gambaran Pipeline

Pipeline terdiri dari beberapa layer utama:

0. Config Layer

Mengelola seluruh konfigurasi sistem:

- Kafka (broker & topic)
- Database PostgreSQL
- Centralized configuration untuk memudahkan maintenance
---
1. Data Generation (Producer Layer)

Mensimulasikan data transaksi e-commerce secara real-time:

- ```orders_producer.py ``` → menghasilkan data order
- ```payments_producer.py ``` → menghasilkan data pembayaran
- ```shippings_producer.py ``` → menghasilkan data pengiriman

Semua data dikirim dalam format JSON.

---
2. Event Streaming (Kafka Layer)

Data dari producer dikirim ke Apache Kafka dengan pembagian topic:

- ```orders```
- ```payments```
- ```shippings```

Kafka bertindak sebagai message broker untuk:

- decoupling antar sistem
- handling high-throughput data
- real-time streaming
---
3. Data Consumption (Consumer Layer)

Consumer membaca data dari Kafka:

- ```orders_consumer.py```
- ```payments_consumer.py```
- ```shippings_consumer.py```

Proses yang dilakukan:

- menerima event
- deserialisasi JSON
- forwarding ke layer berikutnya
---
4. Processing Layer

Melakukan processing ringan terhadap data:

- validasi struktur data
- standardisasi format
- memastikan data siap untuk disimpan

---
5. Load Layer (Database Handler)

Data diproses dan dimuat ke database melalui loader:

- ```orders_loader.py```
- ```payments_loader.py```
- ```shippings_loader.py```

Menggunakan koneksi terpusat dari ```db.py.```
---
6. Storage Layer (PostgreSQL)

Data disimpan secara real-time ke dalam database:

Database: **E_Commerce**

📊 Tabel:

- ```orders```
- ```payments```
- ```shippings```

## 🧰 Teknologi yang Digunakan
| Layer           | Teknologi       |
|-----------------|-----------------|
| Orchestration   | Python          |
| Streaming       | Apache Kafka    |
| Data Format     | JSON            |
| Processing      | Python          |
| Database        | PostgreSQL      |
---
## 🗂️ Struktur Proyek
```pesta
config/
  kafka_config.py
  db_config.py

producer/
  orders_producer.py
  payments_producer.py
  shippings_producer.py
  run_producers.py

consumer/
  orders_consumer.py
  payments_consumer.py
  shippings_consumer.py
  run_consumer.py

load/
  db.py
  orders_loader.py
  payments_loader.py
  shippings_loader.py
```

---
## 🚀 Cara Kerja Sistem
1. Producer menghasilkan data transaksi secara real-time
2. Data dikirim ke Kafka berdasarkan jenis event
3. Consumer membaca data dari Kafka
4. Data diproses dan divalidasi
5. Data dimuat ke PostgreSQL
6. Data siap digunakan untuk analisis atau dashboard
---
## 📊 Hasil Output
- Data transaksi berhasil diproses secara real-time
- Event order, payment, dan shipping terpisah dengan jelas
- Data tersimpan langsung ke database tanpa delay signifikan
- Sistem mampu mensimulasikan aliran data e-commerce skala besar
---
## 💡 Insight & Nilai Proyek
- Implementasi nyata real-time data pipeline
- Penerapan event-driven architecture
- Penggunaan Kafka untuk streaming data skala besar
- Desain modular (producer, consumer, loader terpisah)
- Simulasi sistem e-commerce seperti di industri
---
## 🏁 Kesimpulan

Proyek ini menunjukkan bagaimana membangun sistem data pipeline modern yang mampu menangani data secara real-time menggunakan pendekatan event streaming.

Melalui proyek ini, saya memahami:

- Arsitektur event-driven system
- Cara kerja Apache Kafka dalam streaming data
- Pentingnya decoupling antar komponen sistem
- Pengelolaan pipeline data secara modular dan scalable












