import random

all_foods =["お惣菜パン","ホットドッグ","ハンバーガー","サンドイッチ","ドリア","チャーハン","弁当","そば", "焼きそば", "うどん", "パスタ","ラーメン",]


print("決定と入力するまで選んだ範囲からランダムで出力されます")
select = input("麺、ご飯、パン、ランダムから選んでください")
if select == "麺":
    foods = ["そば", "焼きそば", "うどん", "パスタ","ラーメン",]
elif select == "ご飯":
    foods = ["ドリア","チャーハン","弁当",]
elif select == "パン":
    foods = ["お惣菜パン","ホットドッグ","ハンバーガー","サンドイッチ",]
elif select == "ランダム":
    foods = all_foods
else:
    print("選択肢以外の文字が入力されたため、ランダムで出力します")
    foods = all_foods

decide = ""

while decide != "決定":
    choice = random.choice(foods)
    print(choice)
    decide = input("入力:")
    
print(f"今日のご飯は{choice}")