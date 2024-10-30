#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
sys.path.append(os.path.join(os.getcwd(), "selenium_project"))
import random
import pytest
from utils.logger import log
from common.readconfig import ini
from page_object.jforumpage import jforumPage
from config.conf import cm

class Testjforum:
    @pytest.fixture(scope='module', autouse=True)
    def open_baidu(self, drivers):
        """打开jforum地址"""
        jforum = jforumPage(drivers)
        jforum.get_url(ini.url)

    def test_001(self, drivers):
        """登录操作"""
        jforum = jforumPage(drivers)
        jforum.click_login()
        jforum.input_username("admin")
        jforum.input_password("123456")
        jforum.click_submit_login()
        log.info("登录成功....")
        # assert drivers.title == 'Example Domain'

    def test_002(self, drivers):
        """进入板块回复帖子"""
        jforum = jforumPage(drivers)
        jforum.click_plate()
        jforum.click_article()
        jforum.click_Reply_article()
        content = ''.join(i for i in random.sample(\
            'zyxwvutsrqponmlkjihgfedcbaABCDEFGHIJKLMNOPQRSTUVWX', random.randint(10, 30)))
        jforum.input_article_content(f"{content}")
        jforum.click_article_content()
        log.info("回复帖子成功....")

    def test_003(self, drivers):
        """注销操作"""
        jforum = jforumPage(drivers)
        jforum.click_logout()
        log.info("注销成功....")

if __name__ == '__main__':
    test_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_jforum.py")
    pytest.main([test_file, "-vs", f"--html={cm.REPORT_FILE}/report.html"])

