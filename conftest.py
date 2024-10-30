#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import base64
import pytest
from py.xml import html # type: ignore
from selenium import webdriver
import pytest_html
from selenium_project.config.conf import cm

driver = None


@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        # driver.maximize_window()
        # drivers.set_window_size(1024, 768)
    def fn():
        driver.quit()
    request.addfinalizer(fn)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    """
    当测试失败的时候,自动截图,展示到html报告中
    :param item:
    """
    # pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extras = getattr(report, 'extras', [])

    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            screen_img = _capture_screenshot(item.name)
            if screen_img:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extras.append(pytest_html.extras.html(html))
        report.extras = extras

def pytest_html_report_title(report):
    """报告标题title"""
    report.title = "jforum项目ui自动化测试"


def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('casename'))

def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))


def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append("<div class='empty log'>No log output captured.</div>")


def _capture_screenshot(test_name):
    """拍摄屏幕截图并返回 Base64 编码的字符串"""
    file_path = os.path.join(cm.failed_img, f"{test_name}.png")
    driver.save_screenshot(file_path)

    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')


def pytest_html_results_summary(prefix, summary, postfix):
    # 添加自定义前缀信息
    prefix.extend(["<p>前缀: Ui自动化测试</p>"])

    # 获取统计信息
    passed = getattr(summary, 'passed', 0)
    failed = getattr(summary, 'failed', 0)
    skipped = getattr(summary, 'skipped', 0)

    # 添加汇总信息
    summary_info = f"<p>测试结果: 已通过 {passed} 测试, 失败 {failed}, 跳过 {skipped}</p>"
    
    # 确保 summary 是可扩展的
    summary.append(summary_info)

    # 添加自定义后缀信息
    postfix.extend(["<p>后缀: 测试完成，感谢您的查看!</p>"])
