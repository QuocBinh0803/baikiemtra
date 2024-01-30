def is_anagram(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    if len(word1) != len(word2):
        return False
    ds1 = sorted([x for x in word1])
    ds2 = sorted([x for x in word2])

    for i in range(len(ds1)):
        if ds1[i] != ds2[i]:
            return False
        else:
            return True
def main():
    word1=input("Nhập từ thứ 1: ")
    word2=input("Nhập từ thứ 2: ")
    print(is_anagram(word1, word2))
if __name__ == "__main__":
    main()