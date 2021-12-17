import random
from _ml import MLAgent, train, save, load, train_and_plot, RandomAgent, validate, plot_validation
from _core import is_winner, opponent, start
 
trainplot = False
validation = False
training = False
onevone = True

class MyAgent(MLAgent):
  def evaluate(self,board):
    if is_winner(board, self.symbol):
      reward = 1
    elif is_winner(board, opponent[self.symbol]):
      reward = -10
    else:
      reward = 0
    return reward


  
#Agents     
my_agent = load('MyAgent_61005')
my_agent.learning = False
random_agent = RandomAgent()
validation_agent=random_agent


play = True
while play == True:
  if play == True:
    print("\n 1) Speel een 1v1 tegen iemand anders \n 2) Speel een 1v1 tegen een AI \n 3) Teken een win/loss diagram van de AI \n 4) Train een nieuwe AI")
    choice = input()
    play = False


  #FREEPLAY
  if choice == '1':
    start()
  #1V1 AI
  if choice == '2':
    print("Wil je X of O zijn? (X/O)")
    xofo = input()
    if xofo == 'X' or xofo == 'x':
      start(player_o=my_agent)
    if xofo == 'O' or xofo =='o':
      start (player_x=my_agent)
  #WIN/LOSS DIAGRAM
  if choice == '3':
    print("AI X of AI O? (X/O)")
    xofo2 = input()
    if xofo2 == 'X' or xofo2 == 'x':
      validation_agent = RandomAgent()
      validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=500)
      plot_validation(validation_result)
    if xofo2 == 'O' or xofo2 == 'o':
      validation_agent = RandomAgent()
      validation_result = validate(agent_o=my_agent, agent_x=validation_agent, iterations=500)
      plot_validation(validation_result)
  #TRAIN NIEUWE AI
  if choice == '4':
    my_agent = MyAgent(alpha=0.5, epsilon=1)
    random.seed(1)
    train_and_plot(
      agent=my_agent,
      validation_agent=random_agent,
      iterations=50,
      trainings=100,
      validations=1000)

  print("Opnieuw? (JA/NEE)")
  opnieuw = input()
  if opnieuw == 'JA' or  opnieuw== 'ja' or opnieuw=='Ja':
    play = True
  if opnieuw == 'NEE' or opnieuw == 'nee' or opnieuw == 'Nee':
    play = False
