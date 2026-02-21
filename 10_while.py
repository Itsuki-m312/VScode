password = ""

while password != "1234":
    password = input("正しいパスワードを入力してください")

print("パスワード入力完了")#正しいパスワードが入力されるまで順次処理でwhileのループが繰り返されるので、whileを突破すると次に進める

#whileは while 条件式: で使い、条件式がtrueであればループを実行する