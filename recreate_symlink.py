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
        self.event_occurred = True
        # print(event)

def recreate_symlink(symlink_path):
    # 如果发生变化进行如下操作 ：对以前的软链接进行删除并重建
    time.sleep(10)
    target_folder = os.readlink(symlink_path)
    os.unlink(symlink_path)
    create_directory_link(target_folder,symlink_path)
    print(f"Folder updated: {symlink_path}")
    # time.sleep(60)

def create_directory_link(source, link):
    # 创建目录链接
    cmd = f'mklink /j "{link}" "{source}"'
    subprocess.run(cmd, shell=True)


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
            if event_handler.event_occurred :
                recreate_symlink(file_path)
                time.sleep(60)
                event_handler.event_occurred = False
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    d_folder = r"C:\Users\O-c-O\OneDrive - post.usts.edu.cn\test1"  # D文件夹软链接路径

    notify_system_change(d_folder)
