import time
import random
print("反応速度を測定します。")
print("【！！！！！】が出たら、できるだけ早くEnterキーを押してください。")
print("準備ができたらEnterキーを押してください。")
ran = random.randint(1,10)
wait = input()
time.sleep(5)
time.sleep(ran)
print("!!!!!!!!!!!!!")
start = time.perf_counter()

en = input()

end = time.perf_counter()

co = end - start
count = ('{:.4f}'.format(co))
if co > 0.01:
    print(f"反応速度: {count} 秒")
else:
    print("反応速度が0.01秒未満だったので終了しました。")