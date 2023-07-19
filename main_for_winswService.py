import sys

from thread_for_folder import monitor
class MyException(Exception):
    def __init__(self, message):
        self.message = message

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for folder in sys.argv[1:]:
            monitor(folder)# 开始监听文件变化
            # print(folder)
    else:
        raise MyException("need one argument ")