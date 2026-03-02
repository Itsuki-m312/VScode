values = [1,2,3,4,5,]

for value in values: # for 変数名 in リストオブジェクト:　でリストから１つずつ要素を順番に取り出し、それぞれに処理を一度ずつ実行する
    print("value",value,"value**2",value**2)
    #変数名はリストから取り出した要素を参照している

cases = [109,104,98,140,123,83,120,]

total = 0

for case in cases:
    total = total + case

print(total)