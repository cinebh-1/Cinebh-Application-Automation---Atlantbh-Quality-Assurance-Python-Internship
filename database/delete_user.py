# import psycopg2
# class DBConnector:
#     def delete_user(user_email):
#         global conn, cursor
#         try:
#             conn = psycopg2.connect(
#                 host="127.0.0.1",
#                 database="cinebh_db",
#                 user="cinebh_user",
#                 password="cinebh123",
#                 port="5432"
#         )
#             conn.autocommit = False
#             cursor = conn.cursor()
#             query = """
#             DELETE FROM users
#             WHERE email = %s;
#             """
#             cursor.execute(query, (user_email,))
#             conn.commit()
#             if cursor.rowcount == 0:
#                 print("No user found with that ID.")
#             else:
#                 print(f"User with email {user_email} deleted successfully.")
#         except Exception as e:
#             if conn:
#                 conn.rollback()
#             print("Error:", e)
#         finally:
#             if cursor:
#                 cursor.close()
#             if conn:
#              conn.close()