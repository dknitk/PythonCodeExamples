# Pattern program

def pattern1(level):
    '''
    *
    * *
    * * *
    * * * *
    :param level:
    :return:
    '''
    for i in range(1, level+1):
        print()
        for j in range(i):
            print('*', end='')

def pattern2(level):
    '''
    ****
    ***
    **
    *
    :param level:
    :return:
    '''
    for i in range(level, 0, -1):
        print()
        for j in range(i):
            print('*', end='')

if __name__=='__main__':
    print('----- Pattern 1 ------')
    pattern1(5)
    print('\n----- Pattern 2 ------')
    pattern2(5)