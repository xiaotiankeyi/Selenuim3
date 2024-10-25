from one import count

class test_count():
    def start(self):
        try:
            obj = count(3, 5)
            accept = obj.count_digit()
            assert (accept == 10), 'test failed'
        except AssertionError as e:
            print(e)
        else:
            print('test succeed')


if __name__ == "__main__":
    test_count.start('obj')