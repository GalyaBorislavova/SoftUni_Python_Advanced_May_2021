parentheses = input()
is_balanced = True

brackets = {"(": ")", "[": "]", "{": "}"}
opening = []
for p in parentheses:
    if p in "([{":
        opening.append(p)
    else:
        if not opening:
            is_balanced = False
            break
        else:
            if not opening:
                is_balanced = False
                break
            current_opening = opening.pop()
            if not brackets[current_opening] == p:
                is_balanced = False
                break

if is_balanced:
    print("YES")
else:
    print("NO")