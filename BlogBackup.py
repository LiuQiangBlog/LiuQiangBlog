import os

def git_operation():
    '''
    git 命令行函数，将仓库提交
    
    ----------
    需要安装git命令行工具，并且添加到环境变量中
    '''


    #首次运行
    #os.system('echo "This is my backup repository of blog photos!" >> README.md')
    #os.system('git init')
    #os.system('git add --all')
    #os.system('git commit -m "first commit"')
    #os.system('git remote add origin https://github.com/LiuQiangBlog/BlogBackup.git')
    #os.system('git push -u origin master')


    #后续运行
    os.system('git add --all')
    os.system('git commit -m "update LiuQiangBlog"')
    os.system('git remote add origin https://github.com/LiuQiangBlog/LiuQiangBlog.git')
    os.system('git push origin master')


if __name__ == "__main__":
    git_operation()    # 提交到github仓库
