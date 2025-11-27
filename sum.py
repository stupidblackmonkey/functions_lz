
def popa(list):
    
    sum = 0
    for y in list:
        sum += y
    return sum

def main():
    qw = input("Введите числа через пробел: ")
    list = []
    for x in qw.split():
        list.append(int(x))
    pa = popa(list)
    print (pa)
if __name__ == '__main__':
    main()