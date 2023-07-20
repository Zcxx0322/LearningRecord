#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps

import socket
import struct

ipaddress = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ipaddress.connect(("8.8.8.8", 80))
ip_result = ipaddress.getsockname()
print("本机地址:{}".format(ip_result[0]))

with open("/proc/net/route") as f:  # 解析/proc/net/route文件
    next(f)
    for line in f:
        routes = line.strip().split()
        interface = routes[0]  # 网卡名称
        mask = socket.inet_ntoa(struct.pack("<L", int(routes[7], 16)))  # 解子网掩码
        gateway = socket.inet_ntoa(struct.pack("<L", int(routes[2], 16)))  # 解网关
print("网卡名称:{}\n子网掩码:{}\n默认网关:{}".format(interface, mask, gateway))

with open('/etc/resolv.conf', 'r') as f:  # 读取/etc/resolv.conf文件
    lines = f.readlines()
    line1 = lines[1]
    line2 = lines[2]
    print("DNS服务器:{}\t  {}".format(line1, line2))
