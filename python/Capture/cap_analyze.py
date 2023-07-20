#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps

import pyshark


def key_information_get(pkt):
    # https://github.com/KimiNewt/pyshark/README.md
    if 'FTP' in pkt:
        if pkt.ftp.get_field_value('request_command') == 'USER':
            print(pkt.ftp)
        if pkt.ftp.get_field_value('request_command') == 'PASS':
            print(pkt.ftp)


def ip_conversation(pkt):
    protocol = pkt.transport_layer
    src_addr = pkt.ip.src
    src_port = pkt[pkt.transport_layer].srcport
    dst_addr = pkt.ip.dst
    dst_port = pkt[pkt.transport_layer].dstport
    print('%s  %s:%s --> %s:%s' % (protocol, src_addr, src_port, dst_addr, dst_port))


def main():
    capture = pyshark.FileCapture('/home/colamps/workspace/test111')
    for pkt in capture:
        ip_conversation(pkt)
        key_information_get(pkt)


if __name__ == '__main__':
    main()
