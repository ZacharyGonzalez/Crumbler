import sys
from src.handlers import TrieHandler
from src.handlers.FileHandler import FileHandler
from src.handlers.BitHandler import BitHandler
import cProfile

VERIFY = True  # Toggle verification

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        return

    fh = FileHandler()
    file_path = fh.load_path(sys.argv[1])

    # --- Step 1: find trie patterns ---
    root = TrieHandler.build_bit_trie(BitHandler.bit_stream(file_path), seq_len = 10)
    top_patterns = TrieHandler.collect_top_patterns(root, max_results = 5)
    for pattern in top_patterns:
        print("Top patterns:", pattern)

    # --- Step 1.5: find optimal seq_len ---
        # maybe grab lens of 30, remove them, then go over remainder with len of 25, 20, 15, 10, until down to 5


    # --- Step 2: pass through linearly and compare if pattern match, place location as where to insert for dict---
        # The values for the keys should be inspected for which one is the smallest as that should be the next placement

    # --- Step 3: check if the removal of those patterns has created any new patterns
        # repeat step 1 and 2
    
    # --- step 4: repeat step 3 as many times as the memory saving is greater than than the tables expansion (we can use -1 as an index position to say halt additions for this key until all keys have depleted)

    # --- step 5: verify original bit len is the same as the decoded bit len
if __name__ == "__main__":
    cProfile.run("main()")
