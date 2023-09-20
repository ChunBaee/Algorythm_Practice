from collections import deque

deq = ["#", "+", "+", "+", "+"]
deq = deque(deq)
for i in range(0, 5):
    print("".join(deq))
    deq.rotate(1)