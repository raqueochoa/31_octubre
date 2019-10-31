#inputs
contador = 1
español = 1
quimica= 1
force = 1

#proceso
while contador <= 10:
      materia = input("Dame la materia que estudias: ")
      edad = input("dame tu edad: ")
      contador += 1
      if materia == español:
          español = español + 1
          print( f"La cantidad de alumnos que estudian español son: {español}")
      elif materia == quimica:
           quimica = quimica + 1
           print ( f"La cantidad de alumnos que estudian quimica son: {quimica}")
      elif materia == force:
           force = force + 1
           print ( f"La cantidad de alumnos que estudian force son: {force}")
