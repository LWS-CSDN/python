class Person:
    """
    关于这个类的描述,类的作用,类的构造函数等等
    """
    #这个表示,是人的个数
    def run(self):
        """
        描述
        """
        print("人在跑")
# 生成项目文档
# 方式1
# 使用内置模块pydoc
# 具体步骤
# 查看文档描述python3 -m pydoc 模块名称(模块名称不带.py后缀)
# 启动本地服务,浏览文档 python3 -m pydoc -p 6666(手动选择端口,本地开放端口,如果被占用了换其他的)
# python3 -m pydoc -b(自动分配端口)
# 生成指定模块html文档 python3 -m pydoc -w 模块名称