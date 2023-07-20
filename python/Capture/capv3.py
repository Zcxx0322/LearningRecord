import pyshark


def CaptureInfo(pkt):
    print('-----------------------------------------------')
    encap_type = pkt.frame_info.encap_type
    arrival_time = pkt.frame_info.time
    epoch_time = pkt.frame_info.time_epoch
    frame_number = pkt.frame_info.number
    frame_length = pkt.frame_info.len
    cap_length = pkt.frame_info.cap_len
    src = pkt.eth.src
    dst = pkt.eth.dst
    net_type = pkt.eth.type
    src_ip = pkt.ip.src
    dst_ip = pkt.ip.dst
    src_port = pkt.tcp.srcport
    dst_port = pkt.tcp.dstport
    seq_num = pkt.tcp.seq
    ack_num = pkt.tcp.ack
    print('Encapsutcp Type:\t%s\nArrival Time:\t\t%s\nEpoch Time:\t\t%s\nFrame Number:\t\t%s\n'
          'Frame Length:\t\t%s\nCapture Length:\t\t%s' %
          (encap_type, arrival_time, epoch_time, frame_number, frame_length, cap_length))
    print('Destination mac:\t%s\nSource mac:\t\t%s\nNetType:\t\t%s' % (src, dst, net_type))
    print('Source IpAddress:\t%s\nDestination IpAddress:\t%s' % (src_ip, dst_ip))
    print('Source Port:\t\t%s\nDestination Port:\t%s\n'
          'Seq:\t\t\t%s\nAck:\t\t\t%s' % (src_port, dst_port, seq_num, ack_num))


def main():
    capture = pyshark.FileCapture('/home/colamps/workspace/test111')
    for pkt in capture:
        if 'FTP' in pkt:
            if pkt.ftp.get_field_value('request_command') == 'USER':
                CaptureInfo(pkt)
                print(pkt.ftp)
            if pkt.ftp.get_field_value('request_command') == 'PASS':
                CaptureInfo(pkt)
                print(pkt.ftp)


if __name__ == '__main__':
    main()
