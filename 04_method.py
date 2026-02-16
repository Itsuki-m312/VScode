text = "lower letters"
uppered_text = text.upper() #upper()メソッドで大文字にできる。データ.メソッド名(引数)
print( uppered_text )
text2 = "The shells she sells are sea-shells,I'm sure."
print(text2.find("sea")) #findメソッドは引数を指定して、その位置を戻り値として返す

data = 0.5
print(data.as_integer_ratio())#値を整数の比で表す。データごとに専用のメソッドが多くある

text3 = input()
lower_text = text3.lower()
print(lower_text)