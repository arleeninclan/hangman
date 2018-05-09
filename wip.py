import random

def is_subset(subset, superset):
  """ Returns True if every item in subset is also in superset """
  return all([i in superset for i in subset])
  
def search(iterable, obj):
  """ Returns list of indices where obj can be found in iterable """
  return [index for index, item in enumerate(iterable) if item == obj]


  
class Hangman:
  
  WORDS = ['psychology', 'network', 'biology', 'tulips', 'highschool', 'transcript', 'pneumonia', 'oxygen', 'syndrome', 'wristwatch', 'policeman', 'zodiac', 'microwave', 'transplant','subway', 'transportation', 'celebration', 'fishhook', 'blizzard', 'hurricane', 'tsunami', 'earthquake', 'bookwarm', 'jazz', 'crocodile', 'venus', 'xray', 'itching', 'sleeveless', 'foxes', 'overjoy', 'puzzling', 'python', 'engineering']
  
  chosen_word = list(random.choice(WORDS))
  
  def __init__(self):
    self.state = ['_' for i in self.chosen_word]
    self.game_over = False
  
  def __repr__(self):
    return "Hangman({})".format(self.state)
  
  def __str__(self):
    return 
  
  def move(self):
    print(self.state)
    check_letter = input("Guess a letter... make sure it's lowercase: ")
    index = search(self.chosen_word, check_letter)
    for n in index:
      self.state[n] = self.chosen_word[n]
      
  def has_won(self): 
    if is_subset(self.chosen_word, self.state):
      return True
    
  def play(self):
    while not self.game_over:
      self.move()
      if self.has_won():
        print('You won!')
        self.game_over = True
        break
  

#-------------END-------------#
game = Hangman()
game.play()
