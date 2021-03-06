'''
fixture 类级别的
'''
import pytest

@pytest.fixture(scope='class')
def db():
    print("前置：连接数据库")
    yield
    print("后置：断开数据库连接")

@pytest.fixture(scope='class')
def login():
    print("前置：在首次调用login的地方执行前置")
    yield
    print("后置：模块所有用例执行完执行后置")

class TestRegister:
    def test_001(self):
        print("注册用例1")
    def test_002(self,db): # 类里面，首次调用db的地方执行前置
        print("注册用例2")
    def test_003(self):
        print("注册用例3")  # 类里面所有用例执行完，执行后置


class TestLogin:
    def test_001(self,login): # login的前置
        print("登录用例1")
    def test_002(self,db,login): # db的前置
        print("登录用例2")
    def test_003(self):
        print("登录用例3") # login、db的后置
