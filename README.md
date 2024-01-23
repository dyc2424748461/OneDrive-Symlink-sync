# syncForOneDrive

使用重命名目录链接的方式，提醒OneDrive进行更新。
> mklink /j link source #创建软链接

## 将需要建立软链接的文件夹统一放到一个目录中

在OneDrive文件夹下应将软链接文件夹都放到一个文件夹中。

文件夹的结构如下所示

```
|- normal_folder

​	|- folder1[symlink]

​	|- folder2[symlink]
```



## 使用

### [main.py](main.py)

在main.py中指定含有符号链接的正常文件夹。运行后main.py。

程序会默认加入开机自启，

==请同意==。

## [main_for_winswService.py](main_for_winswService.py)

> [winsw/winsw: A wrapper executable that can run any executable as a Windows service, in a permissive license. (github.com)](https://github.com/winsw/winsw)

需要使用winsw进行windows服务的创建。

1. 下载对应的winsw.exe、和.xml文件

2. 将winsw.exe 和.xml文件放在`服务文件夹`下

3. 修改xml文件https://github.com/winsw/winsw?tab=readme-ov-file#use-winsw-as-a-bundled-tool

   这里先简单使用sample-minimal.xml进行修改，在xml文件中修改的主要部分：

   - 指定运行main.py的python.exe，
   - 指定main_for_winswService.py文件地址。

   ```
   <service>
     
     <!-- ID of the service. It should be unique across the Windows system-->
     <id>syncForOneDrive</id>
     <!-- Display name of the service -->
     <name>recreate symlink</name>
     <!-- Service description -->
     <description>监控符号链接指向的文件，若有修改则重建符号链接</description>
     
     <!-- Path to the executable, which should be started -->
     <executable>"D:\coding\python_venv\syncForOneDrive\Scripts\python.exe"</executable>
   
     <!-- 
       OPTION: arguments
       Arguments, which should be passed to the executable
     -->
   
     <arguments>D:\coding\python\syncForOneDrive\main_for_winswService.py</arguments>
   
   </service>
   ```

然后在cmd中进入文件夹`服务文件夹`

执行命令 [winsw/winsw: A wrapper executable that can run any executable as a Windows service, in a permissive license. (github.com)](https://github.com/winsw/winsw#usage)

```
winsw install xxx.xml
winsw start xxx.xml
winsw stop xxx.xml
```


# 注意
程序仅仅模仿了检测文件夹内的文件内容是否发生变化，若发生变化则重命名目录链接，重命名两次保持目录名称不变。
    扩展了：
   - 开机自启
   - 一个目录链接一个线程