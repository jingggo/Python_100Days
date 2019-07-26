"""

@Author:jyang
@Date:7/4/2019
"""

import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
import  requests
from lxml import etree
import datetime
import time
import html
import csv
import exception
import int
import psycopg2
import socket
import sys
import os


#处理航班信息HTML
def get_info(fnum,soup,dep,arr):
    try:
        hbh = fnum

        phdate=time.strftime("%Y-%m-%d") #抓取票号日期

        szm_str=dep

        szm_end=arr

        str_time=' '
        for li in soup.select('div[class="fl three-lef"]'): #起飞时间
         str_time=li.get_text()

        end_time=' '
        for li in  soup.select('div[class="fr three-rig"]'): #到达时间
         end_time=li.get_text()

         jt = ' '
         for li in soup.select('div[class="fl three-mid"]'):  # 经停
             jt = li.get_text()
             if(jt!=' '):
                 jt=jt[4:]

         km=''
         for li in soup.select('p[class="one"]'): #里程（km）
          km=li.get_text()
          km=km[4:]

         km_time=' '
         for li in soup.select('p[class="two"]'): #耗时（分钟）
          km_time=li.get_text()
          km_time=km_time[4:]

        jx=' '
        for li in soup.select('span[style="max-width:75px!important"]'): #机型
         jx=li.get_text()

        jxdx=' '
        if(soup.select('span[title="大型客机"]')):
           jxdx='大型客机'
        elif(soup.select('span[title="中型客机"]')):
           jxdx = '中型客机'
        elif(soup.select('span[title="小型客机"]')):
           jxdx = '中型客机'

        can=' '
        if (soup.select('span[class="totalCont"]')):
         can='提供'

        pf=' '
        for li in soup.select('span[class="score cur"]'): #舒适度评分
         pf=li.get_text()

        updatetime=time.strftime("%Y-%m-%d") #更新时间

    finally:
        return(hbh, phdate, szm_str, szm_end, str_time, end_time, jt, km, km_time, jx, jxdx, can, pf, updatetime)


ok_ip=[] #可用IP
all_ip=[] #IP列表
ok=[] #返回信息
# 根据航班参数请求页面
def get_content(fnum,dep,arr,date,type):
    # 首次使用本机IP
    # http://happiness.variflight.com/search/airline?date=2019-07-04&dep=WUH&arr=LJG&type=1
    content = requests.get('http://happiness.variflight.com/info/detail?fnum='+fnum+'&dep='+dep+'&arr='+arr+'&date='+date+'&type='+type+'').text
    soup = BeautifulSoup(content, 'html.parser')

    #是否上限需代理IP
    if(content.find("Notifica: timeout del gateway")>0 or content.find("The requested URL could not be retrieved")>0 or content.find("main notFound")>0 or content.find("此类查询已达当日上限")>0):
      ipinfo = open('代理IP(2017-12-25).txt')
      all_ip = ipinfo.read().splitlines()

      if len(ok_ip)>0: #有可用IP
           iptext=ok_ip[0]
           # 查询上限，换IP
           proxies = {'http': '//' + iptext, 'https': '//' + iptext}
           try:
               content = requests.get(
                   'http://happiness.variflight.com/info/detail?fnum=' + fnum + '&dep=' + dep + '&arr=' + arr + '&date=' + date + '&type=' + type + '',
                   proxies=proxies).text
               #, timeout=120
               #socket.setdefaulttimeout(150)  # 超时后能自动往下继续跑
               soup = BeautifulSoup(content, 'html.parser')
               # 可用IP是否上限
               if (content.find("Notifica: timeout del gateway") > 0 or content.find(
                       "The requested URL could not be retrieved") > 0 or content.find(
                   "main notFound") > 0 or content.find("此类查询已达当日上限") > 0):
                   ok_ip.remove(iptext)  # 移除不可用IP
           except:
               pass

      else: #无可用IP找IP列表
          # 获取IP列表
          for qwe in all_ip:
              iptext = qwe

              # 查询上限，换IP
              proxies = {'http': '//' + iptext, 'https': '//' + iptext}
              try:
                  content = requests.get(
                      'http://happiness.variflight.com/info/detail?fnum=' + fnum + '&dep=' + dep + '&arr=' + arr + '&date=' + date + '&type=' + type + '',
                      proxies=proxies).text
                  #,timeout=120
                  #socket.setdefaulttimeout(150) ##超时后能自动往下继续跑
                  soup = BeautifulSoup(content, 'html.parser')

                  # 可用IP是否上限
                  if (content.find("502 Bad Gateway")>0 or content.find("Notifica: timeout del gateway") > 0 or content.find(
                          "The requested URL could not be retrieved") > 0 or content.find(
                          "main notFound") > 0 or content.find("此类查询已达当日上限") > 0):
                      ok_ip.remove(iptext)  # 移除不可用IP
                      continue
                  # 是可用IP即结束循环
                  else:
                      ok_ip.append(iptext)  # 加入可用IP
                      print('目前可用IP：' + iptext)
                      break
              except :
                  continue

    #暂无航班信息
    if (content.find("没有找到您输入的航班信息") > 0):
        ok=[]
    #查询成功
    else:
        try:
          ok=get_info(fnum,soup,dep,arr)
        except:
            return ok
    #返回航班信息
    return ok


#写入CSV文件
def save(fnum,dep,arr,date,type):
    #返回航班信息
    try:
       content=get_content(fnum,dep,arr,date,type)
       # 写方式打开一个文本，把获取的航班信息存放进去
       with open('Flight_Info.csv', 'a', ) as f:
           writer = csv.writer(f)
           writer.writerows([content])
           f.close()
    except:
        pass


hbb=''
szm_cf=''
szm_md=''
#循环爬取
def py_info():
    global hbb
    global szm_cf
    global szm_md
    try:
        print('请输入航班号：')
        hbb = input()  # 航班号
        print('请输入出发地三字码：')
        szm_cf = input()  # 出发地三字码
        print('请输入目的地三字码：')
        szm_md = input()  # 目的地三字码
        hblx = '1'  # 航班类型默认为1
        hbrq = time.strftime("%Y-%m-%d")  # 日期默认当天
        save(hbb, szm_cf, szm_md, hbrq, hblx)  # 保存写入CSV文件
        print(hbb + '航班爬取完成！')

    # 爬取出错跳过继续
    except:
        print(hbb+'航班爬取出错'+szm_cf+szm_md) #输出出错航班信息
        pass


#主程序
if __name__ == '__main__':
    py_info()