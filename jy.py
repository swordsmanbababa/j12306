import http.client, mimetypes, urllib, json, time, requests

######################################################################

class YDMHttp:

    apiurl = 'http://api.yundama.com/api.php'
    username = ''
    password = ''
    appid = ''
    appkey = ''

    def __init__(self, username, password, appid, appkey):
        self.username = username
        self.password = password
        self.appid = str(appid)
        self.appkey = appkey

    def request(self, fields, files=[]):
        response = self.post_url(self.apiurl, fields, files)
        response = json.loads(response)
        return response

    def balance(self):
        data = {'method': 'balance', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['balance']
        else:
            return -9001

    def login(self):
        data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['uid']
        else:
            return -9001

    def upload(self, filename, codetype, timeout):
        data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
        file = {'file': filename}
        response = self.request(data, file)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['cid']
        else:
            return -9001

    def result(self, cid):
        data = {'method': 'result', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'cid': str(cid)}
        response = self.request(data)
        return response and response['text'] or ''

    def decode(self, filename, codetype, timeout):
        cid = self.upload(filename, codetype, timeout)
        if (cid > 0):
            for i in range(0, timeout):
                result = self.result(cid)
                if (result != ''):
                    return cid, result
                else:
                    time.sleep(1)
            return -3003, ''
        else:
            return cid, ''

    def report(self, cid):
        data = {'method': 'report', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'cid': str(cid), 'flag': '0'}
        response = self.request(data)
        if (response):
            return response['ret']
        else:
            return -9001

    def post_url(self, url, fields, files=[]):
        for key in files:
            files[key] = open(files[key], 'rb');
        res = requests.post(url, files=files, data=fields)
        return res.text

username    = 'xwdlyx'

# 密码
password    = 'dkd231320'

# 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
appid       = 3805

# 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
appkey      = '2640280601391e049ae75cb0ef71c064'

# 图片文件

# 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
codetype    = 6701

# 超时时间，秒
timeout     = 60

def identify(filename):
    # 检查
    if (username == 'username'):
        print('请设置好相关参数再测试')
    else:
        # 初始化
        yundama = YDMHttp(username, password, appid, appkey)

        # 登陆云打码
        uid = yundama.login();
        print('uid: %s' % uid)

        # 查询余额
        balance = yundama.balance();
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        cid, result = yundama.decode(filename, codetype, timeout);
        print('cid: %s, result: %s' % (cid, result))
        return cid, result
# from urllib import request,parse
# import json
#
# def fetch_data(url):
#     with request.urlopen(url) as f:
#         data=f.read()
#     return json.loads(data)
#
#
#
# # 测试
# URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
# data = fetch_data(URL)
# print(data)
# assert data['query']['results']['channel']['location']['city'] == 'Beijing'
# print('ok')





# import itertools

# def pi(N):
#     iter1=itertools.count(1)
#     ns=itertools.takewhile(lambda x:x%2!=0 ,iter1)
#
#     sum=0.0
#     for i,each in enumerate(ns):
#         if i%2!=0:
#             each=0-each
#         sum=sum+4/float(each)
#     return sum
#
# print(pi(10))
# print(pi(100))
# print(pi(1000))
# print(pi(10000))
# assert 3.04 < pi(10) < 3.05
# assert 3.13 < pi(100) < 3.14
# assert 3.140 < pi(1000) < 3.141
# assert 3.1414 < pi(10000) < 3.1415
print('ok')
# import hashlib,random
# def calc_md5(pssword):
#     md5=hashlib.md5()
#     md5.update(pssword.encode('utf-8'))
#     return md5.hexdigest()

# import base64,struct
# bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
#
# def bmp_info(data):
#     print(data)
#     a=struct.unpack('<ccIIIIIIHH', data[0:30])
#     return {
#         'width': a[6],
#         'height': a[7],
#         'color': a[9]
#     }
# bi = bmp_info(bmp_data)
# assert bi['width'] == 28
# assert bi['height'] == 10
# assert bi['color'] == 16
# print('ok')

# import base64
#
# def safe_base64_decode(s):
#     if len(s)%4==0:
#         b=base64.b64decode(s)
#         return b
#     else:
#         s=s+b'='
#         return safe_base64_decode(s)
#
# assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
# assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
# print('ok')

# import re
# from datetime import  datetime,timezone,timedelta
#
# def to_timestamp(dt_str,tz_str):
#     dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
#     # utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
#     m=re.match(r'^UTC([/+/-])([0-9])+:00',tz_str)
#     print(m.groups())
#     a=m.group(2)
#     a=int(a)
#     b=m.group(1)
#     if b=='-':
#         a=0-a
#     tz=timezone(timedelta(hours=a))
#     # print(dt)
#     # dt.replace(tzinfo=timezone.utc)
#     # print(dt)
#     # dt=dt.astimezone(tz)
#     # print(dt)
#     dt = dt.replace(tzinfo=tz)
#     return dt.timestamp()
#
# da=datetime.fromtimestamp(1433121030.0)
# print(da)
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# assert t1 == 1433121030.0, t1
#
# t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# assert t2 == 1433121030.0, t2
#
# print('ok')

# import re
# def is_valid_email(addr):
#     a=re.match(r'(^[0-9a-zA-Z][0-9a-zA-Z.]+[0-9a-zA-Z]+)@([0-9a-zA-Z]+).(com)',addr)
#     return a
#
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')
# import json
#
# obj = dict(name='小明', age=20)
# s = json.dumps(obj, ensure_ascii=True)
#
# print(s)
# fpath = r'E:\bababa'
# import os
# import time
# import re
# def findFile(dirpath,type):
#     for file in os.listdir(dirpath):
#         dir=os.path.join(dirpath,file)
#         if os.path.isfile(file):
#             stype=os.path.splitext(dir)
#             if stype[1]==type:
#                 print(dir)
#                 print('\n')
#         else:
#             if os.path.isdir(dir):
#                 findFile(dir,type)
#
#
# findFile(fpath,'.txt')

# def listFile(path):
#     print('权限\t文件数\t用户名\t群组名\t大小\t月份\t日期\t时间\t文件名')
#     for x in os.listdir(path):
#         dir=os.path.join(path,x)
#         st=os.stat(dir)
#         print()
#         print(oct(st.st_mode)[-3:],end='\t')
#         print(numOfFiles(dir),end='\t')
#         print(st.st_uid,end='\t')
#         print(st.st_gid,end='\t')
#         print(st.st_size,end='\t')
#         lc_time=time.localtime(st.st_mtime)
#         print(time.strftime('%b',lc_time),end='\t')
#         print(lc_time.tm_mday,end='\t')
#         print(time.strftime('%H:%M',lc_time),end='\t')
#         print(x)
#
# def numOfFiles(path,num=1):
#     try:
#         for x in os.listdir(path):
#             dir=os.path.join(path,x)
#             if os.path.isdir(dir):
#                 num+=1
#                 num=numOfFiles(dir,num)
#     except BaseException as e:
#         pass
#     finally:
#         return num
#
# listFile(fpath)

# with open(fpath,'w') as f:
#     f.write('hel ikjfim ejkljge')
# with open(fpath,'r') as f:
#     s=f.read()
# print(s)

# import unittest
#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if(self.score>100 or self.score<0):
#             raise  ValueError
#         if self.score >= 80:
#             return 'A'
#         if self.score >= 60:
#             return 'B'
#         return 'C'
#
#
# class TestStudent(unittest.TestCase):
#
#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')
#
#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')
#
#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')
#
#     def test_invalid(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
#
# if __name__ == '__main__':
#     unittest.main()

# from functools import reduce
# import logging
# def str2num(s):
#     try:
#          s=float(s)
#     except ValueError as e:
#         logging(e)
#     finally:
#         return s
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()

# from enum import Enum,unique
# class Gender(Enum):
#     Male=0
#     Female=1
# class Student(object):
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')
# class Screen(object):
#
#     def __init__(self):
#         self.__resolution = 786432
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self,width):
#         self.__width=width
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self,height):
#         self.__height=height
#
#     @property
#     def resolution(self):
#         return self.__resolution
#
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')

