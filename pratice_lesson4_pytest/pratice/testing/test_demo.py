import pytest
import yaml


# @pytest.mark.parametrize('a',yaml.safe_load('./datas/param_a.yaml'))
# @pytest.mark.parametrize('b',yaml.safe_load('./datas/param_b.yaml'))
@pytest.mark.parametrize('a',[2,1000,-3,-3000,0.5,2020.7,-1.7,-4000.8,0])
@pytest.mark.parametrize('b',[3,3300,-5,-6000,0.4,5080.6,-4.8,-6000.8,0])
def test_param(a,b):
    # print(f"a={a},b={b}")
    result = a + b
    print(f"{a}+{b}={result}" )
    res = []
    res.append(result)
    print(res)
    return result

# if __name__ == '__main__':
#     pytest.main('test_demo.py')