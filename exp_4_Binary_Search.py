
from typing import Optional, List, Tuple
from collections import deque
class Node:
    def __init__(self, key):
        self.key = key
        self.count = 1    # number of duplicate entries for this key
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
    def __repr__(self):
        if self.count > 1:
            return f"{self.key}({self.count})"
        return str(self.key)
class BinarySearchTree:
    def __init__(self):
        self.root: Optional[Node] = None

    # --------------- Insert (handle duplicates) ---------------
    def insert(self, key):
        def _insert(node: Optional[Node], key) -> Node:
            if node is None:
                return Node(key)
            if key == node.key:
                node.count += 1
            elif key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)

    # --------------- Search ---------------
    def search(self, key) -> Optional[Node]:
        node = self.root
        while node:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    # --------------- Delete (decrement count if duplicates) ---------------
    def delete(self, key):
        def _min_value_node(node: Node) -> Node:
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node: Optional[Node], key) -> Optional[Node]:
            if node is None:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # Found node
                if node.count > 1:
                    node.count -= 1
                    return node
                # node.count == 1 -> remove node
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    # node with two children: replace with inorder successor
                    succ = _min_value_node(node.right)
                    node.key = succ.key
                    node.count = succ.count
                    # remove successor node(s) from right subtree (set succ's counts consumed)
                    # we must delete successor key succ.count times; but we moved succ.count into node,
                    # so we must remove all copies from the right subtree
                    node.right = _delete_all(node.right, succ.key)
            return node

        def _delete_all(node: Optional[Node], key) -> Optional[Node]:
            # delete all occurrences of key in subtree
            if node is None:
                return None
            if key < node.key:
                node.left = _delete_all(node.left, key)
            elif key > node.key:
                node.right = _delete_all(node.right, key)
            else:
                # remove this node (regardless of count)
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    succ = _min_value_node(node.right)
                    node.key = succ.key
                    node.count = succ.count
                    node.right = _delete_all(node.right, succ.key)
            return node

        self.root = _delete(self.root, key)

    # --------------- Traversals (display tree) ---------------
    def inorder(self) -> List:
        res = []
        def _in(node):
            if node:
                _in(node.left)
                res.append((node.key, node.count))
                _in(node.right)
        _in(self.root)
        return res

    def preorder(self) -> List:
        res = []
        def _pre(node):
            if node:
                res.append((node.key, node.count))
                _pre(node.left)
                _pre(node.right)
        _pre(self.root)
        return res

    def postorder(self) -> List:
        res = []
        def _post(node):
            if node:
                _post(node.left)
                _post(node.right)
                res.append((node.key, node.count))
        _post(self.root)
        return res

    # Print traversal outputs in readable form
    def display_traversals(self):
        def fmt(lst):
            return " ".join(f"{k}" + (f"({c})" if c>1 else "") for k,c in lst)
        return {
            'inorder': fmt(self.inorder()),
            'preorder': fmt(self.preorder()),
            'postorder': fmt(self.postorder())
        }

    # --------------- Depth (height) ---------------
    def depth(self) -> int:
        def _depth(node: Optional[Node]) -> int:
            if node is None:
                return 0
            return 1 + max(_depth(node.left), _depth(node.right))
        return _depth(self.root)

    # --------------- Mirror image ---------------
    def mirror_inplace(self):
        """Convert tree to its mirror in-place."""
        def _mirror(node: Optional[Node]):
            if node:
                node.left, node.right = node.right, node.left
                _mirror(node.left)
                _mirror(node.right)
        _mirror(self.root)

    def mirror_copy(self) -> 'BinarySearchTree':
        """Return a new BST that is the mirror copy of current tree (structure mirrored)."""
        def _mirror_node(node: Optional[Node]) -> Optional[Node]:
            if node is None:
                return None
            new_node = Node(node.key)
            new_node.count = node.count
            # swap left/right when creating copy
            new_node.left = _mirror_node(node.right)
            new_node.right = _mirror_node(node.left)
            return new_node
        new_tree = BinarySearchTree()
        new_tree.root = _mirror_node(self.root)
        return new_tree

    # --------------- Create a (deep) copy ---------------
    def copy(self) -> 'BinarySearchTree':
        def _copy_node(node: Optional[Node]) -> Optional[Node]:
            if node is None:
                return None
            new_node = Node(node.key)
            new_node.count = node.count
            new_node.left = _copy_node(node.left)
            new_node.right = _copy_node(node.right)
            return new_node
        new_tree = BinarySearchTree()
        new_tree.root = _copy_node(self.root)
        return new_tree

    # --------------- Display all parent nodes with their child nodes ---------------
    def display_parents(self) -> List[Tuple]:
        """Return list of tuples (parent_key, left_child_key_or_None, right_child_key_or_None)."""
        res = []
        def _visit(node: Optional[Node]):
            if node:
                left = node.left.key if node.left else None
                right = node.right.key if node.right else None
                if left is not None or right is not None:
                    res.append((node.key, left, right))
                _visit(node.left)
                _visit(node.right)
        _visit(self.root)
        return res

    # --------------- Display leaf nodes ---------------
    def leaf_nodes(self) -> List[int]:
        leaves = []
        def _leaf(node: Optional[Node]):
            if node:
                if node.left is None and node.right is None:
                    leaves.append(node.key)
                _leaf(node.left)
                _leaf(node.right)
        _leaf(self.root)
        return leaves

    # --------------- Display tree level-wise (each level on new line) ---------------
    def level_order(self) -> List[List[Tuple]]:
        """Return list of levels; each level is list of tuples (key, count)."""
        levels = []
        if not self.root:
            return levels
        q = deque([self.root])
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                node = q.popleft()
                level.append((node.key, node.count))
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels.append(level)
        return levels

    # Helper: pretty print level-order
    def print_level_order(self):
        levels = self.level_order()
        for i, level in enumerate(levels, start=1):
            row = " ".join(f"{k}" + (f"({c})" if c>1 else "") for k,c in level)
            print(f"Level {i}: {row}")

    # Utility: clear tree
    def clear(self):
        self.root = None

