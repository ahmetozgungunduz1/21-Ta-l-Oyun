import random

print("21 TAŞLI STRATEJİ OYUNU")
print("Ortada 21 taş var. Sırayla 1,2,3 taş çekersin.")
print("Son taşı çeken kaybeder.")

kalan_tas = 21

while kalan_tas > 0:
    print(f"Kalan Taş Sayısı: {kalan_tas} Taş")

    while True:
        secim = input("Kaç taş almak istiyorsun (1/2/3):").strip()

        if not secim.isdigit() or not (1 <= int(secim) <=3):
            print("Yanlış girdiniz, lütfen 1,2,3 ten birini seçiniz")
            continue

        oyuncu_tas = int(secim)

        if oyuncu_tas > kalan_tas:
            print(f"{kalan_tas}'tan fazla alamazsın")
            continue
        break

    kalan_tas -= oyuncu_tas
    print(f"Sen {oyuncu_tas} taş aldın.")

    if kalan_tas == 0:
        print("\n Son taşı sen aldın! Maalesef oyunu kaybettin")
        break

    maksimum_alinabilir = min(3, kalan_tas)
    bilgisayar_tas = random.randint(1, maksimum_alinabilir)


    kalan_tas -= bilgisayar_tas
    print(f"Bilgisayar {bilgisayar_tas} taş aldı.")

    if kalan_tas == 0:
        print("\n Bilgisayar son taşı almak zorunda kaldı! Sen kazandın!")
        break
      
