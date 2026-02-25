# mikan = input("みかんの個数")
# momo = input("桃の個数")
# mikan_number = int(mikan)
# momo_number = int(momo)
# total_mikan = mikan_number * 40
# total_momo = momo_number * 100
# total = total_mikan + total_momo
# print("みかん",total_mikan,"円","もも",total_momo,"円","合計",total,"円")

def fruit_price(number_of_momo,number_of_mikan):#defで関数を作ることができる（関数を定義する):が必要
    total_momo = number_of_momo * 100 #インテンドが必要
    total_mikan = number_of_mikan * 40
    total = total_momo + total_mikan

    return total #returnで関数の戻り値（結果として返す値のこと）を指定

total = fruit_price(5,3)
print("合計",total,"円")
#total_momo等をローカル変数と言う。ローカル変数は、関数外から参照できない
#ローカル変数以外の変数をグローバル変数といい、グローバル変数はどんな場合でも参照できる
#関数以外の部分はモジュールスコープ、関数の部分は、ローカルスコープという。
#同じモジュールスコープ内で定義された関数、変数、モジュールは関数の内側でも呼び出せる例↓
ima = "現在時刻"
import time
def print_time():
    now = time.asctime()
    print(ima,now,)

print_time()