# ---------------- Example usage / demonstration ----------------
if __name__ == "__main__":
    bst = BinarySearchTree()
    data = [50, 30, 20, 40, 70, 60, 80, 70, 30]  # note duplicates: 70 and 30
    for x in data:
        bst.insert(x)

    print("Traversals:")
    for name, out in bst.display_traversals().items():
        print(f" {name}: {out}")

    print("\nDepth (height) of tree:", bst.depth())

    print("\nLevel-wise display:")
    bst.print_level_order()

    print("\nLeaf nodes:", bst.leaf_nodes())

    print("\nParent nodes with children:")
    for p, l, r in bst.display_parents():
        print(f" Parent {p}: left -> {l}, right -> {r}")

    # Search
    key = 70
    node = bst.search(key)
    print(f"\nSearch for {key}:", "Found" if node else "Not found", f"({node.count})" if node else "")

    # Delete examples (duplicate-aware)
    print("\nDeleting 70 (one occurrence).")
    bst.delete(70)
    print("Search for 70 after one delete:", bst.search(70))
    print("Deleting 70 (second occurrence).")
    bst.delete(70)
    print("Search for 70 after second delete:", bst.search(70))

    print("\nInorder after deletes:", bst.inorder())

    # Mirror copy
    mirrored = bst.mirror_copy()
    print("\nMirrored tree (level-wise):")
    mirrored.print_level_order()

    # Create a deep copy
    copy_tree = bst.copy()
    print("\nCopy tree (level-wise):")
    copy_tree.print_level_order()

    # In-place mirror (on the copy)
    print("\nMirroring the copy in-place...")
    copy_tree.mirror_inplace()
    print("Copy after in-place mirror:")
    copy_tree.print_level_order()






# Experiment No 4: Binary Search Tree (BST) Operations
# COs: CO1, CO2, CO3
# Aim
# Implement a Binary Search Tree (BST) in Python and perform the following operations:
# 1. Insert (handle duplicate entries)
# 2. Delete node
# 3. Search node
# 4. Display tree traversals (Inorder, Preorder, Postorder)
# 5. Display depth of tree
# 6. Display mirror image
# 7. Create a copy of the tree
# 8. Display all parent nodes with their child nodes
# 9. Display leaf nodes
# 10. Display tree level-wise
# Objectives
# ● Understand BST properties: left child < parent < right child.
# ● Implement insert, delete, search operations efficiently.
# ● Visualize tree traversals and understand recursive and iterative methods.
# ● Explore tree depth, mirror image, copy, and level-wise traversal.
# Theory
# Binary Search Tree (BST)
# ● A BST is a node-based binary tree with the following properties:
# ○ Left subtree of a node contains values less than the node’s value.
# ○ Right subtree contains values greater than the node’s value.
# ○ No duplicate nodes (optional, but can be handled during insertion).
# ● Each node contains:
# ○ data (value)
# ○ left (pointer to left child)
# ○ right (pointer to right child)

