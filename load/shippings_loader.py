from load.db import get_connection

def insert_shipping(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO shippings (
            shipment_id, order_id, carrier, status, shipped_at
        )
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (shipment_id) DO NOTHING;
    """, (
        data["shipment_id"],
        data["order_id"],
        data["carrier"],
        data["status"],
        data["shipped_at"]
    ))

    conn.commit()
    cursor.close()
    conn.close()