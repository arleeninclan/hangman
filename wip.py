from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.image import Image 
from kivy.uix.boxlayout impot BoxLayout 
from kivy.properties import StringProperty
import random

def is_subset(subset, superset):
  """ Returns True if every item in subset is also in superset """
  return all([i in superset for i in subset])
  
def search(iterable, obj):
  """ Returns list of indices where obj can be found in iterable """
  return [index for index, item in enumerate(iterable) if item == obj]


  
class HangmanApp(App):
  
  WORDS = ['psychology', 'network', 'biology', 'tulips', 'highschool', 'transcript', 'university', 'pneumonia', 'oxygen', 'syndrome', 'wristwatch', 'policeman', 'zodiac', 'microwave', 'transplant','subway', 'transportation', 'celebration', 'fishhook', 'blizzard', 'hurricane', 'tsunami', 'earthquake', 'bookworm', 'temperature', 'potion', 'weather', 'computer', 'classic', 'music', 'literature', 'trigonometry', 'calculus', 'chemistry', 'physics', 'javascript', 'jazz', 'crocodile', 'venus', 'xray', 'itching', 'sleeveless', 'foxes', 'overjoy', 'puzzling', 'python', 'engineering', 'country', 'anatomy', 'synonym','optics', 'lipstick', 'recreation', 'applecider', 'vegetable', 'homework', 'exam', 'violence', 'protest', 'government', 'pangaea', 'earth', 'staircase', 'classroom', 'message', 'security', 'fishtank', 'pineapple', 'jacket', 'shower', 'clarinet', 'flute', 'xray', 'award', 'hangman', 'synapsis', 'mitosis', 'earings', 'boots', 'parrot', 'godfather', 'wedding', 'celebration', 'birthday', 'garden', 'computer', 'consequence', 'education', 'manufacture', 'company', 'beverage']
  
  chosen_word = list(random.choice(WORDS))
  
  tries_left = 8
  letters_left = []
  val = StringProperty('1')
  
  def build(self):
      return HangMan()
      
  def __init__(self):
    self.state = ['_' for i in self.chosen_word]
    self.game_over = False
  
  def __repr__(self):
    return "Hangman({})".format(self.state)
  
  def __str__(self):
    return 
  
  def checking(self, obj):
    try:
      float(obj)
    except ValueError:
      return False
    return True
    
  
  def move(self):
    if self.tries_left == 8:
      self.val = str(1)
    else:
      self.val = str(9 - self.tries_left)

    print(self.state)
    check_letter = input("Guess a letter: ")
    check_letter = check_letter.lower()
    if self.checking(check_letter) == False:
      index = search(self.chosen_word, check_letter)
      for n in index:
        self.state[n] = self.chosen_word[n]
      if index == []:
        self.tries_left -= 1
      self.letters_left.append(check_letter)
    
    

  def has_won(self): 
    if is_subset(self.chosen_word, self.state):
      return True
    
    
  def play(self):
    while not self.game_over:
      self.move()
      if self.has_won():
        print('\nYou won!')
        self.game_over = True
        together = ''.join(self.chosen_word)
        print('The word was: {}'.format(together))
        break
      if self.tries_left == 0:
        self.game_over = True
        together = ''.join(self.chosen_word)
        print('\nYou lose! ):')
        print('The word was: {}'.format(together))
        break
      used = '\nLetters Guessed: {}'.format(self.letters_left)
      print(used)

    
if __name__ == '__main__':
    HangmanApp().run()  

#-------------END-------------#
game = Hangman()
game.play()
