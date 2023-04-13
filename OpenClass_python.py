
# INGET GOALS BELAJAR PYTHON
# Buat understanding logical thinking buat dipake scripting di Blender maupun Unreal Engine. Jadi next abis paham basic2nya, lgsg cari tutorial Python for Blender atau Python for Unreal
# Course link: https://www.youtube.com/watch?v=LWIzgB8NOyk&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=60&ab_channel=KelasTerbuka

# 1
# Apa itu Python ____________________________________


# 58
# Standard Library ____________________________________
'''
import datetime

data_waktu = datetime.datetime.now()
print(data_waktu)
print(f"Datetime now: {data_waktu}")
print(f"Tahun: {data_waktu.year}")
print(f"Hari : {data_waktu.strftime('%A')}")

# QNA | kenapa kok ada f di sebelumnya printf string?

data = ["a", "b", "c", "d", "e", "a", "g", "a", "e", "d"]

count = 0
for i in data:
    if i == "a":
        count += 1

print("Jumlah a: " + str(count) + "\n")

# coba pake module data count buat do something similar. Ngapain kita bikin dari scratch kalo emg udah disediain di Python wkwkwk

from collections import Counter

data_count = Counter(data)

print(f"data count = {data_count}\n")
print(f"jumlah a = {data_count['a']}\n")
print(f"jumlah d = {data_count['d']}\n")
'''