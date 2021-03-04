def addup(total, index, max):

    total = total + index
    index = index + 1
    if index > max:
        return total
    else:
        return addup(total, index, max)

def consecutive_sum(num):
    if num == 1:
        print('consecutive_sum({0}) - return: {0}'.format(num))
        return 1
    else:
        print('consecutive_sum({0}) - return: {0} + consecutive_sum({1})'
                .format(num, num -1))
        return num + consecutive_sum(num - 1)

#print(addup(0, 1, 500))
print(consecutive_sum(10))

#### Questions:
# 1. calculate sum for concecutive even numbers.
# 
