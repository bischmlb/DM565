### 1.1 Finite automata
 - models for computers with an extremely limited amount of memory
 - Example could be swing doors (tænk på dsb togdøre)
 - CONTROLLER: State - Input
 - **Markov Chains**
 - **Formal Definition:** set of states, input alphabet, rules for moving, start state, and accept states
 - ```δ(x,1)=y``` (This rules says that, if we are in state x, and we receive a 1, we move to state y.)
```
A ﬁnite automaton is a 5-tuple (Q,Σ,δ,q0,F), where
1. Q is a ﬁnite set called the states,
2. Σ is a ﬁnite set called the alphabet,
3. δ: Q×Σ−→Q is the transition function,1
4. q0 ∈Q is the start state, and
5. F ⊆Q is the set of accept states.
```

### 1.2 Nondeterminism
NFA's will make multiple children or trees, and accept if one of the trees reaches and accept state.
