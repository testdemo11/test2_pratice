# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from flask import Flask, request, jsonify, json
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost:3306/testcase?charset=utf8mb4'
db = SQLAlchemy(app)
api = Api(app)


# 第一种方式存储数据，[]
# testcases = []
# #自定义类的数据，json序列化有问题，需要让它继承dict,字典可以解析成json格式
# class TestCase(dict):
#     def __init__(self,name,des,steps):
#         self['name'] = name
#         self['des'] = des
#         self['steps'] = steps

# 第二种方式通过数据库来存放数据
class TestCase(db.Model):
    # __tablename__ = 'testcase'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    des = db.Column(db.String(120), unique=False, nullable=True)
    steps = db.Column(db.String(1024), unique=False, nullable=True)

    # def __init__(self, username, email):
    #     self.name = username
    #     self.email = email

    def __repr__(self):
        return '<TestCase %r>' % self.name
        # return {
        #     'name': self.name,
        #     'des': self.des,
        #     'steps': self.steps
        # }


class TestCaseService(Resource):
    def get(self):
        """
        获取所有的接口测试用例或者单个测试用例，返回json结构体
        :return:
        """
        testcases = [str(item) for item in TestCase.query.all()]
        return jsonify(testcases)

    def post(self):
        """
        新增测试用例或者修改测试用例,大部分会用post来代替put
        :return:
        """
        print('testtest')
        print(request.args)
        app.logger.info(request.args)
        if 'name' in request.args:
            print('update')
            print(request.json)
            print(request.json.get('name'))
            testcase = TestCase.query.filter_by(name=request.json.get('name')).first()
            print(testcase.des)
            print(testcase.steps)
            print('testcase')
            print(testcase)
            testcase.des = request.json.get('des')
            testcase.steps = json.dumps(request.json.get('steps'))
            print('after')
            print(testcase.des)
            print(testcase.steps)
            db.session.add(testcase)
            db.session.commit()
            # testcases = [str(item) for item in TestCase.query.all()]
            # print('测试用例')
            # print(testcases)
            # for i in range(len(testcases)):
            #     if 'name:'+ request.args['name'] == testcases[i]:
            #         app.logger.info(request.json)
            #         testcases[i] = request.json
            #         db.session.add(testcases)
            #         db.session.commit()
        else:
            app.logger.info(request.json)
            print('add')
            testcases = TestCase(**request.json)
            testcases.steps = json.dumps(request.json.get('steps'))
            app.logger.info(testcases)
            # testcases.append(testcase)
            db.session.add(testcases)
            db.session.commit()

        return {
            'msg': 'ok',
            'errcode': 0
        }

    def delete(self):
        """
        删除特定用例
        :return:
        """
        testcase = TestCase.query.filter_by(name=request.args.get('name')).first()
        app.logger.info(testcase)
        db.session.delete(testcase)
        db.session.commit()
        # if 'name' in request.args:
        # for item in testcases:
        #     if item['name'] == request.args['name']:
        #         testcases.remove(item)
        return {
            'msg': 'ok',
            'errcode': 0
        }

    def put(self):
        """
        新增测试用例，或者修改测试用例，有时候会通过post来代替put
        :return:
        """


api.add_resource(TestCaseService, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)