# Advantages of BST
# ● Efficient search, insertion, and deletion: average O(log n) time if balanced.
# ● Supports ordered traversal (Inorder gives sorted output).
# ● Basis for more advanced trees: AVL, Red-Black Trees.
# Tree Operations
# 1. Insertion
# ○ Traverse BST starting from root.
# ○ If value < current node → move left; if > → move right.
# ○ Insert at appropriate null child.
# ○ Handle duplicates by ignoring or storing count.
# 2. Deletion
# ○ Three cases:
# 1. Node is leaf → remove directly.
# 2. Node has one child → replace node with child.
# 3. Node has two children → replace node with inorder successor (smallest in right
# subtree) or inorder predecessor.
# 3. Search
# ○ Traverse left or right depending on comparison until value found or null reached.
# 4. Tree Traversals
# ○ Inorder (LPR) → Left, Parent, Right → sorted output
# ○ Preorder (PLR) → Parent, Left, Right
# ○ Postorder (LRP) → Left, Right, Parent
# 5. Depth / Height of Tree
# ○ Depth = maximum number of nodes from root to leaf.

# 6. Mirror Image
# ○ Swap left and right children recursively for all nodes.
# 7. Copy Tree
# ○ Recursively create new nodes with same data and structure.
# 8. Parent-Child Display
# ○ Traverse tree and print node along with left and right child if exists.
# 9. Leaf Nodes
# ○ Nodes with no left or right child.
# 10. Level-wise Display (Breadth First)
# ○ Traverse using queue (BFS) to display nodes level by level.
# Observation / Result
# ● BST insertion handles duplicate nodes.
# ● Traversals display tree in different orders.
# ● Deletion and search operations work correctly.
# ● Mirror image, copy, parent-child, leaf nodes, and level-wise traversal executed successfully.
# Conclusion
# ● BST implemented with all major operations in Python.
# ● Students understand recursion, tree traversal, and advanced BST functionalities.
# ● BST supports efficient searching, insertion, deletion, and visualization.




# Experiment 04:
# Implement binary search tree and perform following operations:
# a. Insert (Handle insertion of duplicate entry)
# b. Delete
# c. Search
# d. Display tree (Traversal)
# e. Display - Depth of tree
# f. Display - Mirror image
# g. Create a copy
# h. Display all parent nodes with their child nodes
# i. Display leaf nodes
# j. Display tree level wise
# Python Code
# class Node:
#  def __init__(self, data):
#  self.data = data
#  self.left = None
#  self.right = None
# class BST:
#  def __init__(self):
#  self.root = None
#  # Insert node
#  def insert(self, root, key):
#  if root is None:
#  return Node(key)
#  if key < root.data:
#  root.left = self.insert(root.left, key)
#  elif key > root.data:
#  root.right = self.insert(root.right, key)
#  else:
#  print(f"Duplicate {key} ignored")
#  return root
#  # Search node
#  def search(self, root, key):
#  if root is None:
#  return None
#  if key == root.data:
#  return root
#  elif key < root.data:
#  return self.search(root.left, key)
#  else:
#  return self.search(root.right, key)
#  # Find minimum (for deletion)


#  def minValueNode(self, node):
#  current = node
#  while current.left is not None:
#  current = current.left
#  return current
#  # Delete node
#  def delete(self, root, key):
#  if root is None:
#  return root
#  if key < root.data:
#  root.left = self.delete(root.left, key)
#  elif key > root.data:
#  root.right = self.delete(root.right, key)
#  else:
#  if root.left is None:
#  return root.right
#  elif root.right is None:
#  return root.left
#  temp = self.minValueNode(root.right)
#  root.data = temp.data
#  root.right = self.delete(root.right, temp.data)
#  return root
#  # Traversals
#  def inorder(self, root):
#  return self.inorder(root.left) + [root.data] + self.inorder(root.right) if root else []
#  def preorder(self, root):
#  return [root.data] + self.preorder(root.left) + self.preorder(root.right) if root else []
#  def postorder(self, root):
#  return self.postorder(root.left) + self.postorder(root.right) + [root.data] if root else []
#  # Height of tree
#  def height(self, root):
#  if root is None:
#  return 0
#  return 1 + max(self.height(root.left), self.height(root.right))
#  # Mirror image
#  def mirror(self, root):
#  if root:
#  root.left, root.right = root.right, root.left
#  self.mirror(root.left)
#  self.mirror(root.right)
#  # Copy tree
#  def copyTree(self, root):
#  if root is None:
#  return None
#  new_root = Node(root.data)
#  new_root.left = self.copyTree(root.left)
#  new_root.right = self.copyTree(root.right)
#  return new_root
#  # Display parent-child nodes

