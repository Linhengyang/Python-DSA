#输入odd n，打印底边为n的空心等腰三角形（#字符组成）
def triangle(n):
    left = n//2
    print(" "*left + "#" + " "*left)
    for mid in range(1, n-1, 2):
        if mid < n-2:
            left = (n-2-mid)//2
            print(" "*left + "#" + " "*mid + "#" + " "*left)
        else:
            print("#"*n)
#输入一个纯字母英文单词，把ee换成E3，然后把剩下的e换成3
def change(word):
    word = word.lower()
    word = word.replace("ee", "12")
    word = word.replace("e", "4")
    word = word.replace('12', "E3")
    word = word.replace('4', "3")
    print(word)

if __name__ == "__main__":
    word = "neeEeear"
    change(word)