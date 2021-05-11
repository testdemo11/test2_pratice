import pytest
import yaml

from pratice.demo.calc import Calculator

with open("./datas/calc_demo.yaml") as f:
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


class TestCalculator:
    def setup(self):
        print("开始计算")
        #实例化计算器类
        self.calc = Calculator()

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect",add_datas)
    # @pytest.mark.parametrize("a,b,expect", add_datas, ids=add_id)
    def test_add(self,a,b,expect):
        # 假设最大能输入999999999
        if a > 999999999:
            print("超出最大数值999999999，不允许输出")
            assert False
        # 假设最小能输入-999999999
        elif a < -999999999:
            print("超出最小数值-999999999，不允许输出")
            assert False
        # 假设最大能输入999999999
        elif b > 999999999:
            print("超出最大数值999999999，不允许输出")
            assert False
        # 假设最小能输入-999999999
        elif b < -999999999:
            print("超出最小数值-999999999，不允许输出")
            assert False
        else:
            #调用add方法
            result = self.calc.add(a,b)
            #假设最大能输入999999999
            if result > 999999999:
                print("超出最大数值999999999，不允许输出")
                assert False
            # 假设最小能输入-999999999
            elif result < -999999999:
                print("超出最小数值-999999999，不允许输出")
                assert False
            else:
                if isinstance(result, float):
                    # 浮点型的计算，是二进制运算，可能会丢位，所以可以使用round方法处理浮点数，强制保留2位数
                    result = round(result, 2)
                #断言判断
                assert result == expect

    # @pytest.mark.parametrize("a,b,expect",div_datas,ids= div_id)
    @pytest.mark.parametrize("a,b,expect", div_datas)
    def test_div(self,a,b,expect):
        #判断除数是否为0，为0不能除
        if b == 0:
            print("b为除数，不可以为0")
            assert False
        #判断被除数是否为0，为0，除数任意数都是为0（除数0除外）
        elif a == 0:
            result = self.calc.div(a, b)
            assert result == 0
        elif a > 999999999:
            print("超出最大数值999999999，不允许输出")
            assert False
        # 假设最小能输入-999999999
        elif a < -999999999:
            print("超出最小数值-999999999，不允许输出")
            assert False
        # 假设最大能输入999999999
        elif b > 999999999:
            print("超出最大数值999999999，不允许输出")
            assert False
        # 假设最小能输入-999999999
        elif b < -999999999:
            print("超出最小数值-999999999，不允许输出")
            assert False
            # 判断a和b是否相等，相等，任意数除完结果都是1（除数0除外）
        elif a == b:
            # 调用div方法
            result = self.calc.div(a, b)
            # result = int(result)
            assert result == 1
        else:
            result = self.calc.div(a, b)
            # 假设最大能输出999999999
            if result >999999999:
                print("超出最大数值999999999，不允许输出")
                assert False
            # 假设最小能输出-999999999
            elif result < -999999999:
                print("超出最小数值-999999999，不允许输出")
                assert False
            else:
                if isinstance(result,float):
                    result = round(result,2)
                assert result == expect