# NAVSAHYADRI EDUCATION SOCIETY’S, GROUP OF INSTITUTIONS
#  Savitribai Phule Pune University
# Second Year of Artificial Intelligence and Machine Learning (2024 Course)
# Course Code: PCC-204-AIM Course Name: Data Structures & Algorithms Lab
# 6 Asst.Prof.Salunkhe A.A
#  def displayParentChild(self, root):
#  if root:
#  left = root.left.data if root.left else None
#  right = root.right.data if root.right else None
#  print(f"Parent: {root.data}, Left: {left}, Right: {right}")
#  self.displayParentChild(root.left)
#  self.displayParentChild(root.right)
#  # Display leaf nodes
#  def displayLeafNodes(self, root):
#  if root:
#  if not root.left and not root.right:
#  print(root.data, end=' ')
#  self.displayLeafNodes(root.left)
#  self.displayLeafNodes(root.right)
#  # Level-wise traversal
#  def levelOrder(self, root):
#  if not root:
#  return
#  queue = [root]
#  while queue:
#  node = queue.pop(0)
#  print(node.data, end=' ')
#  if node.left: queue.append(node.left)
#  if node.right: queue.append(node.right)
#  print()
# # --- Driver Code ---
# bst = BST()
# root = None
# # Insert nodes
# nodes = [50, 30, 70, 20, 40, 60, 80, 70] # includes duplicate 70
# for n in nodes:
#  root = bst.insert(root, n)
# print("Inorder Traversal:", bst.inorder(root))
# print("Preorder Traversal:", bst.preorder(root))
# print("Postorder Traversal:", bst.postorder(root))
# print("Height of tree:", bst.height(root))
# # Search
# key = 40
# found = bst.search(root, key)
# print(f"Search {key}:", "Found" if found else "Not Found")
# # Delete
# root = bst.delete(root, 20)
# print("Inorder after deleting 20:", bst.inorder(root))
# # Mirror
# bst.mirror(root)
# print("Inorder of Mirror Tree:", bst.inorder(root))
# bst.mirror(root) # restore original
# # Copy
# copy_root = bst.copyTree(root)

# NAVSAHYADRI EDUCATION SOCIETY’S, GROUP OF INSTITUTIONS
#  Savitribai Phule Pune University
# Second Year of Artificial Intelligence and Machine Learning (2024 Course)
# Course Code: PCC-204-AIM Course Name: Data Structures & Algorithms Lab
# 7 Asst.Prof.Salunkhe A.A
# print("Inorder of Copy Tree:", bst.inorder(copy_root))
# # Parent-Child
# print("Parent-Child Nodes:")
# bst.displayParentChild(root)
# # Leaf Nodes
# print("Leaf Nodes:", end=' ')
# bst.displayLeafNodes(root)
# print()
# # Level-wise
# print("Level-wise Traversal:", end=' ')
# bst.levelOrder(root)


# Output
# Duplicate 70 ignored
# Inorder Traversal: [20, 30, 40, 50, 60, 70, 80]
# Preorder Traversal: [50, 30, 20, 40, 70, 60, 80]
# Postorder Traversal: [20, 40, 30, 60, 80, 70, 50]
# Height of tree: 3
# Search 40: Found
# Inorder after deleting 20: [30, 40, 50, 60, 70, 80]
# Inorder of Mirror Tree: [80, 70, 60, 50, 40, 30]
# Inorder of Copy Tree: [30, 40, 50, 60, 70, 80]
# Parent-Child Nodes:
# Parent: 50, Left: 30, Right: 70
# Parent: 30, Left: None, Right: 40
# Parent: 40, Left: None, Right: None
# Parent: 70, Left: 60, Right: 80
# Parent: 60, Left: None, Right: None
# Parent: 80, Left: None, Right: None
# Leaf Nodes: 40 60 80
# Level-wise Traversal: 50 30 70 40 60 80 