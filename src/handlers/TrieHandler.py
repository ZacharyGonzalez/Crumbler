from collections import deque
from typing import Deque, List, Tuple, Iterable

class TrieNode:
    __slots__ = ['children', 'count']
    def __init__(self):
        self.children = {}  # 0 or 1 -> TrieNode
        self.count = 0

# Binary tree pathing
def _insert_trie(root: TrieNode, bits: Deque[int]):
    node = root
    for bit in bits:
        if bit not in node.children:
            node.children[bit] = TrieNode()
        node = node.children[bit]
    node.count += 1

def build_bit_trie(bit_iter:Iterable[int], seq_len: int = 20) -> TrieNode:
    """Takes a sequence of bits and adds them to a Tree containing count of occurences, in a specific order"""
    root = TrieNode()
    buffer:deque[int] = deque(maxlen=seq_len)
    for bit in bit_iter:
        buffer.append(bit)
        if len(buffer) == seq_len:
            _insert_trie(root, buffer)
    return root

def collect_top_patterns(root: TrieNode, max_results:int=10) -> List[Tuple[List[int], int]]:
    """Returns a list of candidates for pattern matching and their occurences: """
    results = []
    def dfs(node: TrieNode, path: Deque[int]):
        if node.count > 0:
            results.append((list(path), node.count))
        for bit, child in node.children.items():
            path.append(bit)
            dfs(child, path)
            path.pop()
    dfs(root, deque())
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:max_results]
