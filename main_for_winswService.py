import sys

from thread_for_folder import monitor
class MyException(Exception):
    def __init__(self, message):
        self.message = message
def print_help():
    help = """
    程序将会检测存在OneDrive文件夹中的软链接，并且进行更新
    输入的应该是非软链接的文件夹
    用法：main_for_winswService [文件夹1] [文件夹2]
    """
    print(help)
if __name__ == "__main__":
    if len(sys.argv) > 1:
        for folder in sys.argv[1:]:
            monitor(folder)# 开始监听文件变化
            print(folder)
    else:
        print_help()
        raise MyException("Note: at least one argument is required")