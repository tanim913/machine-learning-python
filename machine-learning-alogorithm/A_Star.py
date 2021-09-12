import queue as q
import sModule as pri_queue

neighbour = [('s', 'a', 7), ('s', 'b', 2), ('s', 'c', 3), ('a', 'b', 3), ('a', 'd', 4), ('b', 'd', 4),
             ('b', 'h', 1), ('d', 'f', 5),
             ('h', 'f', 3), ('h', 'g', 2), ('g', 'e', 2), ('k', 'e', 5), ('i', 'k', 4), ('j', 'k', 4),
             ('l', 'i', 4), ('l', 'j', 4),
             ('c', 'l', 2)]

heu_fn = [('s', 10), ('a', 9), ('b', 7), ('c', 8), ('d', 8), ('h', 6), ('l', 6), ('f', 6), ('g', 3), ('i',4), ('j',4), ('k',3), ('e',0)]

priority_queue = q.PriorityQueue()
t_nodes = []
path = []

# main
s = str(input('Enter start node:'))
g = str(input('Enter goal node:'))


visited = {}
tn_index = {}
parrent_node = {}
h_value = 0
next_node = False
for i in range(len(heu_fn)):
    visited[heu_fn[i][0]] = False
for i in range(len(heu_fn)):
    if heu_fn[i][0] ==s:
        h_value = heu_fn[i][1]
        priority_queue.put(pri_queue.NodePriority(s, 0, 'root', h_value))
t_nodes.append((s, 0, 'root', h_value))
index = 0
tn_index[s] = 0
parrent_node[0] = s
parrent_node['root'] = 'root'
n_h_value = 0

while not (priority_queue.empty()):
    v = priority_queue.get()
    node = v.name
    visited[node] = True
    if (node == g):
        path.append(node)
        break
    else:
        i = 0
        for i in range(len(neighbour)):
            if (neighbour[i][0] == node):
                next_v = neighbour[i][1]
                index = index + 1
                tn_index[next_v] = index
                parrent_node[index] = node
                cost = neighbour[i][2]
                if (visited[next_v] == False):
                    next_node = True
                    t_nodes.append((node, next_v))
                    for j in range(len(heu_fn)):
                        if heu_fn[j][0] ==next_v:
                            priority_queue.put(pri_queue. NodePriority(next_v,tn_index[next_v],tn_index[node],heu_fn[j][1]+cost))

                else:
                    next_node = False
        if(next_node == True):
            path.append(node)

print('The path is:')
for x in path:
    print(x,end=' ')