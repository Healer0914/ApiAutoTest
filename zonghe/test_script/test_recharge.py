'''
测试充值的脚本
'''
import pytest

from zonghe.caw import DataRead


@pytest.fixture(params=DataRead.read_yaml(r"test_data\recharge.yaml"))
def recharge_data(request):
    return request.param

def test_recharge(register_data,baserequest,urlt):
    pass


