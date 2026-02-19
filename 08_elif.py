# print("123".isalpha())
# print("abc".isalpha())
#文字列がアルファベットかどうかを判定するメソッド

string = input("文字列を入力してください")

if string.isdecimal():
    print(string,"は数字です")
elif string.isalpha():
    print(string,"はアルファベットです")
else:
    print(string,"は数字でもアルファベットでもありません")
    