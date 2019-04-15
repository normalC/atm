"""
http://www.cnblogs.com/alex3714/articles/5161349.htmljson & pickle 模块
用于序列化的两个模块

要实现的功能	可以使用的api
将Python数据类型转换为（json）字符串	json.dumps()
将json字符串转换为Python数据类型	json.loads()
将Python数据类型以json形式保存到本地磁盘	json.dump()
将本地磁盘文件中的json数据转换为Python数据类型	json.load()
将Python数据类型转换为Python特定的二进制格式	pickle.dumps()
将Python特定的的二进制格式数据转换为Python数据类型	pickle.loads()
将Python数据类型以Python特定的二进制格式保存到本地磁盘	pickle.dump()
将本地磁盘文件中的Python特定的二进制格式数据转换为Python数据类型	pickle.load()
以类型dict的形式将Python数据类型保存到本地磁盘或读取本地磁盘数据并转换为数据类型	shelve.open()


"""


import json

info = {"name": "Alex", "age": 22}

with open('info.json', 'w', encoding='utf-8') as f:
    print(type(json.dumps(info)))  # <class 'str'>
    json.dump(info, f)  # 高级做法2，同上


with open('info.json', 'r', encoding='utf8') as f:
    # data=json.loads(f.read())
    data = json.load(f)  # 同上
    print(data["age"])

# pickle写进文件中的貌似是一段乱码，其实不然，这是pickle自己的一套语法规则，当然这也不是加密
# pickle可以序列化所有的数据类型
# 但是pickle只能在Python中使用，别的语言不认识它

import pickle


def sayhi(name):
    print("Hello ",name)


info1 = {"name": "Alex", "age": 22, 'func':sayhi}

with open('info1.pk', 'wb') as f:
    print(type(pickle.dumps(info1)))  # <class 'bytes'>
    f.write(pickle.dumps(info1))  # sayhi是一个内存地址，用json序列化就写不到文件中，会报错

import pickle

# def sayhi(name):
#     print("Hello2 ",name)

with open('info1.pl', 'rb') as f:
    data = pickle.loads(f.read())  # 报错
    print(data)
    # data["func"]('alex')
# AttributeError: Can't get attribute 'sayhi' on <module '__main__' from 'D:/python-study/s14/Day04/pickle反序列化.py'>
# 为什么报错呢？因为sayhi是一个内存地址，当pickle序列化.py程序执行完之后，这个地址就被释放了，当然我们就找不到了。
# 这里只是想说明一点：pickle可以序列化所有的数据类型，不管这个数据是否可被反序列化
# 如果想要不报错，可以把sayhi函数的定义拷贝过来，而且还可以执行这个函数
# 只要保证函数名相同就不会报错，函数体可以完全不一样


import json

# Python3.x中input方法获取到的都是字符串，相当于Python2.x中的raw_input
inp_str = input("请输入：")  # 输入一个列表，[1,2,3]
print(type(inp_str))  # <class 'str'>
inp_str = json.loads(inp_str, encoding="UTF-8")  # 根据字符串书写格式，将字符串自动转换成 列表类型
print(type(inp_str), inp_str[0])  # <class 'list'> 1

inp_str = input("请输入：")  # 输入一个字典，{"name":"Rose","age":21,"sex":"F"}
# 切记，字典内部必须是 双引号 ！！！单引号会报错。
print(type(inp_str))  # <class 'str'>
inp_str = json.loads(inp_str, encoding="UTF-8")  # 根据字符串书写格式，将字符串自动转换成 字典类型
print(type(inp_str), inp_str['name'], inp_str['age'], inp_str['sex'])  # <class 'dict'> Rose 21 F


OS模块
os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
os.curdir  返回当前目录: ('.')
os.pardir  获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')    可生成多层递归目录
os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  删除一个文件
os.rename("oldname","newname")  重命名文件/目录
os.stat('path/filename')  获取文件/目录信息
os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep    输出用于分割文件路径的字符串
os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  运行shell命令，直接显示
os.environ  获取系统环境变量
os.path.abspath(path)  返回path规范化的绝对路径
os.path.split(path)  将path分割成目录和文件名二元组返回
os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  如果path是绝对路径，返回True
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间


sys模块

sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxint         最大的Int值
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]