# B.-Not-Quite-Latin-Square
t = int(input())
for _ in range(t):
    _matt = []
    for i in range(3):
        s = input()
        _matt.append(s)
    for j in _matt:
        if "A" not in j:
            print("A")
        elif "B" not in j:
            print("B")
        elif "C" not in j:
            print("C")
