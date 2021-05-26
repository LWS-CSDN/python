
import pymysql
db=pymysql.connect(
    host='172.18.46.230',
    user='jhq',
    password='123456',
    port=3306
)
cursor=db.cursor()
# 获取MySQL版本
cursor.execute('SELECT VERSION()')
data=cursor.fetchone()
print('Database version:',data)
# 创建数据库Test,默认编码utf-8
cursor.execute('CREATE DATABASE test DEFAULT CHARACTER SET utf8')
db.close()