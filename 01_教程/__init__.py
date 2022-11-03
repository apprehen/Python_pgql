import psycopg2 as pg

# 创建实例对象
conn = pg.connect(database="test_db", user="postgres", password="Apprehen", host="127.0.0.1", port="5432")
print("Opened database successfully")
cur = conn.cursor()

# 插入操作
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#   VALUES(3,'kurumi',18,'bigdate',10000)")
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#   VALUES(4,'megumi',18,'explosion',20000)")
# conn.commit()
# print("Records created successfully")
# conn.close()

# # 查询操作
# cur.execute("SELECT id,name,address,salary from COMPANY")
# rows= cur.fetchall()
# for row in rows:
#   print(f"ID = {row[0]}")
#   print(f"NAME = {row[1]}")
#   print(f"ADDRESS = {row[2]}")
#   print(f"SALARY = {row[3]}")
#   print("\n")
# print("Operation done successfully")
# conn.close()

# # 更新操作
# cur.execute("UPDATE COMPANY set name='二乃',salary=100000 where ID=1")
# conn.commit()
# print("Operation done successfully")
# conn.close()

# 删除操作
cur.execute("DELETE FROM COMPANY where ID=3;")
conn.commit()
print("Total number of rows deleted :",cur.rowcount)

