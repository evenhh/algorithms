import sys

def main():
    while True:
        res = []
        try:
            n = sys.stdin.readline()
            if n == '':
                break
            n = int(n)
            a = [ i for i in range(n) ]
            index=0
            out=1
            while len(a)>1:
                if index==len(a):
                    index=0
                if out == 3:
                    a.pop(index)
                    out = 0
                    index -= 1
                index +=1
                out +=1
            print(a[0]+1)
        except Exception as e:
            print(e)
            break   


main() 
