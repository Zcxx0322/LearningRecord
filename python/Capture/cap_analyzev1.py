#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps


import pyshark


def frame_info_get(pkt):
    encap_type = pkt.frame_info.encap_type
    arrival_time = pkt.frame_info.time
    epoch_time = pkt.frame_info.time_epoch
    frame_number = pkt.frame_info.number
    frame_length = pkt.frame_info.len
    cap_length = pkt.frame_info.cap_len
    print('Encapsulation Type:\t%s\nArrival Time:\t\t%s\nEpoch Time:\t\t%s\nFrame Number:\t\t%s\n'
          'Frame Length:\t\t%s\nCapture Length:\t\t%s' %
          (encap_type, arrival_time, epoch_time, frame_number, frame_length, cap_length))


def ethernet_info_get(pkt):
    src = pkt.eth.src
    dst = pkt.eth.dst
    net_type = pkt.eth.type
    print('Destination mac:\t%s\nSource mac:\t\t%s\nNetType:\t\t%s' % (src, dst, net_type))


def ip_info_get(pkt):
    src_ip = pkt.ip.src
    dst_ip = pkt.ip.dst
    print('Source IpAddress:\t%s\nDestination IpAddress:\t%s' % (src_ip, dst_ip))


def tcp_info_get(pkt):
    src_port = pkt.tcp.srcport
    dst_port = pkt.tcp.dstport
    seq_num = pkt.tcp.seq
    ack_num = pkt.tcp.ack
    print('Source Port:\t\t%s\nDestination Port:\t%s\n'
          'Seq:\t\t\t%s\nAck:\t\t\t%s' % (src_port, dst_port, seq_num, ack_num))
    print('------------------------------------')


def main():
    capture = pyshark.FileCapture('/home/colamps/workspace/test111')
    ftp_packets = []
    for packet in capture:
        ftp_packets.append(packet)
        if len(ftp_packets) == 2:
            break
    for pkt in ftp_packets:
        # ftp_info_get(pkt)
        frame_info_get(pkt)
        ethernet_info_get(pkt)
        ip_info_get(pkt)
        tcp_info_get(pkt)


if __name__ == '__main__':
    main()
