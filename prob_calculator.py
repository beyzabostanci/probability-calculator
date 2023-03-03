import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):#a variable number of arguments that specify the number of balls of each color that are in the hat. A hat will always be created with at least one ball.
    self.contents = []#The arguments passed into the hat object upon creation should be converted to a contents. 
#contents should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color
    for ball in balls:
      self.contents += [ball] * balls[ball] #self.content = self.content + [ball] * balls[ball]
    
  def draw(self, number_of_balls):#draw method that accepts an argument indicating the number of balls to draw from the hat
    # If the number of balls to draw exceeds the available quantity, return all the balls.
    if number_of_balls > len(self.contents):
      all_balls = copy.copy(self.contents)
      self.contents = []
    else:#remove balls at random from contents and return those balls as a list of strings
      all_balls = random.sample(self.contents, number_of_balls)#sample method returns a list with selection
      for ball in all_balls:
        self.contents.remove(ball)
    return all_balls
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  #expected -olasılık
  #experiments -deney sayısı
  #drawn-cekilecek top sayısı
  #hat- yerleştirilcek yer
  correct_guess = 0

  for i in range(num_experiments):
    cop_hat = copy.deepcopy(hat)
    balls_drawn = cop_hat.draw(num_balls_drawn)
    check = True
    for key in expected_balls:
      check = check and (expected_balls[key] <= balls_drawn.count(key))

    correct_guess += 1 if check else 0
  return correct_guess/num_experiments
