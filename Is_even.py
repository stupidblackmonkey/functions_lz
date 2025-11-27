
def pro(a):
    if a == 0:
        print (a , "- это ноль" )
    elif a % 2 == 0:
        print (a , "- Четное число" )
    else:
        print (a, "- Не чётное число")
    return (a)

def main():
    a = int(input("Введите любое число: "))
    pro(a)

if __name__ == '__main__':
    main()