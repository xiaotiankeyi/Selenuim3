import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR + '\\public'))

from publicway import Publicclass
from mysql import datasql
import requests
import unittest
from bs4 import BeautifulSoup
from requests.cookies import RequestsCookieJar


class Loginapi(Publicclass):
    '''接口登录'''
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }

    url = "http://192.168.117.9:8080/jforum/jforum.page"

    data = {
        'module': 'user',
        'action': 'validateLogin',
        'returnPath': 'http://192.168.117.9:8080/jforum/forums/list.page',
        'username': 'admin',
        'password': 'admin',
        'redirect': '',
        'login': '登入'
    }

    def test_login(self):
        '''登录成功'''
        response = requests.request('post', self.url, params=self.data, headers=self.headers)
        cookie = RequestsCookieJar()
        print(response.cookies)

        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        login_text = soup.find('a', id='logout').get_text()
        try:
            assert login_text == ' 注销 [Admin]'
        except Exception as e:
            print(e)

    def test_del_post(self):
        """删除帖子测试..."""
        sql = "SELECT count(post_id) from jforum_posts;"
        accept = datasql(sql)
        # 获取删除操作前的帖子数
        front_data = accept[0]['count(post_id)']
        print(front_data)

        sql = "SELECT count(post_id) from jforum_posts;"
        accept = datasql(sql)
        # 获取删除操作前的帖子数
        back_data = accept[0]['count(post_id)']
        print(back_data)
        assert front_data > back_data


if __name__ == "__main__":
    unittest.main()
