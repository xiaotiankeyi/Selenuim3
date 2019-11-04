import unittest
import requests
from bs4 import BeautifulSoup


class Loginapi(unittest.TestCase):

    def test_login(self):
        url = "http://192.168.117.9/bbs/upload/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }
        data = {
            'fastloginfield': 'username',
            'username': 'admin',
            'password': 'admin',
            'quickforward': 'yes',
            'handlekey': 'ls'
        }

        seesion = requests.session()
        response = seesion.request('post', url, params=data, headers=headers, timeout=10, )
        # print(response.content.decode('utf8'))
        # print(response.cookies)

        url = "http://192.168.117.9/bbs/upload/forum.php"
        response2 = seesion.get(url)
        # print(response2.content.decode('utf8'))
        html = response2.text

        soup = BeautifulSoup(html, 'html.parser')
        tag = soup.find_all('a', string='退出')

        formhash = '{}'.format(tag).split('formhash=')

        h = formhash[1].split('">')[0]
        print(h)

        '''删帖'''
        data = {
            'frommodcp': '',
            'formhash': h,
            'fid': 37,
            'redirect': 'http://192.168.117.9/bbs/upload/forum.php?mod=viewthread&tid=7&extra=page%3D1',
            'listextra': 'page%3D1',
            'handlekey': 'mods',
            'moderate[]': 7,
            'operations[]': 'delete',
            'reason': 'delete',
        }
        url = "http://192.168.117.9/bbs/upload/forum.php?mod=topicadmin&action=moderate&optgroup=3&modsubmit=yes&infloat=yes&inajax=1"
        seesion.post(url, params=data, headers=headers)

        '''增贴'''
        data = {'formhash': h,
                'posttime': '1571266584',
                'wysiwyg': 1,
                'subject': 'dfsafjsgjsoigndasdasdasdjosngdsg',
                'message': 'sdgsdjgpisgsfs估计是假的dasdasddss',

                'replycredit_extcredits': 0,
                'replycredit_times': 1,
                'replycredit_membertimes': 1,
                'replycredit_random': 100,
                'readperm': '',
                'price': '',
                'tags': '',
                'rushreplyfrom': '',
                'rushreplyto': '',
                'rewardfloor': '',
                'replylimit': '',
                'stopfloor': '',
                'creditlimit': ''}

        url = "http://192.168.117.9/bbs/upload/forum.php?mod=post&action=newthread&fid=37&extra=&topicsubmit=yes"
        seesion.post(url, params=data, headers=headers)


if __name__ == "__main__":
    unittest.main()
