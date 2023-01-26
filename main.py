print ("== WHAT SOUND? ==")
print ()

exit = "no"

while exit == "no":
  animal_sound = input ("What animal do you want to hear?  ")

  if animal_sound == "dog" or animal_sound == "Dog":
    print ("Barrrrrrkk 🐶")
  elif animal_sound == "sheep" or animal_sound == "Sheep":
    print ("Bleehhhhhh 🐑")
  elif animal_sound == "cow" or animal_sound == "Cow":
    print ("Moooooooo 🐮")
  elif animal_sound == "owl" or animal_sound == "Owl":
    print ("Hooooooot 🦉")
  elif animal_sound == "pig" or animal_sound == "Pig":
    print ("oink, oink 🐷")
  else:
    print ("I don't know that sound")
  print ()
  
  exit = input ("Do you want exit the program?  ")
  print ()