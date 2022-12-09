class persona:
  def __init__(self, vards, uzvards, kvalifikacija=1):
    self.vards=vards
    self.uzvards=uzvards
    self.kvalifikacija=kvalifikacija
  def myfunc(self):
    print(self.vards, self.uzvards)
  
p1=persona("Edijs", "Čākurs")
print("Vārds: ",p1.vards)
print("Uzvārds: ",p1.uzvards)

uzvards=p1.uzvards[:-1]
print("Uzredzēšanos",uzvards,"kungs!")
del p1
del uzvards

p1=persona("Sūkļu", "Bobs")
p2=persona("Mr", "Krabītis")
p3=persona("Patriks", "Zvaigzne")

print("1)",p1.vards,p1.uzvards)
print("2)",p2.vards,p2.uzvards)
print("3)",p3.vards,p3.uzvards)
izvele = int(input("Ievadiet ciparu lai atlasitu no augšējiem minētiem: "))
if izvele == 1:
  print(p1.vards,p1.uzvards,"ir atlaists")
  del p1
elif izvele == 2:
  print(p2.vards,p2.uzvards,"ir atlaists")
  del p2
elif izvele == 3:
  print(p3.vards,p3.uzvards,"ir atlaists")
  del p3
input()
