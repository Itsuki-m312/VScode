#コレクションとは、リストやタプル、辞書、文字列などのように、他のオブジェクトを集約するオブジェクトのこと。

#コレクションのオブジェクトは、共通して使うことができる処理がある。

dict_obj = {"犬":"dog","猫":"cat","鳥":"bird"}
print("辞書の要素数:",len(dict_obj))

tuple_obj = ("あ","い","う")
print("タプルの要素数:",len(tuple_obj))

list_obj = [1,2,3,4,]
print("リストの要素数は:",len(list_obj))

str_obj = "abcdefg"
#同様に比較演算子,in,for等も共通して使うことができる

print("あ" in tuple_obj)
print(1 in list_obj)

print("犬" in dict_obj) #辞書オブジェクトでは、in演算子はキーが登録されているかどうかを調べる
print("a" in str_obj) #文字列オブジェクトではその中に文字が含まれているかどうか調べる
print("efg" in str_obj) #文字列が含まれているかどうかも調べることができる

for letter in str_obj: #文字列をfor文に指定すると、一つずつ文字を取り出す
    upper_letter = letter.upper()
    print(upper_letter)

for jpn in dict_obj: #辞書をfor文に指定すると、キーを一つずつ取り出す
    eng = dict_obj[jpn]
    print(eng)