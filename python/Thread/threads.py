#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps
import time
from threading import Thread

"zhangchongxin"
def main(name="colamps"):
    for i in range(4):
        print("Hi", name)
        time.sleep(2)


thread_1 = Thread(target=main)
thread_1.start()
thread_2 = Thread(target=main, args=("zhang",))
thread_2.start()
thread_3 = Thread(target=main, args=("chong",))
thread_3.start()
thread_4 = Thread(target=main, args=("xin",))
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

