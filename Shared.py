import copy

def expand(node):
    i = node['values'].index(0)
    nodes = []

    if i%3 != 0:
        tmp = copy.deepcopy(node)
        tmp['depth'] = node['depth'] + 1
        tmp['values'][i], tmp['values'][i-1] = tmp['values'][i-1], tmp['values'][i]
        tmp['parent'] = node
        nodes.append(tmp)
    if i%3 != 2:
        tmp = copy.deepcopy(node)
        tmp['depth'] = node['depth'] + 1
        tmp['values'][i], tmp['values'][i+1] = tmp['values'][i+1], tmp['values'][i]
        tmp['parent'] = node
        nodes.append(tmp)
    if i > 2:
        tmp = copy.deepcopy(node)
        tmp['depth'] = node['depth'] + 1
        tmp['values'][i], tmp['values'][i-3] = tmp['values'][i-3], tmp['values'][i]
        tmp['parent'] = node
        nodes.append(tmp)
    if i < 6:
        tmp = copy.deepcopy(node)
        tmp['depth'] = node['depth'] + 1
        tmp['values'][i], tmp['values'][i+3] = tmp['values'][i+3], tmp['values'][i]
        tmp['parent'] = node
        nodes.append(tmp)

    return nodes