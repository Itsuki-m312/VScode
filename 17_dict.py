eng = {"apple":"りんご","peach":"もも","cow":"うし"}
#これを辞書オブジェクトと呼び、検索する時に指定するデータをキー,結果を値と呼ぶ{"キー1:値1","キー2"...}で表す
print(eng)

print(eng["cow"])#辞書オブジェクト[キー]で参照できる

eng["dog"] = "犬" #辞書オブジェクト[キー] = 値　で辞書オブジェクトに要素を追加することができる

print(eng["dog"])

eng["dog"] = "いぬ" #置き換え

print(eng["dog"])

del eng["dog"] #要素の削除

print(eng)

print(len(eng)) #要素数
