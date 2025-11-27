
def tempa (a):
    b = ((a * 9 ) / 5) + 32
    return (b)

def main():
    a = int(input('введите температуру в градусах цельсия :'))
    ba = tempa(a)
    print("Температура по фаренгейту" , ba)

if __name__ == '__main__':
    main()