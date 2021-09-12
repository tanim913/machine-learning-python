import queue as q
import gbfsModule as gbfs_q
neighbour = [('s', 'a', 7), ('s', 'b', 2), ('s', 'c', 3), ('a', 'b', 3), ('a', 'd', 4), ('b', 'd', 4),
             ('b', 'h', 1), ('d', 'f', 5),
             ('h', 'f', 3), ('h', 'g', 2), ('g', 'e', 2), ('k', 'e', 5), ('i', 'k', 4), ('j', 'k', 4),
             ('l', 'i', 4), ('l', 'j', 4),
             ('c', 'l', 2)]

heu_fn = [('s', 10), ('a', 9), ('b', 7), ('c', 8), ('d', 8), ('h', 6), ('l', 6), ('f', 6), ('g', 3), ('i',4), ('j',4), ('k',3), ('e',0)]


pq = q.PriorityQueue()
t_nodes = []
path = []


s = str(input('Enter start node:'))
g = str(input('Enter goal node:'))
t_nodes.append((s, 'root'))
visited = {}
next_node = False
for i in range(len(heu_fn)):
    visited[heu_fn[i][0]] = False


for i in range(len(heu_fn)):
    if heu_fn[i][0] ==s:
        pq.put(gbfs_q.NodePriority(s,heu_fn[i][1]))

while not (pq.empty()):
    v = pq.get()
    print(v)
    node = v.node_name
    visited[node] = True
    if (node == g):
        path.append(node)
        break
    else:
        for i in range(len(neighbour)):
            if (neighbour[i][0] == node):
                next_v = neighbour[i][1]
                if (visited[next_v] == False):
                    next_node = True
                    t_nodes.append((node, next_v))
                    for j in range(len(heu_fn)):
                        if heu_fn[j][0] ==next_v:
                            pq.put(gbfs_q. NodePriority(next_v,heu_fn[j][1]))
                else:
                    next_node = False
        if(next_node == True):
            path.append(node)

print('The path is:',end=' ')
for x in path:
    print(x,end=' ')