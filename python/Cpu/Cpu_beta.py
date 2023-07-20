# ！~/workspace/pythonProject
# -*- coding:utf-8 -*-
# Copyright (C) 2023-2024 XXXXXXXX
import signal

import psutil


# noinspection PyUnusedLocal
def sigint_handler(sig, frame):
    print('\n\n收到 Ctrl+C 信号，退出......')
    exit(0)


def main():
    while True:
        total_cpu_times = psutil.cpu_times_percent(interval=1)
        print("Cpu:")
        print("sy: {}%".format(total_cpu_times.system))
        print("us: {}%".format(total_cpu_times.user))
        print("id: {}%".format(total_cpu_times.idle))
        print("ni: {}%".format(total_cpu_times.nice))
        print("hi(irq): {}%".format(total_cpu_times.irq))
        print("si(softirq): {}%".format(total_cpu_times.softirq))
        print("st(steal): {}%".format(total_cpu_times.steal))


if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigint_handler)
    main()
