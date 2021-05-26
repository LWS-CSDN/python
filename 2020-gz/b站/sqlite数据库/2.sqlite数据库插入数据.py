'''
SQLite数据库是一种嵌入式数据库,它的数据库就是一个文件scores.db
经常被集成到各种应用程序中,甚至IOS，Android,Mac OS,liunx
python中内置了Sqlite数据库,直接使用
数据库:关系型数据库,一个数据库中会有多张表,表和表之间通过主外键进行关联
python中操作sqlite数据库
获取connection
连接之后需要打开游标,cursor,
关闭连接,释放资源
本节任务:通过python向数据库插入数据
'''
import sqlite3
db_file='scores.db'
#插入数据
def insert_score_data():
    #1.获取连接
    conn=sqlite3.connect(db_file)
    #2.打开游标cursor
    cur=conn.cursor()
    #3.虚拟DOM的两种创建方式.插入sql语句
    #insert into +表名(列1,列2,...) values(?,?,...)
    sql='insert into score (stu_name,match_score,chinese)' \
        ' values(?,?,?)'
    #插入数据时,需要使用元组类型
    data=('赵五',89.9,78.2)
    cur.execute(sql,data)
    #执行插入时,需要进行显示提交数据,否则数据无法同步到数据库中
    conn.commit()
    #4.关闭资源
    cur.close()
    conn.close()

insert_score_data()