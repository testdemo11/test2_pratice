# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import requests

from pratice_lesson17.backend.backend import db, TestCase


def test_testcase_get():
    r = requests.get('http://127.0.0.1:5000/testcase')
    size = len(r.json())
    assert r.status_code == 200


def test_testcases_addcase():
    r = requests.get('http://127.0.0.1:5000/testcase')
    size = len(r.json())
    print(size)
    r = requests.post("http://127.0.0.1:5000/testcase",
                      json={
                          'name':'demo1',
                          'des':'des1',
                          'steps':['1','2']
                      })
    assert r.status_code == 200
    r = requests.get('http://127.0.0.1:5000/testcase')
    size_new = len(r.json())
    print(size_new)
    # r = requests.post("http://127.0.0.1:5000/testcase",
    #                   json={
    #                       'name': 'demo1',
    #                       'des': 'des1',
    #                       'steps': ['1', '2']
    #                   })
    assert r.status_code == 200
    assert size_new == size + 1

def test_testcase_update():
    r = requests.get('http://127.0.0.1:5000/testcase')
    size = len(r.json())
    print(size)
    r = requests.delete("http://127.0.0.1:5000/testcase",
                        params={'name': 'demo2'})
    r = requests.post("http://127.0.0.1:5000/testcase",
                      json={
                          'name': 'demo2',
                          'des': 'des1',
                          'steps': ['1', '2']
                      })
    assert r.status_code == 200
    r = requests.get('http://127.0.0.1:5000/testcase')
    size_new = len(r.json())
    r = requests.post("http://127.0.0.1:5000/testcase",
                      params={'name':'demo2'},
                      json={
                          'name': 'demo2',
                          'des': 'des2',
                          'steps': ['ee', '2e']
                      })
    size_latest = len(r.json())
    print(size_latest)
    r = requests.get('http://127.0.0.1:5000/testcase')
    assert r.status_code == 200


def test_testcase_delete():
    r = requests.get('http://127.0.0.1:5000/testcase')
    size_original= len(r.json())
    print(size_original)
    r = requests.post("http://127.0.0.1:5000/testcase",
                      json={
                          'name': 'demo3',
                          'des': 'des2',
                          'steps': ['ee', '2e']
                      })
    r = requests.get('http://127.0.0.1:5000/testcase')
    size_new = len(r.json())
    print(size_new)
    assert size_new == size_original + 1
    r = requests.delete("http://127.0.0.1:5000/testcase",
                      params={'name':'demo3'})


    r = requests.get('http://127.0.0.1:5000/testcase')
    size_latest = len(r.json())
    print(size_latest)
    assert r.status_code == 200
    assert size_latest == size_original

def test_db():
    #新建表，连接的数据库必须提前新建好
    db.create_all()
    #查询第一条数据
    testcase = TestCase.query.first()
    print(testcase)

    testcase_add = TestCase()
    testcase_add.name ='t'
    testcase_add.des = 'test'
    testcase_add.steps = 'iiii'

    db.session.add(testcase_add)
    db.session.commit()

    print(TestCase.query.all())