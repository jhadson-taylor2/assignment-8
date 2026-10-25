class DoctorNode:
  def __init__(self, name):
    self.name = name
    self.left = None
    self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None

    def _find(self, node, name):
        """Return the node with the given name, or None."""
        if node is None:
            return None
        if node.name == name:
            return node
        return self._find(node.left, name) or self._find(node.right, name)
    def insert(self, parent_name, name, side):
        if side not in ("left", "right"):
            raise ValueError(f"Invalid side '{side}': use 'left' or 'right'.")
        parent = self._find(self.root, parent_name)
        if parent is None:
            raise ValueError(f"Parent '{parent_name}' not found in tree.")
        if getattr(parent, side) is not None:
            raise ValueError(f"{parent_name} already has a {side} report.")
        setattr(parent, side, DoctorNode(name))
 
    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)
    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)
 
    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")    

    assert tree.preorder(tree.root) == ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]
    assert tree.inorder(tree.root) == ["Dr. Morgan", "Dr. Phan", "Dr. Carson", "Dr. Croft", "Dr. Goldsmith"]
    assert tree.postorder(tree.root) == ["Dr. Morgan", "Dr. Carson", "Dr. Phan", "Dr. Goldsmith", "Dr. Croft"]
 
    
    for args in [("Dr. Nobody", "Dr. X", "left"),    
                 ("Dr. Croft", "Dr. X", "middle"),  
                 ("Dr. Croft", "Dr. X", "left")]:    
        try:
            tree.insert(*args)
            raise AssertionError("expected ValueError")
        except ValueError as e:
            print("OK:", e)
 
    empty = DoctorTree()
    assert empty.preorder(empty.root) == []
    print("All doctor tree tests passed.")
