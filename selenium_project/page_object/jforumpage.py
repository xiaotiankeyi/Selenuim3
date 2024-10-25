#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
sys.path.append(os.path.join(os.getcwd(), "selenium_project"))

from page.webpage import WebPage
from utils.times import sleep
from common.readelement import Element

search = Element('jforum')


class jforumPage(WebPage):
    """登录-进入版本-查看帖子-返回首页-注销"""
    def click_login(self):
        """点击登录,进入登录页面"""
        self.is_click(search['登录'])
        sleep()

    def input_username(self, content):
        """输入会员名称"""
        self.input_text(search['会员名称'], txt=content)
        sleep()

    def input_password(self, content):
        """输入会员密码"""
        self.input_text(search['登录密码'], txt=content)
        sleep()

    def click_submit_login(self):
        """点击提交登入"""
        self.is_click(search['提交登入'])
        sleep()

    def click_plate(self):
        """点击进入板块"""
        self.is_click(search['进入版块'])
        sleep()
    
    def click_article(self):
        """点击进入帖子"""
        self.is_not_element_click(search['进入帖子'])
        sleep()

    def click_Reply_article(self):
        """点击回复帖子"""
        self.is_not_element_click(search['进入回复文章页'])
        sleep()

    def input_article_content(self, content):
        """输入回复内容"""
        self.input_text(search['输入回复内容'], txt=content)
        sleep()

    def click_article_content(self):
        """提交回复内容"""
        self.is_click(search['提交回复内容'])
        sleep(3)

    def click_logout(self):
        """点击注销"""
        self.is_click(search['注销'])
        sleep()


if __name__ == "__main__":
    obj = jforumPage()