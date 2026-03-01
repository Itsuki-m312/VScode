#基本的にプログラマーが名前をつけられるもの(数値、関数など）をオブジェクトと呼ぶ

cases = [10,12,14,8,6,15,19,]#7つの整数オブジェクトを要素とするリストオブジェクト

# print(cases)

empty_list = []
print(empty_list)

#リストを参照するときは左から順番に[0,1,2,...]となる
print(cases[3])

#指定している要素の順番をインデックスという

total = cases[0] + cases[1] + cases[2]
print(total)  #リストオブジェクト[インデックス]で参照した要素は、式の中で普通の値や変数と同じように使うことができる

print(cases)

cases.insert(7,13) #リストオブジェクト.insert(挿入位置,オブジェクト) でリストに要素を追加することができる
cases.insert(0,8)

print(cases)

cases[0] = 7 #リストオブジェクト[インデックス] = 値 でリスト内の要素を書き換えることができる

print(cases)

del cases[6] #del リストオブジェクト[インデックス] でリスト内の要素を削除することができる

print(cases)
