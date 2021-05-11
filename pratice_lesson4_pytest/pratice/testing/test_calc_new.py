import allure
import pytest
import yaml



with open("./datas/calc.yaml") as f:
    # #获取yaml文件中add对应的数值
    data = yaml.safe_load(f)
    data_add = data["add"]
    # data_add = yaml.safe_load(f)["add"]
    add_datas = data_add['adddata']
    # add_id = data_add['addid']

    data_div = data["div"]
    # data_div = yaml.safe_load(f)["div"]
    div_datas = data_div['divdata']
    # div_id = data_div['divid']

@pytest.fixture(params=add_datas)
def get_datas(request):
    # print("开始计算")
    data = request.param
    # print(f"测试数据为{data}")
    yield data
    # print("结束计算")

@allure.feature("测试计算器")
class TestCalculator:
    """
     1 把setup 和teardown换成fixture方法get_calc
     2 把get_calc放到conftest.py
     3 把参数化换成了fixture参数化方式
     4 测试用例中的数据需要通过get_datas获取
      get_datas 返回了一个列表[0.1,0.2,0.3] 分别代表了a,b expect
    """
    # @pytest.mark.add
    # @pytest.mark.parametrize("a,b,expect",add_datas)
    # @pytest.mark.parametrize("a,b,expect", add_datas, ids=add_id)
    @allure.story("计算器的加法测试")
    @pytest.mark.run(order=1)
    def test_add(self,get_calc,get_datas):
        #调用add方法
        with allure.step("从计算器的加方法中得到加过的值"):
            result = get_calc.add(get_datas[0],get_datas[1])
        #假设最大能输入999999999
        if result>=1000000000:
            print("超出最大数值999999999，不允许输出")
            assert False
        # 假设最小能输入-999999999
        elif result<=-1000000000:
            print("超出最小数值-999999999，不允许输出")
            assert False
        else:
            if isinstance(result, float):
                # 浮点型的计算，是二进制运算，可能会丢位，所以可以使用round方法处理浮点数，强制保留2位数
                result = round(result, 2)
            #断言判断
            assert result == get_datas[2]

    # @pytest.mark.parametrize("a,b,expect",div_datas,ids= div_id)
    @pytest.mark.parametrize("a,b,expect", div_datas)
    def test_div(self,get_calc,a,b,expect):
        #判断除数是否为0，为0不能除
        if b == 0:
            print("b为除数，不可以为0")
            assert False
        #判断被除数是否为0，为0，除数任意数都是为0（除数0除外）
        elif a == 0:
            result = get_calc.div(a, b)
            assert result == 0
        #判断a和b是否相等，相等，任意数除完结果都是1（除数0除外）
        elif a == b:
            #调用div方法
            result = get_calc.div(a, b)
            # result = int(result)
            assert result == 1
        else:
            result = get_calc.div(a, b)
            # 假设最大能输出999999999
            if result >= 1000000000:
                print("超出最大数值999999999，不允许输出")
                assert False
            # 假设最小能输出-999999999
            elif result <= -1000000000:
                print("超出最小数值-999999999，不允许输出")
                assert False
            else:
                if isinstance(result,float):
                    result = round(result,2)
                assert result == expect