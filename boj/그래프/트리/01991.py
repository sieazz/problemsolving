import sys
from collections import defaultdict


tree = defaultdict(list)
N = int(sys.stdin.readline())
for _ in range(N):
    line = sys.stdin.readline().split(" ")
    tree[line[0]] = [line[1], line[2].rstrip()]


def preorder_traversal(node, tree):
    if node.isalpha():
        print(node, end='')
        preorder_traversal(tree[node][0], tree)
        preorder_traversal(tree[node][1], tree)


def inorder_traversal(node, tree):
    if node.isalpha():
        inorder_traversal(tree[node][0], tree)
        print(node, end='')
        inorder_traversal(tree[node][1], tree)


def postorder_traversal(node, tree):
    if node.isalpha():
        postorder_traversal(tree[node][0], tree)
        postorder_traversal(tree[node][1], tree)
        print(node, end='')


preorder_traversal('A', tree)
print()
inorder_traversal('A', tree)
print()
postorder_traversal('A', tree)
print()