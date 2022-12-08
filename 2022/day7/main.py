class Tree:
    def __init__(self):
        self.children = []
        self.parent = None
        self.size = None
        self.name = ""


class DirCrawler:


    def __init__(self, f):
        self.tree = Tree()
        self.tree.name = "/"
        self.currnode = self.tree
        self.file = f
        self.file.readline()
        self.parse()

    def parse(self):
        while True:
            line = self.file.readline().split()
            if not line:
                break

            print(line)
            if line[0] =="$":
                if line[1] == "cd":
                    if line[2] == "..":
                        self.currnode = self.currnode.parent
                    else:
                        self.currnode = self.first(line[2])
                elif line[1] == "ls":
                    pass
            elif line[0] =="dir":
                tree = Tree()
                tree.name = line[1]
                tree.parent = self.currnode
                self.currnode.children.append(tree)

            else:
                tree = Tree()
                tree.name = line[1]
                tree.size = line[0]
                tree.parent = self.currnode
                self.currnode.children.append(tree)

    def first(self, n):
        for x in self.currnode.children:
            print(type(x))
            if x.name == n:
                return x


import os
with open(os.path.join(os.getcwd(), "input.txt")) as f:
    DirCrawler(f)

