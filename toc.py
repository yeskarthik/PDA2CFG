nodes = []
visited = set()

class Node:
    def __init__(self, state):
        self.state = state
        self.adjs = set()
        self.adjNames = set()

    def addAdj(self, read, pop, push, node):
        self.adjs.add((read, pop, push, node))
        self.adjNames.add(str(node.state))

    def checkIfAdjExists(self, c):        
        return c in self.adjNames
    def dfs(self, c):
        global visited
        visited = set()
        
        return self.dfs_helper(c)

    def dfs_helper(self, c):
        global visited
        if str(c) in self.adjNames:
            return True
        else:
            for e in self.adjNames:                              
                if e not in visited and str(c) in nodes[int(e)].adjNames:
                    return True
                elif e not in visited:
                    visited.add(e)
                    flag = nodes[int(e)].dfs_helper(c)
                    if flag == True:
                        return flag
                
            return False



def generateStates(n):
    t = 0
    while (t < n):
        nodes.append(Node(str(t)))
        print t
        t += 1

generateStates(12)

nodes[0].addAdj('E', 'E', '1', nodes[1])
nodes[1].addAdj('0', 'E', 'a', nodes[2])
nodes[2].addAdj('E', 'a', 'E', nodes[3])
nodes[3].addAdj('0', 'Y', 'E', nodes[3])
nodes[3].addAdj('0', 'E', 'X', nodes[4])
nodes[3].addAdj('0', '$', 'E', nodes[7])
nodes[3].addAdj('E', '$', 'E', nodes[11])
nodes[4].addAdj('E', '$', 'E', nodes[5])
nodes[5].addAdj('E', '$', 'E', nodes[3])
nodes[6].addAdj('0', '$', 'E', nodes[6])
nodes[6].addAdj('E', '$', 'E', nodes[8])
nodes[6].addAdj('E', '$', 'E', nodes[9])
nodes[7].addAdj('E', '$', 'E', nodes[6])
nodes[8].addAdj('0', '$', 'E', nodes[3])
nodes[9].addAdj('E', '$', 'E', nodes[10])
nodes[10].addAdj('E', '$', 'E', nodes[6])


#print nodes[0].checkIfAdjExists('2')

# print nodes[1].dfs(str(3))
# print nodes[3].dfs(str(3))
# print nodes[0].dfs(str(0))
# print nodes[1].dfs(str(3))
# print nodes[3].dfs(str(3))

### Generate non terminals

class Variable:
    def __init__(self, name):
        self.name = name
        self.rules = set()

    def addRule(self, rule):
        self.rules.add(rule)

variables = []

def convert(i):
    if i == '10':
        return 'a'
    elif i == '11':
        return 'b'
    elif i == '12':
        return 'c'
    elif i == '13':
        return 'd'
    elif i == '14':
        return 'e'
    elif i == '15':
        return 'f'
    else:
        return i

def convert_back(t):
    if t == 'a':
        return 10
    elif t == 'b':
        return 11
    elif t == 'c':
        return 12
    elif t == 'd':
        return 13
    elif t == 'e':
        return 14
    elif t == 'f':
        return 15
    else:
        return int(t)


def generateVariables():
    for i in range(len(nodes)):
        for j in range(len(nodes)):

            variables.append(Variable(convert(str(i))+convert(str(j))))
            print convert(str(i))+convert(str(j))

def generateRules():
    for i in range(len(variables)):
        if variables[i].name[0] == variables[i].name[1]:
            variables[i].addRule('E')        
            print str(variables[i].name) + ' -> E'
        #if nodes[int(variables[i].name[0])].checkIfAdjExists(str(variables[i].name[1])):
        for j in range(len(variables)):
            for k in range(len(variables)):
                
                if variables[j].name[0] == variables[i].name[0] \
                        and variables[k].name[1] == variables[i].name[1] \
                        and variables[j].name[1] == variables[k].name[0]:

                    # #print variables[i].name + ' ' + variables[j].name + ' ' + variables[k].name
                    # print variables[j].name
                    # print variables[k].name
                    # print nodes[int(variables[j].name[0])].dfs(str(variables[j].name[1]))
                    # print nodes[int(variables[k].name[0])].dfs(str(variables[k].name[1]))
                    # # # print nodes[int(variables[j].name[0])].state
                    # # # print nodes[int(variables[j].name[1])].state
                    # # # print nodes[int(variables[k].name[0])].state
                    # # # print nodes[int(variables[k].name[1])].state
                    # # print nodes[int(variables[j].name[0])].dfs(str(variables[j].name[1]))
                    # # print nodes[int(variables[j].name[1])].dfs(str(variables[k].name[0]))
                    # # print nodes[int(variables[k].name[0])].dfs(str(variables[k].name[1])) 
                    # print nodes[1].dfs(str(3))
                    # print nodes[3].dfs(str(3))
                    if nodes[convert_back(variables[j].name[0])].dfs(str(variables[j].name[1])) and \
                        nodes[convert_back(variables[k].name[0])].dfs(str(variables[k].name[1])) :

                        print variables[i].name + ' --> ' + variables[j].name + ' ' + variables[k].name
                        variables[i].addRule(variables[j].name + ' ' + variables[k].name)

generateVariables()
generateRules()