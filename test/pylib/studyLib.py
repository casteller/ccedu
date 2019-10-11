# coding=utf-8
import requests,json,time
from pprint import pprint
class  studyLib(object):
    ip = "10.206.20.47:8097"
    time = time.strftime("%Y-%m-%d", time.localtime())
    def header(self):
        headers = {
            'Host': studyLib.ip,
            'Cookie':'APP_SESSIONID='+cookies,
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        return headers
    #获取cookies
    def get_cookie(self):
        session = requests.Session()
        url = "http://"+self.ip+"/ccsedu/a/login.do"
        payload = {'args': None, 'usertype':2, 'username':'zhangqingqin', 'password':'1qaz@WSX'}
        session.post(url,data=payload)
        s = session.cookies.get_dict()
        print(s['APP_SESSIONID'])
        return s['APP_SESSIONID']
    #添加老师
    def addteacher(self,name,masterCourse,externalUnit,position):
        url = "http://"+studyLib.ip+"/ccsedu/a/js/jsgl/saveLecturer "
        payload = {'name':name,'sex':1,'levels':1,'type':2,'masterCourse':masterCourse,'externalUnit':externalUnit,'position':position}
        res = requests.post(url,data=payload,headers=SL.header())
        print(res.json())
    #添加课件
    def addkejian(self,name,explain,specialty):
        url = "http://"+studyLib.ip+"/ccsedu/a/kc/kjgl/saveCourseware"
        payload = {'name':name,'explain':explain,'specialty':specialty,'corpId':510101,'deptId':51000005,'createBy':89787,'createDate':studyLib.time}
        r = requests.post(url,data=payload,headers=SL.header())
        print(r.json())
    #试题呈报
    def submit(self,id):
        url = "http://"+studyLib.ip+"/ccsedu/a/ks/tkgl/reportQuestion"
        payload = {'id': id}
        r = requests.post(url, data=payload, headers=SL.header())
        print(r.json())
    #试题审核
    def audit(self, id):
        url = "http://"+studyLib.ip+"/ccsedu/a/ks/tkgl/auditQuestion"
        payload = {'id': id}
        r = requests.post(url, data=payload, headers=SL.header())
        print(r.json()['msg'])
if __name__ == '__main__':
    SL = studyLib()
    cookies = SL.get_cookie()
    # res = SL.addteacher("李睿",'数学','未知机构','职务数学老师')
    # re = SL.addkejian("测试添加课件","测试课件简介",1)
    # with open(r'C:\Users\Administrator\Desktop\ksid.txt','r')as f:
    #     ids = f.read().splitlines()
    #     for id in  ids:
    #         SL.audit(id)
    # with open(r'C:\Users\Administrator\Desktop\username.txt', 'r')as f:
    #     users = f.read().splitlines()
    #     for user in  users:
    #         SL.get_cookie(user)
    SL.addteacher("李睿", '数学', '未知机构', '职务数学老师')