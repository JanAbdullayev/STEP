class Platinium:
  Price = 4000
  effect_on_speed = -100
  weight = 200
  color = "Reflecting Gray"
  temperature_defence = 200

class Gold:
  Price = 2000
  effect_on_speed = 0
  weight = 100
  color = "Golden"
  temperature_defence = 100

class Aliminium:
  Price = 800
  effect_on_speed = +100
  weight = 50
  color = "Light Gray"
  temperature_defence = 0


class EngineESS:
  Work = 400
  EnergyUse = 200
  Power = 47
  Horse_Power = 347
  Price = 8000

class EngineDSL:
  Work = 800
  EnergyUse = 400
  Power = 77
  Horse_Power = 689
  Price = 14000

class EngineMHEV:
  Work = 200
  EnergyUse = 100
  Power = 23
  Horse_Power = 244
  Price = 5500



class Mercedes(Platinium):
  Name = "Mercedes GG Class"
  Doors = 4
  Places = 5
  Work = EngineDSL.Work
  EnergyUse = EngineDSL.EnergyUse
  Power = EngineDSL.Power
  Horse_Power = EngineDSL.Horse_Power
  Price = Platinium.Price + EngineDSL.Price
class BMW(Gold):
  Name = "E38"
  Doors = 2
  Places = 2
  Work = EngineESS.Work
  EnergyUse = EngineESS.EnergyUse
  Power = EngineESS.Power
  Horse_Power = EngineESS.Horse_Power
  Price = Gold.Price + EngineESS.Price

class Camry():
  Name = "3.5"
  Doors = 4
  Places = 5
  Work = EngineMHEV.Work
  EnergyUse = EngineMHEV.EnergyUse
  Power = EngineMHEV.Power
  Horse_Power = EngineMHEV.Horse_Power
  Price = Aliminium.Price + EngineMHEV.Price


choose = int(input("Choose Car \n 1. Mercedes \n 2. BMW \n 3. Camry \n : "))

if choose == 1:
  print("Name",Mercedes.Name)
  print("Effect on speed",Mercedes.effect_on_speed)
  print("Weight",Mercedes.weight)
  print("Color",Mercedes.color)
  print("Temperature Defence",Mercedes.temperature_defence)
  print("Doors",Mercedes.Doors)
  print("Places",Mercedes.Places)
  print("Work",Mercedes.Work)
  print("Energy Use",Mercedes.EnergyUse)
  print("Power",Mercedes.Power)
  print("Norse Power",Mercedes.Horse_Power)
  print("Price",Mercedes.Price)
elif choose == 2:
  print("Name",BMW.Name)
  print("Effect on speed",BMW.effect_on_speed)
  print("Weight",BMW.weight)
  print("Color",BMW.color)
  print("Temperature Defence",BMW.temperature_defence)
  print("Doors",BMW.Doors)
  print("Places",BMW.Places)
  print("Work",BMW.Work)
  print("Energy Use",BMW.EnergyUse)
  print("Power",BMW.Power)
  print("Norse Power",BMW.Horse_Power)
  print("Price",BMW.Price)
elif choose == 3:
  print("Name",Camry.Name)
  print("Effect on speed",Camry.effect_on_speed)
  print("Weight",Camry.weight)
  print("Color",Camry.color)
  print("Temperature Defence",Camry.temperature_defence)
  print("Doors",Camry.Doors)
  print("Places",Camry.Places)
  print("Work",Camry.Work)
  print("Energy Use",Camry.EnergyUse)
  print("Power",Camry.Power)
  print("Norse Power",Camry.Horse_Power)
  print("Price",Camry.Price)
  
else:
  print("Chosee from givenn!")
