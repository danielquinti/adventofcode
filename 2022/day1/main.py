import os
# with open(os.path.join(os.getcwd(), "input.txt")) as f:
#     max = 0
#     acc = 0
#     for line in f:
#         trimmed_line = line.rstrip()
#         if trimmed_line == "":
#             if acc > max:
#                 max = acc
#             acc=0
#         else:
#             acc+=int(trimmed_line)
#     print(max)

import queue


with open(os.path.join(os.getcwd(), "input")) as f:
    top3 = queue.PriorityQueue(maxsize=3)
    acc = 0
    for line in f:
        trimmed_line = line.rstrip()
        if trimmed_line == "":
            try:
                top3.put(acc,block=False)
            except queue.Full:
                curr_third = top3.get(block=False)
                if curr_third < acc:
                    top3.put(acc,block=False)
                else:
                    top3.put(curr_third,block=False)

            finally:
                acc=0
        else:
            acc+=int(trimmed_line)
    print(sum([top3.get(block=False) for i in range(3)]))