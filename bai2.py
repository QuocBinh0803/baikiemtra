def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

def main():
    s = input("Nhập chuỗi cần kiểm tra: ")
    s = s.replace(" ", "").lower()
    if is_palindrome(s):
        print("True")
    else:
        print("False")
        
if __name__ == "__main__":
    main()