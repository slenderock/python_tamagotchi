class Pet:
  health = 50
  mutilation = 50
  love = 50
  alive = True

  if health<=0:
    print("You can stop now...She is dead")
    kill()

  def __init__(self, name):
    self.name = name

  def help(self):
    return "All commands:\n\
      \tintroduse\n\
      \tflog\n\
      \tcaress\n\
      \tkill"

  def display_vital_statistics(self):
    print("\nCurrent stats:")
    print("\tname:      \t" + str(self.name))
    print("\thealth:    \t" + str(self.health))
    print("\tlove:      \t" + str(self.love))
    print("\talive:     \t" + str(self.alive) + "\n\n")

  def introduse(self):
    return "My name is " + self.name

  def caress(self):
    self.love += 10
    self.mutilation -= 10
    return "You are so sweet)  "

  def flog(self):
    self.mutilation+= 10
    self.love -= 10
    self.health -= 5
    return "Oh yeah"

  def kill(self):
    self.alive = False
    return "Goodbye, my love"

raw_input("Hey, man, you want to dominate someone? [y/n]\n")
print("\n(Laughter) I think it does not matter.\n")
pet_name = raw_input("Please, give a name for your little toy and let's start =_= \n")

pet = Pet(pet_name)

while pet.alive:
  pet.display_vital_statistics()
  wishes = raw_input(pet.name +"> Whats your wishes?\n")
  print(pet.name +"> As you wish, my master.\n")
  try:
    exec("print(pet.name +'> ' + pet." + wishes + "())")
  except:
    print(pet.name + "> I don't know this command(write 'help' to get list of commands)")
