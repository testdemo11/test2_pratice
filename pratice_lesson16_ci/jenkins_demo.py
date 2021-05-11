# -*- coding:utf-8 -*-
__author__ = 'Tnew'
import logging
import datetime
import os,re
import configparser
from jenkinsapi.jenkins import Jenkins
# logging.basicConfig(level=logging.INFO,format='%(ascitime)s-%(name)s-%(levelname)s:%(message)s')
# logger=logging.getLogger(__name__)

# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

logger = logging.getLogger('mylogger')
fh = logging.FileHandler('logfile')
formatter = logging.Formatter('%(ascitime)s-%(name)s-%(levelname)s:%(message)s')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)


def get_jk_config(chose):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getcwd(),'jenkins_server.ini'))
    username = config.get(chose,'username')
    password = config.get(chose,'password')
    host = config.get(chose, 'host')
    port = config.get(chose,'port')
    url = 'http://'+host+":"+port
    return url,username,password

class JenkinsDemo:
    def __init__(self,job_name,chose='jenkins'):
        self.job_name = job_name
        config = get_jk_config(chose)
        self.jk = Jenkins(*config,useCrumb=True)

    def __get_job_from_keys(self):
        choose_list = []
        print(self.jk.keys())
        for my_job_name in self.jk.keys():
            if self.job_name in my_job_name:
                choose_list.append(my_job_name)
        return choose_list

    def __job_build(self,my_job_name):
        if self.jk.has_job(my_job_name):
            my_job = self.jk.get_job(my_job_name)
            if not my_job.is_queued_or_running():
                try:
                    last_build = my_job.get_last_buildnumber()
                except:
                    last_build = 0
                build_num = last_build+1

                #开始打包
                try:
                    self.jk.build_job(my_job_name)
                    logger.info("开始构建")
                except Exception as e:
                    logger.error(str(e))

                #循环判断jenkins是否打包完成
                while True:
                    if not my_job.is_queued_or_running():
                        count_build = my_job.get_build(build_num)
                        start_time = count_build.get_timestamp()
                        # start_time = count_build.get_timestamp()+ datetime.timedelta(hours=8)
                        console_out = count_build.get_console()
                        status = count_build.get_status()
                        change = count_build.get_changeset_items()
                        logger.info(" "+str(start_time)+"发起的"+my_job_name+"构建已经完成")
                        p2= re.compile(r".*ERROR.*")
                        err_list=p2.findall(console_out)
                        logger.info("打包日志为："+str(console_out))
                        if status == "SUCCESS":
                            if len(change) > 0:
                                for data in change:
                                    for file_list in data['affectedPaths']:
                                        logger.info("发起的"+my_job_name+"变更的类："+file_list)
                                    logger.info("发起的" + my_job_name + "变更的备注：" + data["msg"])
                                    logger.info("发起的" + my_job_name + "变更的提交人：" + data["author"]["fullName"])
                            else:
                                logger.info("发起的" + my_job_name + "没有变更内容")
                            if len(err_list) > 0:
                                logger.warning("构建的"+my_job_name+"构建成功，但包含以下错误: ")
                                for err in err_list:
                                    logger.error(err)
                        else:
                            if len(err_list) > 0:
                                logger.warning("构建的" + my_job_name + "包含以下错误: ")
                                for err in err_list:
                                    logger.error(err)
                        break
            else:
                        logger.warning("发起的" + my_job_name + "Jenkins is running")
        else:
                    logger.warning("发起的" + my_job_name + "没有该服务")


    def run(self):
        my_job_name = self.__get_job_from_keys()
        if len(my_job_name) == 1:
            self.__job_build(my_job_name[0])
        elif len(my_job_name) ==0:
            logger.error("输入的job名不正确")

class TestJenkinsDemo:
    def test_jenkins(self):
        self.jk = JenkinsDemo('test')
        self.jk.run()
