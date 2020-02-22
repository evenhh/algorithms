import sys
def main():
    w_arr = []
    while True:
        try:
            n = int(sys.stdin.readline().strip())
            for i in sys.stdin.readline().strip().split():
                w_arr.append(int(i))
            i = 0
            for j in sys.stdin.readline().strip().split():
                if int(j) == 1:
                    w_arr[i] = 1
                i = i + 1
            if sys.stdin.readline() == '':
                break
        except:
            break
    x = 0
    while x<n-1:
        z = x + 1
        if w_arr[x] ==1 and w_arr[z] ==1:
            w_arr[z] = 0
            print(w_arr[z])
        x = x + 1
    print(n-sum(w_arr))

main() 
