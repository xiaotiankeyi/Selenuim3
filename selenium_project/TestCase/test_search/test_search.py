#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
sys.path.append(os.path.join(os.getcwd(), "selenium_project"))
import re
import pytest
from utils.logger import log
from common.readconfig import ini
from page_object.searchpage import SearchPage


class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_baidu(self, drivers):
        """打开百度"""
        search = SearchPage(drivers)
        search.get_url("https://www.baidu.com")

    def test_001(self, drivers):
        """搜索"""
        search = SearchPage(drivers)
        search.input_search("selenium")
        search.click_search()
        result = re.search(r'selenium', search.get_source)
        log.info(result)
        assert result

    def test_002(self, drivers):
        """测试搜索候选"""
        search = SearchPage(drivers)
        search.input_search("selenium")
        log.info(list(search.imagine))
        assert all(["selenium" in i for i in search.imagine])


if __name__ == '__main__':
    test_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_search.py")
    pytest.main([test_file, "-vs"])

