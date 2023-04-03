import math

def get_entropy(p):
    ent = 0
    for i in range(len(p)):
        temp = p[i] * math.log2(1/p[i])
        print(i, "번째: " , temp)
        ent += temp
    return ent

def get_child_entropy(p, e):
    ent = 0
    for i in range(len(p)):
        temp = p[i] * e[i]
        print(i, "번째(child): " , temp)
        ent += temp
    return ent

### parent entropy
parent_p = [1/5, 4/5]

e_parent = get_entropy(parent_p)
print("e_parent: ", e_parent)

### child total entropy
percent = [5/6, 1/6]
entropy = [0.7219, 0]

e_child = get_child_entropy(percent, entropy)
print("e_child: ", e_child)

### information gain
# information_gain = e_parent - e_child
temp_p = 0.9282
temp_c = 0.6015
information_gain = temp_p - temp_c
print(information_gain)


def child_ent():
    child_cnt = 2
    child1_p = []
    ichild = 0
    for i in range(child_cnt):
        ichild += get_entropy(child1_p)

    ig = iparent - ichild