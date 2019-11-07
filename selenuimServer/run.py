import unittest, os, sys
import multiprocessing
import HTMLTestRunner

#运行目录一
dir1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res\\')

#运行目录二
dir2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res2\\')

def startrun(file):

    discover = unittest.defaultTestLoader.discover(start_dir="{}".format(file), pattern='test*.py', )

    runner = unittest.TextTestRunner()
    runner.run(discover)

if __name__ == "__main__":
    listdir = [dir1, dir2]

    process = []

    for i in listdir:

        t = multiprocessing.Process(target=startrun, args=(i,))
        process.append(t)

    for i in range(len(listdir)):
        process[i].start()

    # for i in range(len(listdir)):
    #     process[i].join()