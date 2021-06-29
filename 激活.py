import os
import random
import math

print("****************************************")
print("欢迎使用BUCT激活工具1.0-2020.09.18")
print("请加入QQ群聊 664761636 联系管理员索取使用密钥")
print("请放在桌面并以管理员权限运行")
print("****************************************")


dirpath=''

p_key=random.randint(1000,6000)

print("您的特征码为：",p_key)
try:
    # print(math.pow(p_key,3)/100000+50)
    secret=eval(input("请输入从管理员处索取到的密钥："))
except:
    print("鉴权错误 请联系管理员")
    exit()


if(secret!=int(math.pow(p_key,3)/100000+50)):
    print("鉴权错误 请联系管理员")
    exit()

def office():
    tag=0
    #找文件 ospp.vbs
    for dirpath, dirnames,filename in os.walk('c:\\'):
        for i in filename:
            if i=='OSPP.VBS':
                tag=1
                break
        if tag==1:
            print("office目录为：",dirpath)
            break
        
    print("请输入要激活的office版本 \n 1.office 2016 \n 2.office 2019 \n 3.office 2010 \n")
    user_command=eval(input("请输入:"))
    key=''
    if(user_command==1):
        key='XQNVK-8JYDB-WJ9W3-YJ8YR-WFG99'
    elif(user_command==2):
        key='NMMKJ-6RK4F-KMJVX-8D9MJ-6MWKP'
    elif(user_command==3):
        key='VYBBJ-TRJPB-QFQRF-QFT4D-H3GVB'
    else:
        print("。。。")
        exit()


    command='''
    cd "'''+dirpath+'''"
    cscript ospp.vbs  /inpkey:'''+key+''' 
    cls
    cscript ospp.vbs /sethst:121.195.153.227
    '''
    f=open('datdatdat.bat','wt+')
    f.writelines(command)
    f.close()
    os.system('datdatdat.bat')
    os.system('cls')

    f=open('datdatdat.bat','wt+')
    command='''
    cd "'''+dirpath+'''"
    cscript ospp.vbs /act
    '''
    f.writelines(command)
    f.close()
    print(os.system('datdatdat.bat'))
    os.remove("datdatdat.bat")
    

def windows():
    user_command=0
    print("请输入要激活的windows版本 \n 1.windows 7 \n 2.windows 10 3.windows 8 \n 4.windows 8.1 \n")
    user_command=eval(input("请输入:"))
    key=''
    if(user_command==1):
        key='FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4'
    elif(user_command==2):
        key='W269N-WFGWX-YVC9B-4J6C9-T83GX'
    elif(user_command==3):
        key='NG4HW-VH26C-733KW-K6F98-J8CK4'
    elif(user_command==4):    
        key='GCRJD-8NW9H-F2CDX-CCM8D-9D6T9'
    else:
        exit()
    
    command='''
    slmgr.vbs -ipk '''+key+'''
    cls
    slmgr.vbs /skms 121.195.153.227:1688
    cls
    slmgr.vbs /ato
    '''
    f=open('datdatdat.bat','wt+')
    f.writelines(command)
    f.close()
    os.system('datdatdat.bat')
    os.system('cls')
    os.remove("datdatdat.bat")


print("本软件使用BUCT的KMS激活服务")
user_command=eval(input("请输入需要的模块 \n 1.office \n 2.windows 10 \n 请输入:"))
if(user_command==1):
    office()
else:
    windows()
exit()