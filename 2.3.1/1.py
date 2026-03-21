s = "GGCCCGGGGAAGTGGAGGGGGATCGCCCGGGTCTCTGTTGGCAGAGTCCGGG"
print("Secuencia 2: ")
print(s)
for nt in ("A", "C", "G", "T"):
    print(nt, round(s.count(nt)/len(s),4))