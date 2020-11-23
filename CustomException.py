class MyError(Exception):

    def __init__(self, value):
        self.value = value

    def __str_(self):
        return repr(self.value)


def main():
    try:
        a = -2
        if a < 0:
            raise MyError(f'{a} is less then or equal to 0')
        else:
            print(a)
    except MyError as error:
        print(error)


if __name__ == '__main__':
    main()
