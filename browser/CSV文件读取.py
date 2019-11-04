import csv

def file_dispose():
    with open(r"C:\Users\admin\Documents\csvfileread.csv", 'r') as f:
        print(f.name)
        data = csv.reader(f)
        print('获取对象,在循环取出',data)
        for i in data:
            print(i)
        f.close()
    print("=" * 50)

    data = csv.reader(open(r"C:\Users\admin\Documents\csvfileread.csv", 'r'))

    for message in data:
        print(message)

'''第二种操作方式'''
import pandas as pd
def pandasfunction():
    data = pd.read_csv(r"C:\Users\admin\Documents\csvfileread.csv", encoding='gbk')
    print(data)

    show_data = data.head()       #选择读取行,默认5行
    print('指定读取行为:\n{}'.format(show_data))

    self_data = data.loc[3].values       #指定读取第3行
    print('读取的指定行数据为:\n{}'.format(self_data))

    more_data = data.loc[[1, 5, 8]]        #指定读取多行, 1行, 5行, 8行, 在loc[]里面嵌套列表指定行数
    print('读取的多行数据为:\n{}'.format(more_data))

    self_row = data.iloc[6, 2]                     #使用位置索引iloc
    print('读取的行列为:\n{}'.format(self_row))

    more_row = data.loc[[3, 8], ['user', 'gender']].values      #指定读取多行多列值,
    print('读取的多行多列值为:\n{}'.format(more_row))

    all_row = data.loc[:,['Email','user']]              #获取所有行的指定列
    print('读取所有行的指定列为:\n{}'.format(all_row))

    row_id = data.index.values
    print('获取的行号为:\n{}'.format(row_id))

    list_id = data.columns.values
    print('获取的列名称为:\n{}'.format(list_id))

    self_list = data['Email'].values
    print('获取指定列的值为\n{}'.format(self_list))

pandasfunction()


from pandas import Series

def series():
    num = Series(['strip', 'split' 'replace','request', 'response'])
    print(num)
    print(num.index)
    print(num.values)
    print('=' * 50)

    '''自定义索引'''
    choice = Series(['split', 'extend', 'count', 'items'],index=['str', 'list', 'tuple', 'dict'])
    print(choice,)
    print( '根据索引获取{}'.format(choice['str']))
    print('=' * 50)

    sd = {'python':9000,'c++':9001,'c#':9000}
    s3 = Series(sd)
    print(s3)
    print('=' * 50)

    '''自动对齐'''
    s4 = Series(sd, index=['java', 'python', 'c++', 'javaScript', 'php'])
    print(s4)