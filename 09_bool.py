age = 15
height = 170
weight = 60
parents = 0
if (age >= 12) and (height >= 140) and (weight >= 40):
    print("お乗りいただけます")
else:
    print("ご遠慮ください") 
#andは二つ以上の条件が同時に真かどうか調べることができる


if (age >= 65) or (age <= 13):   #()をつけると可読性が上がる/優先順位が決められる
    print("割引料金")
else:
    print("通常料金")
#orは二つ以上の条件で、条件のうち１つ以上trueであればtrue,すべてfalseの時falseとなる
if not (age <= 12 ):
    print("ご入場いただけます")
elif not (parents == 0):
    print("ご入場いただけます")
else:
    print("ご入場いただけません")
#notは条件を反転させる。元の条件がtrueならfalse,falseならtrueとなる。上記の場合、１２以下でないということを表す