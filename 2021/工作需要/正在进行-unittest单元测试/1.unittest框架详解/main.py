单元测试框架对比
python(80%):unittest30%,pytest
java(20%):junit,testng

关于unittest和pytest的差异
1.用例编写差异
unittest用例规则(内置的)
1.测试文件必须导包:import unittest
2.测试类必须继承unittest.Testcase
3.测试方法必须以test_开头


pytest用例规则(第三方库)
1.测试文件必须以test_开头或者_test结尾
2.测试类名必须以Test开头
3.测试方法必须以test_开头

测试用例的夹具
unittest:
setUp/tearDown 在测试用例之前和之后执行
setUpClass/tearDownClass 在测试类之前和之后执行
setUpModule/teardownModule 在测试模块之前和之后执行

pytest
setup/teardown 在测试用例之前和之后执行
setup_class/teardown_class 在测试类之前和之后执行
setup_module/teardown_module 在测试模块之前和之后执行
还有其他夹具:@pytest.fixtrue()

断言:
unitest:self.assertEqual() self.assertIn()
pytest:python自带的asseet

报告:
unittest:HtmlTestrunner.py
pytest:pytest-html,allure插件

失败重跑:
unittest没有
pytest:pytest-rerunfaiilures

参数化:
unittest:ddt
pytest:@pytest.mark.parametrize()

四.unittest重要组件
TestCase测试用例:最小单元,业务逻辑
TestSuite测试套件:一组测试用例的集合,或者测试套件的集合
TestFixtrue测试夹具:执行测试用例之前和之后的操作
TestLoader测试加载器:加载测试用例
TestRunner测试运行器:运行指定的测试用例

五.unittest实例

为什么没有main方法也可以运行呢?
unittest运行方式有两种:
1.命令行的运行方式(默认的测试用例的运行方式)
方式1:python -m unittest 模块名.py
方式2:python -m unittest 模块名.类名.方法

python -m 的意思:以脚本的方式来运行测试用例
方式3:python -m unittest -v 模块名.py
-v(verbose)详细的
方式4:python -m unittest -v 模块名.py -k*_weiwei
-k通过通配符匹配方法名

2.通过main运行
if __name__=="__main":
    unittest.main()

六.unittest的测试用例运行结果
.成功
F失败
E错误
S用例跳过

不能通过-v的方式运行,因为这是详细的报错方式,不是简介的报错方式

七.unittest测试用例的执行顺序规则
以ASCII的编码的大小排序[0-9,A-Z,a-z]
通过ord("a")查看ASCII码

八.多种unittest的加载和运行测试用例
1.main方法
2.通过测试套件来加载和运行

3.加载一个目录下所有的测试用例
if __name__="__main__":
    suite=unittest.defaultTestLoader.discover('./1.unittest框架详解',pattern='*.py')
    suite=unittest.defaultTestLoader.discover('./1.unittest框架详解',pattern='test_unittest.py')
    unittest.main(defaultTest='suite')


