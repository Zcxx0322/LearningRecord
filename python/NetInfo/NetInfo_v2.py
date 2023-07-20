#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps


import socket
import struct


class NetworkMod:
    nic_name = ""
    ip_addr = ""
    ip_netmask = ""
    ip_gateway = ""
    dns_server = []

    def __init__(self) -> None:
        self.nic_name, self.ip_netmask, self.ip_gateway = route_get()
        self.ip_addr = ipget()
        self.dns_server = dns_get()


def ipget() -> str:
    ipaddress = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ipaddress.connect(("8.8.8.8", 80))
    ip_result = ipaddress.getsockname()
    return ip_result[0]


def route_get() -> tuple:
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
    return interface, mask, gateway


def dns_get() -> list:
    """
    读取/etc/resolv.conf文件，获取DNS地址
    :return:
    """
    dns_list = []
    with open('/etc/resolv.conf', 'r') as f:
        lines = f.readlines()
        dns_list.append(lines[1].replace('nameserver ', '').strip())
        dns_list.append(lines[2].replace('nameserver ', '').strip())
    return dns_list


def main():
    ip = NetworkMod()
    print('网卡名称:\t\t%s\n主机地址:\t\t%s\n子网掩码:\t\t%s\n默认网关：\t\t%s\nDNS服务器:\t\t%s/%s' % (
        ip.nic_name, ip.ip_addr, ip.ip_netmask, ip.ip_gateway, ip.dns_server[0], ip.dns_server[1]))


if __name__ == '__main__':
    main()
