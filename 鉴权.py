import math
while(1):
    secret=eval(input("请输入密钥："))
    print("解密密码:",int(math.pow(secret,3)/100000+50))