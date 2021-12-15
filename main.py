import random
from _ml import MLAgent, train, save, load, train_and_plot, RandomAgent, validate, plot_validation
from _core import is_winner, opponent, start
 
trainplot = True
validation = False
training = False
onevone = False

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

if trainplot == True:
  my_agent = MyAgent(alpha=0.5, epsilon=1)
  random.seed(1)
  train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)

if validation == True:
  validation_agent = RandomAgent()
  validation_result = validate(agent_o=my_agent, agent_x=validation_agent, iterations=500)
  plot_validation(validation_result)
  
if training == True:
  my_agent = my_agent
  train(my_agent, 1000)
  save(my_agent, 'MyAgent_61005')

if onevone == True:
  start(player_x=my_agent)