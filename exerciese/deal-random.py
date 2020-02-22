import sys
def main():
    res = []
    while True:
        origin = set()
        try:
            n = sys.stdin.readline()
            for i in range(n):
                origin.add(int(sys.stdin.readline()))
            origin = list(origin)
            origin.sort()
            res = res + origin
        except Exception as e:
            print(e)
            break
    for i in res:
        print(i)

main()
