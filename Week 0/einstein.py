def einstein(mass):
    c = 300000000
    energy = mass * c * c
    return energy

m = int(input("m: "))

print(f"E: {einstein(m)}")
