def generator_prima(n):
    prima = set()
    print("ini prima " + str(prima))
    for n in range(2, n):
        if all(n % p > 0 for p in prima):
            prima.add(n)
            yield n


print(*generator_prima(100))
