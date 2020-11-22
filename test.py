def StrOfSize(size):
    '''
    递归实现，精确为最大单位值 + 小数点后三位
    '''
    def strofsize(integer, remainder, level):
        if integer >= 1024:
            remainder = integer % 1024
            integer //= 1024
            level += 1
            return strofsize(integer, remainder, level)
        else:
            return integer, remainder, level

    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    integer, remainder, level = strofsize(size, 0, 0)
    #print(integer, remainder, level)
    if level+1 > len(units):
        level = -1
    return ('{}.{:>03d} {}'.format(integer, remainder, units[level]))


#bbb = StrOfSize(100045)







