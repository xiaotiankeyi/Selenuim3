#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
sys.path.append(os.path.join(os.getcwd(), "selenium_project"))
import configparser
from config.conf import cm

HOST = 'HOST'


class ReadConfig(object):
    """配置文件"""

    def __init__(self):
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(cm.ini_file, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)

    def alter(self,aection, option,value):
        self._set(aection, option, value)
    
ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)
    # ini._set(aection=HOST, option=HOST, value="http://192.168.137.78:8080/jforum-2.8.3/forums/list.page")
    # print(ini.url)
    ini.alter(aection=HOST, option=HOST, value="https://www.baidu.com")
    print(ini.url)

