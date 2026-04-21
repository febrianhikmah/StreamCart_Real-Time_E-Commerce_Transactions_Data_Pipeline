from load.db import get_connection

def insert_order(data):
    conn = get_connection()
    cursor = conn.cursor()

    product = data["product"]

    cursor.execute("""
        INSERT INTO orders (
            order_id, user_id, product_id, product_name, product_price,
            quantity, total_amount, payment_method, status, created_at
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (order_id) DO NOTHING;
    """, (
        data["order_id"],
        data["user_id"],
        product["product_id"],
        product["name"],
        product["price"],
        data["quantity"],
        data["total_amount"],
        data["payment_method"],
        data["status"],
        data["created_at"]
    ))

    conn.commit()
    cursor.close()
    conn.close()

