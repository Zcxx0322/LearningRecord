#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps

import socket
import struct


class network_info_mod(object):

    def __int__(self, ipaddr, route_information, dns):
        self.ipaddr = ipaddr
        self.route_information = route_information
        self.dns = dns

    def ipget(self):
        ipaddress = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ipaddress.connect(("8.8.8.8", 80))
        ip_result = ipaddress.getsockname()
        print("本机地址:{}".format(ip_result[0]))

    def route_get(self):
        """
        解析/proc/net/route文件获取：网卡名称、子网掩码、网关
        :return:
        """
        with open("/proc/net/route") as f:
            next(f)
            for line in f:
                routes = line.strip().split()
                interface = routes[0]
                mask = socket.inet_ntoa(struct.pack("<L", int(routes[7], 16)))
                gateway = socket.inet_ntoa(struct.pack("<L", int(routes[2], 16)))
            print("网卡名称:{}\n子网掩码:{}\n默认网关:{}".format(interface, mask, gateway))

    def dns_get(self):
        """
        读取/etc/resolv.conf文件，获取DNS地址
        :return:
        """
        with open('/etc/resolv.conf', 'r') as f:  # 读取/etc/resolv.conf文件
            lines = f.readlines()
            line1 = lines[1]
            line2 = lines[2]
            print("DNS服务器:{}\t  {}".format(line1, line2))


ip = network_info_mod()
route_information = network_info_mod()
dns_addr = network_info_mod()


ip.ipget()
route_information.route_get()
dns_addr.dns_get()
