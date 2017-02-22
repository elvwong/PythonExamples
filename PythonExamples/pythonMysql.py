# -*- coding: utf-8 -*-
'''
Created on 2017年2月21日

@author: wangyong
'''

# 1、导入MySQLdb模块
import MySQLdb 

def connDb():
    # 2、连接数据库连接
    # MySQLdb.connect(目标数据库IP，用户，密码，数据库)
    db = MySQLdb.connect("localhost", "root", "sa", "test") 
    
    # 3、使用cursor()方法获取操作游标
    cursor = db.cursor()
    
    # 4使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")
    
    # 5、使用 fetchone() 方法获取一条数据库。
    data = cursor.fetchone()
    print "Database version : %s " % data
    
    # 6、关闭数据库连接
    db.close()
    
def selectDb():
    #2、连接数据库连接
    #MySQLdb.connect(目标数据库IP，用户，密码，数据库)
    db = MySQLdb.connect("localhost","root","sa","test" ) 
    #3、使用cursor()方法获取操作游标
    cursor = db.cursor()
    #4使用execute方法执行SQL语句
    sql = "SELECT `time`,`mem_usage` FROM `stat` where `host`='localhost' limit 0,10" 
    cursor.execute(sql)
    #5、获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        time = row[0]
        mem_usage = row[1]
        # 打印结果
        print " time =%s, mem_usage =%s " % \
                 (time, mem_usage )
    
    #6、关闭数据库连接
    db.close()

def insertDb():
    #2、连接数据库连接
    #MySQLdb.connect(目标数据库IP，用户，密码，数据库)
    db = MySQLdb.connect("localhost","root","sa","test" ) 
    #3、使用cursor()方法获取操作游标
    cursor = db.cursor()
    #4使用execute方法执行SQL语句
    sql="""insert into stat(`host`,`mem_free`,`mem_usage`,`mem_total`,`load_avg`,`time`)
        VALUES ('localhost', '7198', '9133', '16332', null, '1487044790')"""        
    cursor.execute(sql)
    #5、提交到数据库执行
    db.commit()
    #6、关闭数据库连接
    db.close()

if __name__ == '__main__':
    insertDb()