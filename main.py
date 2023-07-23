from automatic_start import add_startup_registry_entry,remove_from_startup
from thread_for_folder import monitor


if __name__ == "__main__":
    desc = "update symlink for OneDrive" # 程序的描述
    program_name = "recreate_symlin" # 自定义名字
    add_startup_registry_entry(program_name,desc) # 加入开机自启
    folder = r"C:\Users\O-c-O\OneDrive\up" # 软链接文件都应在此文件夹中
    monitor(folder)# 开始监听文件变化

    '''
    删除开机自启动
    创建的快捷方式在C:\Users\<your user name>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
    '''
    # remove_from_startup(program_name)