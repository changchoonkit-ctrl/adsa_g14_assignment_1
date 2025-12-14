"""Binary tree skeleton for loyalty module."""
from typing import Optional, TypeVar
from src.pos_system.common.interfaces import Node, TreeInterface
T = TypeVar("T")

class BSTNode:
    def __init__(self, customer):
        self.customer = customer
        self.left = None
        self.right = None

class BSTTree(TreeInterface[T]):
    def __init__(self):
        self.root = None

    def insert(self, customer, action_from = ""):
        if(action_from == "Register"):
            if self.search(customer.customer_id) is not None:
                return False

        # Customer does not exist, perform insertion
        def _insert(node, customer):
            if not node:
                return BSTNode(customer)
            if customer.customer_id < node.customer.customer_id:
                node.left = _insert(node.left, customer)
            else:
                node.right = _insert(node.right, customer)
            return node

        self.root = _insert(self.root, customer)
        return True

    def search(self, customer_id):
        node = self.root
        while node:
            if customer_id < node.customer.customer_id:
                node = node.left
            elif customer_id > node.customer.customer_id:
                node = node.right
            else:
                return node.customer
        return None
    
    def inorder_traversal(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left, result)
        result.append(node.customer)
        if node.right:
            self.inorder_traversal(node.right, result)
        return result
    
    def traverse(self):
        """Implements the abstract traverse method (in-order by default)."""
        return self.inorder_traversal()
    
    def delete(self, customer_id):
        def _delete(node, customer_id):
            if not node:
                return None
            if customer_id < node.customer.customer_id:
                node.left = _delete(node.left, customer_id)
            elif customer_id > node.customer.customer_id:
                node.right = _delete(node.right, customer_id)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                # Node with two children: get inorder successor
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.customer = succ.customer
                node.right = _delete(node.right, succ.customer.customer_id)
            return node
        self.root = _delete(self.root, customer_id)

