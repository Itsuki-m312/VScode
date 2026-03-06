#コレクションの中で、整数値のインデックスを指定して参照できるオブジェクトをシーケンスという
values1 = [1,2,3,4,5]

print(values1[0]+values1[3])

values2 = (10,20,30,40,50)

print(values2[1]+values2[4])

values3 = "ABCDE"

print(values3[3]+values3[4])

#シーケンスは比較演算子で比較できる

list1 = ["a","b","c",]
list2 = ["a","b","d",]
print(list1 < list2)