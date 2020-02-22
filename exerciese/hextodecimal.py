import sys
def main():
    inputs = []
    while True:
        try:
            inputs.append(sys.stdin.readline())
        except:
            break
    for i in inputs:
        print(int(i,16))
    
    
main()
