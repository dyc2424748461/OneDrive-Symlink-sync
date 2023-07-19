from thread_for_folder import monitor

if __name__ == "__main__":
    folder = r"C:\Users\O-c-O\OneDrive\up" # onedrive中你放入软链接的文件夹 此文件夹无软链接
    monitor(folder)# 开始监听文件变化