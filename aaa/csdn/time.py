import time


class GetTime():
    def get_system_time(self):
        print(time.time())
        print(time.localtime())
        # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

gettime = GetTime()
gettime.get_system_time()
