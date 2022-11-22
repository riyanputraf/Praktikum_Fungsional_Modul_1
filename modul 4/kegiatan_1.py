import math


def perkalian(number1, number2):
    return number1 * number2


def pembagian(number1):
    def hasil(number2):
        return number1 / number2

    return hasil


def kuadrat(number):
    return number * number


def alpha(n):
    a = pembagian(360)(n)

    if 180 < a < 270:
        return 'Alpha berada di kuadran III, nilai khayal'
    elif a > 270:
        return 'Alpha berada di kuadran IV, nilai khayal'

    def inner_alpha():
        return math.sin(math.radians(a))

    return inner_alpha


def luas_poligon(n, r):
    a = alpha(n)

    # pengecekan apakah inputan berupa string
    if isinstance(a, str):
        return a
    elif n < 0 or r < 0:
        return 'Inputan Gak Boleh Negatif Sayang !'

    def hasil():
        r_kuadrat = kuadrat(r)
        n_kali_r_kuadrat = perkalian(n, r_kuadrat)
        dibagi_2 = pembagian(n_kali_r_kuadrat)(2)
        kali_alpha = perkalian(dibagi_2, a())

        return kali_alpha

    return hasil()


# Test case 1:
# Input:
# n = 9
# r = 21
# Output: luas = 1275.612

print(luas_poligon(9, 21))

# Test case 2:
# Input:
# n = 1.3
# r = 7
# Output: "Alpha berada di kuadran IV, Nilai khayal"

print(luas_poligon(1.3, 7))

# Test case 3:
# Input:
# n = 360
# r = 21
# Output: luas = 1385.372

print(luas_poligon(360, 21))

# Test case 4:
# Input:
# n = -5
# r = 21
# Output: "Inputan salah"

print(luas_poligon(-5, 21))
