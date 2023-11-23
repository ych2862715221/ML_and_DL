# ML_and_DL

## 1)简单介绍：

​	这是一个 Machine Learning 和 Deep Learning 的学习笔记(基于pytorch)，用于整理自己的看书学习过程，和存储代码。
参考教材：《深度学习》,《python机器学习基于Pytorch和Scikit-Learn》,《深度学习与计算机视觉》

## 2）关于上交代码：

进入项目文件夹，右键“Git Bash Here”，通过命令 git init 把这个目录变成git可以管理的仓库。
    
    git init
把文件添加到版本库中，使用命令 git add .添加到暂存区里面去，不要忘记后面的小数点“.”，意为添加文件夹下的所有文件
    
    git add .
 用命令 git commit告诉Git，把文件提交到仓库。引号内为提交说明(可以写提交时间、修改内容)
    
    git commit -m 'first commit'  
关联到远程库
    
    git remote add origin git@github.com:BeroKiTeer/CangshuMaze.git
获取远程库与本地同步合并
    
    git pull --rebase origin master
把本地库的内容推送到远程，使用 git push命令，实际上是把当前分支master推送到远程
    
    git push -u origin master
###二次提交
自动同步
将本地库与远程仓库同步
    
    git pull
把本地库的内容推送到远程
    
    git push
手动解决本地与远程仓库的冲突
把文件添加到版本库中，使用命令 git add .添加到暂存区里面去，不要忘记后面的小数点“.”，意为添加文件夹下的所有文件
    
    git add .
用命令 git commit告诉Git，把文件提交到仓库。引号内为提交说明(可以写提交时间)
    
    git commit -m 'other commit'  
将本地库与远程仓库同步
    
    git pull
使用VScode的版本管理工具手动进行文件同步
    
重新提交
    
    git add .
    git commit -m 'merged commit'  
上传远程仓库

    git push -u origin master
