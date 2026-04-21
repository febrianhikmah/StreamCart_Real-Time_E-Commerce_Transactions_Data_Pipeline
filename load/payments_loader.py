from load.db import get_connection

def insert_payment(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO payments (
            payment_id, order_id, amount, method, status, paid_at
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (payment_id) DO NOTHING;
    """, (
        data["payment_id"],
        data["order_id"],
        data["amount"],
        data["method"],
        data["status"],
        data["paid_at"]
    ))

    conn.commit()
    cursor.close()
    conn.close()