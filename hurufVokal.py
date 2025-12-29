import time
import matplotlib.pyplot as plt
plt.ion()

# cek huruf vokal
def is_vowel(c):
    return c.lower() in "aiueo"

# rekursif
def count_vowels_recursive(s, i=0):
    if i >= len(s):
        return 0
    return (1 if is_vowel(s[i]) else 0) + count_vowels_recursive(s, i + 1)

#iteratif
def count_vowels_iterative(s):
    count = 0
    for ch in s:
        if is_vowel(ch):
            count += 1
    return count

# menampilkan tabel
def print_table(n_values, rec_times, it_times):
    print("\n+----+------------------------+------------------------+")
    print("| n  |   Recursive Time (s)   |   Iterative Time (s)   |")
    print("+----+------------------------+------------------------+")
    for n, r, i in zip(n_values, rec_times, it_times):
        print(f"| {n:2d} | {r:<22.12e} | {i:<22.12e} |")
    print("+----+------------------------+------------------------+")

# grafik
def update_graph(n_values, rec_times, it_times):
    plt.clf()
    plt.plot(n_values, rec_times, label="Recursive", marker="o")
    plt.plot(n_values, it_times, label="Iterative", marker="o")
    plt.title("Performance Comparison: Recursive vs Iterative")
    plt.xlabel("Input (n) = panjang kalimat")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.pause(0.1)

print("=== Hitung Huruf Vokal: Rekursif vs Iteratif ===")

# simpan data hasil
n_values = []
rec_times = []
it_times = []

kalimat = input("Masukkan kalimat: ")

while True:
    if kalimat.strip() == "":
        print("Masukkan nilai n yang valid!")
        kalimat = input("Masukkan kalimat: ")
        continue

    n = len(kalimat)
    n_values.append(n)

    start = time.time()
    r = count_vowels_recursive(kalimat)
    rec_times.append(time.time() - start)

    start = time.time()
    i = count_vowels_iterative(kalimat)
    it_times.append(time.time() - start)

    print("Jumlah vokal (rekursif):", r)
    print("Jumlah vokal (iteratif):", i)

    print_table(n_values, rec_times, it_times)
    update_graph(n_values, rec_times, it_times)

    lanjut = input("\nMasukkan kalimat selanjutnya? (y/n): ").strip().lower()
    if lanjut != "y":
        print("Program selesai. Terima kasih!")
        break

    kalimat = input("Masukkan kalimat: ")

plt.ioff()
plt.show()
