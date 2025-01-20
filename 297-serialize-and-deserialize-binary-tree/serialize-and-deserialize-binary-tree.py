# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        
        treeString = ""
        queue = deque()
        queue.append(root)
        while queue:
            currNode = queue.popleft()
            if currNode is None:
                treeString += "#,"
            else:
                val = currNode.val
                treeString += f'{val},'
                queue.append(currNode.left)
                queue.append(currNode.right)
        
        return treeString
 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        dataList = data.split(",")
        root = TreeNode(int(dataList[0]))
        dataList.pop()
        queue = deque()
        queue.append(root)
        i = 0
        while queue:
            node = queue.popleft()
            if dataList[i+1] != "#":
                newNode = TreeNode(int(dataList[i+1]))
                node.left = newNode
                queue.append(newNode)
            
            if dataList[i+2] != "#":
                newNode = TreeNode(int(dataList[i+2]))
                node.right = newNode
                queue.append(newNode)
            
            i = i+2
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))