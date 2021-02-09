#1.导入模块 sqlite3
import sqlite3

#2.数据库文件
db_file='scores.db'

#3.虚拟DOM的两种创建方式.获取与数据库的连接
conn=sqlite3.connect(db_file)

#4.编写sql语句
sql='select * from score'

#5.执行sql语句
cur=conn.cursor()
cur.execute(sql)
#6.打印结果
print(cur.fetchall())
#7.关闭连接
conn.close()