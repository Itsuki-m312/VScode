counter = 1

while counter <= 5:
    text = input("数字を入力してください")
    if text == "999":
        print("中断")
        break
    number = int(text)
    print(counter,"回目:",number ** 2)
    counter = counter + 1
#breakを使うとループを途中で中断して終了できる
print("終了")
