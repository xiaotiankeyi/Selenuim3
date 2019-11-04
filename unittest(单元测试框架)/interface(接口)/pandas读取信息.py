import requests
import unittest
import pandas as pd


class Apitest(unittest.TestCase):
    file_dir = r"C:\Users\admin\Desktop\showdata.xlsx"
    df = pd.read_excel(file_dir, sheet_name='APIcase')

    test_dict = []
    for i in df.index.values:
        row_data = df.loc[i, ['Host', 'RequestUrl', 'Method',
                              'RequestData', 'verifyResultID', 'verifyResultName']].to_dict()
        test_dict.append(row_data)

    def test_noe_api(self):

        for i in range(0, len(self.test_dict)):
            print(i)
            url = self.test_dict[i]['Host']

            data = eval(self.test_dict[i]['RequestData'])

            response = requests.request("GET", url, params=data).json()
            print(response)
            assert (response['id'], self.test_dict[i]['verifyResultID'])
            assert (response['name'], self.test_dict[i]['verifyResultName'])

            print(response['id'], '\t', response['name'])


if __name__ == "__main__":
    unittest.main()
