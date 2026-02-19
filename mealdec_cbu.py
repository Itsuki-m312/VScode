import random

select = input("麺、ご飯、パンから選んでください")
if select == "麺":
    foods = ["そば", "焼きそば", "うどん", "パスタ",]
elif select == "ご飯":
    foods = ["ドリア","チャーハン","弁当",]
elif select == "パン":
    foods = ["お惣菜パン","ホットドッグ","ハンバーガー","サンドイッチ",]


choice = random.choice(foods)

print(f"今日のご飯は{choice}")