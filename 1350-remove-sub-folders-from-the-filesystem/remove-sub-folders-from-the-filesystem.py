class Node:
    def __init__(self):
        self.children = {}
        self.flag = False

class Trie:
    def __init__(self, root = None):
        self.root = Node()
        # print(self.root.children)

    def insert(self, folder):
        i = 0
        node = self.root
        while i < len(folder):
            if folder[i] == '/':
                i = i+1
                continue
            folder_name = ''
            while i < len(folder) and folder[i] != '/':
                folder_name = folder_name + folder[i]
                i = i + 1
            # print(self.root)
            if node.flag:
                return

            if folder_name not in node.children:
                node.children[folder_name] = Node()
            node = node.children[folder_name]
        
        node.flag = True
        
    
    def findRoot(self, node = None, path=""):
        if node is None:
            node = self.root
        result = []
        if node.flag:
            result.append(path)  # Add this folder to results if it's marked as a root
        else:
            for folder_name, child_node in node.children.items():
                result.extend(self.findRoot(child_node, path + '/' + folder_name))
        return result


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for sub in folder:
            trie.insert(sub)
        # result = trie.findRoot()
        return trie.findRoot()
        