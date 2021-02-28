
from Graph import *
from a_star_alg import f
from Agent import Agent
from Helpful_Function import mst_hurisrtic

def Running_Enviorment(agent1=0 ,agent2=0 ,agent3=0):
    while(agent1.Terminate == False or agent2.Terminate == False or agent3.Terminate == False):
        agent1.Do_Turn()
        agent2.Do_Turn()
        agent3.Do_Turn()



def Simulator(agent1,graph,toPrint):
    while len(agent1.Road) > 0 or agent1.Terminate == False:
          state = agent1.Do_Turn()
          if state == "failure":
              print(state)
              return state
          # if len(agent1.Road) > 0 or agent1.Terminate == False:
          #     break
          print("The State is: ", state)
          graph.nodes[state]["P"]=0
          if toPrint:
              draw_g(graph)


graph = make_graph("graphfailer.txt")
i=1
agent1 = Agent("Gready_Agent",graph,mst_hurisrtic,f,i, 10)
agent2 = Agent("A_Star",graph,mst_hurisrtic,f,i, 10)
agent3 = Agent("Real_Time_A_Star",graph,mst_hurisrtic,f,i, 20)
# print("Gready_Agent")
# Simulator(agent1,graph.copy(),1)
print("\n\nA_Star")
Simulator(agent2,graph.copy(),0)
# print("\n\nReal_Time_A_Star")

# Simulator(agent3,graph.copy(),1)

# #
draw_g(graph)