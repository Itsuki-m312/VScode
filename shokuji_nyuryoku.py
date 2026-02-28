import random

list1 = input("リストを入力してください（５つまで）１つ目:")

while list1 == "":
    list1 = input("1つ目のリストを入力してください:")

list2 = input("２つ目:")

while list2 == "":
    list2 = input("２つ目のリストを入力してください:")

list3 = input("3つ目:")    

if list3 == "":
     foods = [list1,list2,]
     choice = random.choice(foods)
     print(f"今日のご飯は{choice}")
else:
    list4 = input("４つ目:")
    if list4 == "":
         foods = [list1,list2,list3,]
         choice = random.choice(foods)
         print(f"今日のご飯は{choice}")
    else:
         list5 = input("５つ目:")
         if list5 == "":
              foods = [list1,list2,list3,list4,]
              choice = random.choice(foods)
              print(f"今日のご飯は{choice}") 
         else:
            foods = [list1,list2,list3,list4,list5,]
            choice = random.choice(foods)
            print(f"今日のご飯は{choice}")