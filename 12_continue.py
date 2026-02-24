A = 0
while A < 10:
    A = A + 1
    if (A % 2) == 1:
        continue     #continueはループの先頭に戻ってやり直す

    print(A,"は偶数")


counter = 1
while counter <= 10:
    text = input("数字を入力してください")
    if text == "999":
        print("中断")
        break
    elif text == "":
        print("入力が無効です")
        continue
    number = int(text)
    print(counter,"回目",number**2)
    counter = counter + 1

print("終了")