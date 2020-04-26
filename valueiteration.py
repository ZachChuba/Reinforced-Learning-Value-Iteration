def value_iteration(states, terminal_states,
                    nonterminal_states, rewards, transition1,
                    transition2, gamma):
    viprev = [0 for state in nonterminal_states]
    terms = []
    for state in terminal_states:
        terms.append(rewards[state])
    viprev = viprev + terms
    i = 1
    numits = 0
    while (True):
        if numits == 0:
            vi = [0 for state in nonterminal_states] + terms
        else:
            vi = viprev
        for i in range(len(nonterminal_states)):
            def findmax():
                curr_s = rewards[nonterminal_states[i]]
                sum1 = sum2 = cumprob = 0
                for j in range(len(nonterminal_states)):
                    state = nonterminal_states[j]
                    if state != curr_s:
                        sum1 += transition1[i][j] * viprev[j]
                for j in range(len(terminal_states)):
                    state = terminal_states[j]
                    if state != curr_s and cumprob < 1:
                        cumprob += transition2[i][j]
                        sum2 += transition2[i][j] * viprev[j+len(nonterminal_states)]
                        
                return max(sum1, sum2)
            vi[i] = rewards[nonterminal_states[i]] + gamma * findmax()
        if (subtract(viprev, vi) < 0.01 and numits > 1):
            break
        viprev = vi
        numits += 1
    return viprev

def subtract(viprev, vi):
    cumulative = 0
    for i in range(len(vi)):
        cumulative += vi[i] - viprev[i]
    return cumulative
