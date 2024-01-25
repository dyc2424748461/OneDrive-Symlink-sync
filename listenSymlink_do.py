import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class FolderEventHandler(FileSystemEventHandler):
    def __init__(self, symlink_path):
        self.symlink_path = symlink_path
        self.event_occurred = False

    def on_any_event(self, event):
        # if event.event_type not in ['open', 'close']:  # 忽略 "打开" 和 "关闭" 事件
        self.event_occurred = True
        # print(event)
def rename_symlink(symlink_path):
    # 如果发生变化进行如下操作 ：对以前的软链接进行重命名
    time.sleep(10)
    # target_folder = os.readlink(symlink_path)
    try:
        directory, filename = os.path.split(symlink_path)
        tmp = filename+'_1_1'
        tmp_name = os.path.join(directory, tmp)
        os.rename(symlink_path, tmp_name)
        os.rename(tmp_name,symlink_path)
        print(f"successfully change name")
    except Exception as e:
        print(f"Error: {str(e)}")
    print(f"Folder updated: {symlink_path}")
    # time.sleep(60)

def do(symlink_path):
    # 重命名文件夹
    rename_symlink(symlink_path)



def notify_system_change(file_path):
    # 获取软链接的目标文件夹路径
    target_folder = os.readlink(file_path)
    now_time=time.strftime("%Y-%m-%d %H:%I:%S", time.localtime( time.time() ) )
    print(now_time,target_folder)
    # 创建Observer和EventHandler
    event_handler = FolderEventHandler(file_path)
    observer = Observer()
    observer.schedule(event_handler, target_folder, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
            if event_handler.event_occurred :
                do(file_path)
                time.sleep(60)
                event_handler.event_occurred = False
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    d_folder = r"C:\Users\O-c-O\OneDrive - post.usts.edu.cn\SyncedFolders\my-note"  # D文件夹软链接路径

    notify_system_change(d_folder)
