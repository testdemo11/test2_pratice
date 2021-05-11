# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from setuptools import setup
setup(
    name='pytest_encode',
    url='https://github.com/xxx/pytest-encode',
    version='1.0',
    author="tnew",
    author_email='tnew_tao@163.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[# 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages=['pytest_encode'],
    keywords=[
        'pytest', 'py.test', 'pytest_encode',
    ],

    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 入口模块 或者入口函数
    entry_points={
        'pytest11': [
            'pytest-encode = pytest_encode',
        ]
    },
    zip_safe=False
)
