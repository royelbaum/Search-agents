
from Helpful_Function import *
from Graph import make_graph 
from Gready_Agent import Dijkstra

def Gready_Heuristic_Agent(problem,h):
    OPEN = [problem.Initial_State]
    CLOSE = []
    count=0
    while(True):
        if len(OPEN) == 0:
            return "failure"
        elif count>=2000:
            return "infinite loop"
        else:
            state = OPEN.pop(0)
            collect_P(state)
            if problem.Goal_Test(state, h):
                print("number of expantions:", count)
                return state
            if not in_close(CLOSE,state):
                CLOSE.insert(0, state)
                expandarray = Expand_gridy(state,problem.Graph)
                count += 1
                for s in expandarray:
                    fail = update_h_val(s, problem.Graph, h)
                    if fail == "failure":
                        return "failure"
                OPEN = OPEN + expandarray
            OPEN=Sort_By_H_tag(OPEN)



def Sort_By_H(open,h,graph):
    newstate = open.pop(0)
    minimun = h(newstate,graph)
    for i in open:
        heuristic = h(i,graph)
        if heuristic < minimun:
            minimun = heuristic
            open.insert(0,newstate)
            newstate = i
            open.remove(i)
    open.insert(0, newstate)

