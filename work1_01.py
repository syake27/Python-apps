import random
while True:
    ran = random.randint(1,100)
    #print(ran)
    print("数字を入力してください")
    for i in range(1,6):
        while True:
            kai = input()
            if kai.isdigit(): #isdigit数字かどうか判断する
                kaitou = int(kai)
                break
            else:
                print("数字を入力してください")
        if ran == kaitou:
            print("正解！")
            break
        else:
            print("不正解")
            sa = ran - kaitou
            if kaitou < ran:
                if sa > 25:
                    print(f"{kaitou}よりとても大きいよ")
                else:
                    print(f"{kaitou}より大きいよ")
            else:
                if sa < -25:
                    print(f"{kaitou}よりかなり小さいよ")
                else:
                    print(f"{kaitou}より小さいよ")
    
    print(f"正解は{ran}でした!")

    while True:
        retry = input("もう１度しますか？yes no で答えてください")
        if retry == "yes":
            break
        elif retry == "no":
            exit() #exit終了
        else:
            print("yes no で答えてください")