import re

def Horn(formula):
    marked = set()
    clauses = re.findall(r"\(([^()]*?->[^()]*?)\)", formula)

    # Step 1 of algo, where we find the pattern T->p, and mark p as True
    for clause in clauses:
        if re.match(r'T->.+', clause):
            marked.add(clause[3])

    # Step 2 of algo, where we find all the marked hypothesis, and then check the conclusion
    for clause in clauses:
        match = re.match(r'([^->T]+)->(.+)', clause)
        if match:
            left, right = match.groups()
            props = left[0].split('^')

        if set(props).issubset(marked):
            if right != 'F':
                marked.add(right)
            else:
                return 0
            
    # Step 3 of algo, where we conclude, that the formula is satisfiable
    return 1
    
if __name__ == '__main__':
    formula = input("Enter a valid Horn Formula: ")
    # formula = "(s->q)^(T->s)^(q^s->p)"
    print(f"The formula is {'satisfiable' if Horn(formula) else 'not satisfiable'}")