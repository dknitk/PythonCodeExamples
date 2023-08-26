
# Program to test variable
x = 'Global x'

def test():
    y = 'Local Y'
    x = 'Local X'
    print(x + ' , ' + y)

if __name__ == '__main__':
    test()
    print(x)