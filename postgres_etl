import psycopg2


# Параметры соединения
conn_string= "host='localhost' port=5433 dbname='my_database' user='root' password='postgres'" 

# Создаем соединение (оно поддерживает контекстный менеджер, рекомендую пользоваться им)
# Создаем курсор - это специальный объект который делает запросы и получает их результаты
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    query = """select * from pg_catalog.pg_tables""" # запрос к БД
    cursor.execute(query) # выполнение запроса
    result = cursor.fetchone() # получение результата
    print(result)

# Параметры соединения
conn_string= "host='localhost' port=5433 dbname='my_database' user='root' password='postgres'" 

# Создаем соединение (оно поддерживает контекстный менеджер, рекомендую пользоваться им)
# Создаем курсор - это специальный объект который делает запросы и получает их результаты
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    query = """SELECT table_name
  FROM information_schema.tables
 WHERE table_schema='public'
   AND table_type='BASE TABLE';""" # запрос к БД
    cursor.execute(query) # выполнение запроса
    result = cursor.fetchone() # получение результата
    print(result)
    
  import psycopg2

conn_string= "host='localhost' port=54320 dbname='my_database' user='root' password='postgres'" 

with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    row = (-999, 'name', 'address', 0, 'phone', 0, 'mktsegment', 'comment') # кортеж для вставки
    insert = """
    insert into customer (
           c_custkey   
         , c_name      
         , c_address   
         , c_nationkey 
         , c_phone     
         , c_acctbal   
         , c_mktsegment
         , c_comment
    )
    values
    ({values})
    """.format(
    # биндим параметры в строку, чтобы избежать sql-иньекций (best practice)
    values=cursor.mogrify("%s, %s, %s, %s, %s, %s, %s, %s", row).decode('utf-8')
    )
    print('sql запрос:', insert)
    cursor.execute(insert)
    conn.commit() # комитим транзакцию
    cursor.execute('select * from customer where c_custkey < 0')
    result = cursor.fetchall()
    print('результат вставки:', result)
    
    
 import psycopg2

conn_string= "host='localhost' port=54320 dbname='my_database' user='root' password='postgres'" 
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY customer TO STDOUT WITH DELIMITER ',' CSV HEADER;"
    with open('resultsfile.csv', 'w') as f:
        cursor.copy_expert(q, f)
        
        
import pandas as pd
df = pd.read_csv('resultsfile.csv')
df.head(10)


####### !!!!!!!!!!!!!


def to_tbl(tbl_str):
    conn_string= "host='localhost' port=54320 dbname='my_database' user='root' password='postgres'" 
    with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
        q = f"COPY {tbl_str} TO STDOUT WITH DELIMITER ',' CSV HEADER;"
        with open('resultsfile.csv', 'w') as f:
            cursor.copy_expert(q, f)


def count_tbl1(tbl_str):
    conn_string= "host='localhost' port=54320 dbname='my_database' user='root' password='postgres'" 
    with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
        q = f"SELECT count(*) from {tbl_str}"
        cursor.execute(q)
        return(cursor.fetchall())
def count_tbl2(tbl_str):
    conn_string= "host='localhost' port=5433 dbname='my_database' user='root' password='postgres'" 
    with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
        q = f"SELECT count(*) from {tbl_str}"
        cursor.execute(q)
        return(cursor.fetchall())
# переделать в 1 функцию с изменением портов

def from_tbl(tbl_str):
    conn_string= "host='localhost' port=5433 dbname='my_database' user='root' password='postgres'" 
    with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
        q = f"COPY {tbl_str} FROM STDIN WITH DELIMITER ',' CSV HEADER;"
        with open('resultsfile.csv', 'r') as f:
            cursor.copy_expert(q, f)
            
tbl_list = ['customer','lineitem','nation','orders','part','partsupp','region','supplier']
# кол-во записей
print('откуда','куда')
for i in tbl_list:
    print(count_tbl1(i),count_tbl2(i))
    
    
    #### IMPORT#########
for i in tbl_list:
    to_tbl(i)
    from_tbl(i)
    
# кол-во записей
print('откуда','куда')
for i in tbl_list:
    print(count_tbl1(i),count_tbl2(i))
    
  
    
    


 
