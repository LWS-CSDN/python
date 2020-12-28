import sqlite3
db_file='scores.db'

#删除数据
def delete_score_data():
    #1.获取连接
    conn=sqlite3.connect(db_file)
    #2.打开游标
    cur=conn.cursor()
    #删除sql语句
    sql='delete from score where id=?'
    #构建元组数据
    id=(3,)
    cur.execute(sql,id)
    #进行提交commit
    conn.commit()
    #4.关闭资源
    cur.close()
    conn.close()
delete_score_data()