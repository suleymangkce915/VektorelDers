import random

corba = ["Tarhana", "Yayla", "Ezo Gelin"]
anayemek = ["Karnı yarık", "Kuru fasulye", "Mantı"]
icecek = ["Ayran", "Kola", "Gazoz"]

print("Menü Öneri Programı")
print(f"Bugün size {random.choice(corba)} çarbası,")
print(f"Bugün size {random.choice(anayemek)} yemeği,")
print(f"Bugün size {random.choice(icecek)} öneriyorum.")