english_words = {"apple":"りんご","book":"本","dog":"犬",}

word = input("英単語を入力してください")

if word in english_words:
    print(english_words[word])
else:
    print("登録されていません")