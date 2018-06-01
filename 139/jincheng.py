import threading
import time


def thread1_job():
    print('T1 开始\n')
    for i in range(10):
        time.sleep(0.5)
    print('T1 结束\n')


def exampleFuc():
    thread1 = threading.Thread(target=thread1_job, name='T4')
    thread1.start()
    thread1.join()
    print('所有的任务都做完了。\n')


exampleFuc()