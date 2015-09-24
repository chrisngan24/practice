from collections import deque

def breadth_first_search(g, a, b):
    v = None
    g_size = len(g.keys())
    qu = deque([a]) 
    
    while (len(qu) > 0):
        v = qu.pop()
        if g.has_key(v):
            for i in g[v]:
                qu.append(i)
        if v == b:
            return True
        
    return False

def rec_search(g, v, b):
    if v == b:
        return True
    for i in g[v]:
        if rec_search(g, i , b):
            print i
            return True
    return False 
        


def depth_first_search(g, a, b):
    return rec_search(g, a, b)



if __name__ == '__main__':
    g = {}
    g[1] = [2,4]
    g[2] = []
    g[3] = []
    g[4] = [3]

    print breadth_first_search(g, 1, 3)
    print breadth_first_search(g, 2, 3)
    print depth_first_search(g, 1, 3)
    print depth_first_search(g, 2, 3)
