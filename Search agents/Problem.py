class Problem(object):

    def __init__(self,graph,initialstate, goalstate = 0):
        self.Graph = graph
        self.Initial_State = State(initialstate,graph)

        self.Initial_State.g= 0
        self.Goal_State = goalstate


    def Goal_Test(self,node,h):
        #return h(node,self.Graph) == 0
        return len(node.Nodes_W_P)==0
    

    def Expand(self, node):
        nighbores = []
        for i in self.Graph.nodes[node]:
            self.Graph[i]["g(node)"] = node["g(node)"]+self.Graph.edge(node,i)["weight"]
            nighbores.append(i)
        return nighbores


## ------  new class  -------  
class State(object):

    def __init__(self, node ,graph,prev=None,g=0,h=0):
        self.Node = node
        self.Nodes_W_P=[]
        self.h=h
        if prev!= None:
            self.Nodes_W_P=prev.Nodes_W_P.copy()
        else:
            for i in graph.nodes:
                if graph.nodes[i]["P"]>0:
                    self.Nodes_W_P.insert(0,i)
        self.g=g
        self.Prev= prev