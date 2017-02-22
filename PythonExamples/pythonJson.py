# -*- coding: utf-8 -*-
'''
Created on 2017年2月21日

@author: wangyong
'''

import json

if __name__ == '__main__':
    #字典:
    data = {"name" : "tom", "age" : 42}
    json_dic = json.dumps(data) # 编码：把一个Python对象(字典)编码转换成Json字符串
    print json_dic
    
    dic = json.loads(json_dic) # 解码：把Json格式字符串解码转换成Python对象
    print dic
    print type(dic) #<type 'dict'>
    
    #列表
    data = ['physics', 'chemistry', 1997, 2000]
    json_list = json.dumps(data) # 编码：把一个Python对象(列表)编码转换成Json字符串
    print json_list
    
    list = json.loads(json_list) # 解码：把Json格式字符串解码转换成Python对象
    print list
    print type(list) #<type 'list'>
    #元组
    data = ('physics', 'chemistry', 1996, 2016)
    json_tup = json.dumps(data) # 编码：把一个Python对象(元组)编码转换成Json字符串
    print json_tup
    
    tup = json.loads(json_tup) # 解码：把Json格式字符串解码转换成Python对象
    print tup
    print type(tup) #<type 'list'>
    
    data = {"name" : "张三", "age" : 42}
    json_dic = json.dumps(data,ensure_ascii=False) # 编码：把一个Python对象(字典)编码转换成Json字符串
    print json_dic
    
    dic = json.loads(json_dic) # 解码：把Json格式字符串解码转换成Python对象
    print dic
    print type(dic) #<type 'dict'>
    
