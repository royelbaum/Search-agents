
from Helpful_Function import *

def f(h,state,graph):
    return state.g + state.h




def A_Star(problem, h,f):
    OPEN = [problem.Initial_State]
    CLOSE = []
    count=0
    while(True):
        if len(OPEN) == 0 or count >=10000:
            return "failure"
        else:
            state = OPEN.pop(0)
            collect_P(state)
            if problem.Goal_Test(state, h):
                print("number of expantions:", count)
                return state
            if not in_close(CLOSE,state):
                CLOSE.insert(0, state)
                expandarray = Expand(state,problem.Graph)
                count += 1
                for s in expandarray:
                   fail =  update_h_val(s,problem.Graph,h)
                   if fail == "failure":
                       return "failure"
                OPEN = OPEN + expandarray
            OPEN=Sort_By_F(OPEN)


