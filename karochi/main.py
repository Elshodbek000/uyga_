davlatlar = ["O'zbekiston", "AQSH", "Germaniya", "Buyuk Britaniya", "Turkiya"]
print(davlatlar)

print(len(davlatlar))

print(sorted(davlatlar))

print(sorted(davlatlar, reverse=True))

print(davlatlar)

davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

juft_sonlar = [i for i in range(120, 1201) if i % 2 == 0]
print(juft_sonlar)
sonlar = [5, 12, 8, 20, 7]
print(sum(sonlar))
sonlar = [3, 15, 7, 22, 9]

farq = max(sonlar) - min(sonlar)
print(farq)
print(len(sonlar))

katta_royxat = list(range(1, 101))
print(katta_royxat[:20])
print(katta_royxat[40:60])
print(katta_royxat[-20:])
taomlar = ["osh", "manti", "lag'mon", "shashlik", "somsa"]
print(taomlar)
nonushta = taomlar.copy()
print(nonushta)
nonushta = ["qatiq", "tuxum", "non", "choy", "asal"]
nonushta.extend(["olma", "banan"])
print(nonushta)
print("Taomlar:", taomlar)
print("Nonushta:", nonushta)