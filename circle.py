
def krug(b):
    cm = b
    m = b / 100
    return("длина круга в см:" ,  cm , "в м:" , m)
def skrug(c):
    cm = c
    m = c / 10000
    return("площадь круга в см:" ,  cm , "в м:" , m)
def po(b , c):
    print (krug(b))
    print (skrug(c))

def main():
    a = int(input('введи радиус круга :'))
    b = a * 3.14 * 2
    c = 3.14 * a * a
    po(b, c)

if __name__ == '__main__':
    main()