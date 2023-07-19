#  syncForOneDrive

使用替换符号链接的方式，提醒OneDrive进行更新。

## 条件

在OneDrive中含有符号链接的文件夹，并且都应该属于一个正常文件夹内。

文件夹的结构如下所示

```
|- normal_folder

​	|- folder1[symlink]

​	|- folder2[symlink]
```



## 使用

在main.py中指定含有符号链接的正常文件夹。运行后main.py。

程序会默认加入开机自启，

==请同意==。