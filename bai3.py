def swap(num):
    check = True
    if num < 0:
        num = -num
        check = False
    sum = 0
    while num != 0:
        sum = sum*10 + num%10
        num //= 10
    if check:
        print(sum)
    else:
        print(-sum)
def main():
    num = int(input("Nhập số nguyên cần đảo ngược: "))
    print("Số nguyên sau khi đã đảo ngược ", end="")
    swap(num)
if __name__ == "__main__":
    main()