def main():
    n = int(input("ENTER A 4 - DIGIT NUMBER :- "))
    print(sum(n))

def sum(n):
    s=0
    while n!=0:
        rem = n % 10
        if rem % 2== 0:
            s+= rem

        n = n//10

    return s

main()
