from .common import identifier, integer

def run(data):
    nodes=data['nodes']; edges=data['constraints']
    if not isinstance(nodes,list) or not 1<=len(nodes)<=100 or len(edges)>1000: raise ValueError('bounds')
    if len(set(nodes))!=len(nodes): raise ValueError('duplicate_node')
    for n in nodes: identifier(n)
    known=set(nodes)
    for e in edges:
        if e['from'] not in known or e['to'] not in known: raise ValueError('node')
        integer(e['max'], -10**12, 10**12)
    distances={n:0 for n in nodes}; parent={}; changed=None
    for _ in nodes:
        changed=None
        for i,e in enumerate(edges):
            value=distances[e['from']]+e['max']
            if distances[e['to']]>value:
                distances[e['to']]=value;parent[e['to']]=i;changed=e['to']
        if changed is None: break
    if changed is None:
        shift=distances[nodes[0]]
        return {'feasible':True,'schedule':{n:distances[n]-shift for n in nodes},'cycle':[]}
    v=changed
    for _ in nodes: v=edges[parent[v]]['from']
    start=v; witness=[]
    while True:
        i=parent[v];witness.append(i);v=edges[i]['from']
        if v==start: break
    witness.reverse();cycle=[dict(edges[i],constraint_index=i) for i in witness]
    assert all(cycle[i]['to']==cycle[(i+1)%len(cycle)]['from'] for i in range(len(cycle)))
    total=sum(e['max'] for e in cycle);assert total<0
    return {'feasible':False,'cycle':cycle,'cycle_bound_sum':total,'schedule':None}
