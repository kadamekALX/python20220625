i = 0
while i < 10:
    i += 1
    if i == 2:
        continue  # kończy obecny obrót pętli i wraca do sprawdzenia warunku
    print(i)
    if i == 7:
        break  # kończymy najbardziej wewnętrzną pętlę
