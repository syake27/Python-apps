print("カロリー収支計算")

def retry():
    while True:
        x = input(f"{aaa}を入力してください: ")
        if x.isdigit():
            return int(x)
        else:
            print("数字を入力してください。")

while True:
    seibetu = input("性別(m/f)")
    if seibetu == "m":
        break
    elif seibetu == "f":
        break
    else:
        print("m/fで入力してください")

aaa = "年齢"
tosi = retry()

aaa = "身長"
cm = retry()

aaa = "体重"
kg = retry()

aaa = "歩数"
hosuu = retry()

aaa = "本日の摂取カロリー"
sessyu = retry()


if seibetu == "m":
    kiso = float(13.397 * int(kg) + 4.799 * int(cm) - 5.677 * int(tosi) + 88.362)
elif seibetu == "f":
    kiso = float(9.247 * int(kg) + 3.098 * int(cm) - 4.33 * int(tosi) + 447.593)

hosuukcal = 0.03  * int(hosuu) 
print(hosuukcal)

goukei = int(sessyu) - (int(kiso) + int(hosuukcal))

print("計算結果")
print(f"基礎代謝{kiso}")
print(f"歩数による消費カロリー{hosuukcal}")
print(f"合計の消費カロリー{goukei}")

if goukei < 0:
    print(f"今日は{goukei}kcalです。この調子で頑張りましょう")
else:
    print(f"今日は{goukei}です。明日は運動しましょう。")