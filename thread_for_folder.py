from recreate_symlink import notify_system_change as update_file
import os
import threading

# 记录进程
threads = []


def check_folder_links(folder_path):
    '''
    监听软链接的文件夹
    :param folder_path:
    :return:
    '''
    for item in os.listdir(folder_path):
        # print(item)
        item_path = os.path.join(folder_path, item)
        print(item_path)
        try:
            os.readlink(item_path)

            # 开启一个线程进行监听这个文件夹 ps:软链接文件夹不能过多，否则影响性能
            thread_work(item_path)
            print(f"{item_path} is a symbolic link.")
        except Exception as e:
            print(e)

def thread_work(smlink_folder_path):
    # 创建多个线程来执行监控任务
    thread = threading.Thread(target=update_file, args=(smlink_folder_path,))
    threads.append(thread)
    thread.start()


def monitor(foler):

    check_folder_links(foler)

    print("Monitoring threads have finished")

if __name__ == "__main__":

    parent_folder = r"C:\Users\O-c-O\OneDrive\up"  # 文件夹路径

    check_folder_links(parent_folder)


    print("Monitoring threads have finished")
    # add_startup_registry_entry()
