class Tree:
    def __init__(self):
        self.children = []
        self.parent = None
        self.size = None
        self.name = ""


class DirCrawler:
    def __init__(self, f):
        # The tree always starts at the root directory
        self.tree = Tree()
        self.tree.name = "/"
        self.currnode = self.tree

        # We need a file reference to read line by line
        self.file = f

        # The first line is discarded
        self.file.readline()
        self.parse()

    def parse(self):
        while True:
            # split the line by whitespaces
            line = self.file.readline().split()

            # end of file
            if not line:
                break

            # command, either cd or ls
            # cd changes the current directory, ls does nothing
            if line[0] =="$":
                if line[1] == "cd":
                    if line[2] == "..":
                        self.currnode = self.currnode.parent
                    else:
                        #change current node to the first one in this level with a matching name
                        self.currnode = self.first(line[2])

                elif line[1] == "ls":
                    continue

            # add a directory node to the tree
            elif line[0] =="dir":
                tree = Tree()
                tree.name = line[1]
                tree.parent = self.currnode
                self.currnode.children.append(tree)

            # add a file node to the tree
            else:
                tree = Tree()
                tree.name = line[1]
                tree.size = int(line[0])
                tree.parent = self.currnode
                self.currnode.children.append(tree)

        # after creating the tree, find suitable folders and add their sizes
        t,aux=totalspace(self.tree,[])
        print(sum(aux))

    def first(self, n):
        for x in self.currnode.children:
            if x.name == n:
                return x

def totalspace(tree,acc):
    # file
    if not tree.children:
        return tree.size, acc
    # directory
    else:
        total = sum([totalspace(x,acc)[0] for x in tree.children])
        if total <=100000:
            acc.append(total)
        return total,acc


# def printInorder(root):
#     print(f"{root.name} {root.size}")
#     if root.children:
#         print("dir")
#         [printInorder(x) for x in root.children]


import os
with open(os.path.join(os.getcwd(), "input.txt")) as f:
    DirCrawler(f)

