#!/usr/bin/python
#-*-coding: utf-8-*-
import os
from ftplib import FTP
def ftpconnect(host,username,password):
  ftp = FTP(host)
  #ftp.set_debuglevel(2)     #打开调试级别2，显示详细信息
 # ftp.connect(host, 20)     #连接
  ftp.login(username, password) #登录，如果匿名登录则用空串代替即可
  return ftp

def uploadfile(ftp, localfile):
    bufsize = 1024
    ftp.cwd('/home/dawn/FTP')
    fp = open(localfile, 'rb')
    remotepath = os.path.basename(localfile)
    ftp.storbinary('STOR '+ remotepath , fp, bufsize) #上传文件
    ftp.set_debuglevel(0)
    fp.close()


if __name__ == "__main__":
  ip = '192.168.80.142'
  username = 'dawn'
  password = 'root'
  ftp = ftpconnect(ip,username,password)
  #########设置本地读取文件路径##############
  localfile='G:/test/upload/test.txt'
  uploadfile(ftp,localfile)