# class Student(object):
#     count=0
#     def __init__(self,name):
#          Student.count=Student.count+1
#          self.__name=name



# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')
# class Student(object):
#     def __init__(self,name,gender):
#         self.__name=name
#         self.__gander=gender
#     def get_gender(self):
#         return self.__gander
#
#     def set_gender(self,gender):
#         self.__gander=gender
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')
#
# import functools,time
# def metric(func):
#     def wapper(*args,**kw):
#         print('%s executed in %s ms' % (func.__name__, time.time()))
#         return func(*args,**kw)
#     return wapper
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
# # -*- coding: utf-8 -*-
# def is_odd(n):
#     return n % 2 == 1
#
# L = list(filter(is_odd, range(1, 20)))
# L=list(filter(lambda x:x%2==1,range(1,200)))
#
# print(L)

# def createCounter():
#     def f():
#         n=0
#         while True:
#             n=n+1
#             yield n
#     sun=f()
#     def counter():
#         return next(sun)
#     return counter
#
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')


# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0]
# def by_score(t):
#     return t[1]
# L2 = sorted(L, key=by_name)
# print(L2)
# L2 = sorted(L, key=by_score)
# print(L2)


# def is_palindrome(n):
#     n=str(n)
#     length=len(n)
#     for i in range(0,length//2):
#         if(n[i]!=n[-i-1]):
#             return False
#     return True
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')




# from functools import reduce
# DIGITS = {'.':'.','0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def toListItem(c):
#     return DIGITS[c]
# def toList(s):
#     return  List(map(toListItem,s))
# def fun(x,y):
#     return 10*x+y
# def fun1(y,x):
#     return 0.1*y+x
#
# def toFloat(L):
#     for i,key in enumerate(L):
#         if(key=='.'):
#             break
#     FL=map(toListItem,L[i+1:len(L)])
#     FL=list(FL)
#     FL.reverse()
#     print(FL)
#     # FL.reverse()
#     return reduce(fun,map(toListItem,L[0:i-1]))+0.1*reduce(fun1,FL)
#
# print(toFloat('545484.124564'))
#
    


# def mul(a,b):
#     return a*b
# def prod(L):
#     a=reduce(mul,L)
#     print(a)
# L=[3,5,7,9]
# prod(L)

# def standardlize(s):
#     s=s.capitalize()
#     return s
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(standardlize, L1))
# print(L2)
#
#
#
#
#

# def triangles():
#     result=[]
#     while(True):
#         length=len(result)
#         if(length==0):
#             result=[1]
#             yield result
#         elif(length==1):
#             result=[1,1]
#             yield result
#         else:
#             result.append(1)
#             length=len(result)
#             temresult = result[:]
#             for i in range(1,length-1):
#                 temresult[i]=result[i-1]+result[i]
#             result=temresult
#             yield result
#
#
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break


# def findMinAndMax(L):
#     max=L[0]
#     min=L[0]
#     for num in L:
#         if(num>max):
#             max=num
#         if(num<min):
#             min=num
#     return max,min
#
# print(findMinAndMax([7]))
# print(findMinAndMax([7,1,3,2,4,6,8,9,5]))