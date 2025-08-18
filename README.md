# Crumbler
A custom general data compressor

## TEMP INFO
I want to practice some algorithms that I've learned over the years but have never had an opportunity to utilize.

Inside the repo you will find "Rubber_Duck".md files, those are scratch pads where I am essentially writing my thoughts immediately as they come to me and then I evaluate them later after doing some research/ thinking.
I plan on incorporating a form of pattern recognition, RLE, and incorporating a few more novel concepts.

Current design uses a Trie to detect common patterns of designated lengths, however it lacks pruning and the algorithm is reading at the bit level which is a mistake to be fixed (I'll be testing if chunk_sizes is something that can be optimized, specifically for Cache locality when combined with my current inefficient methods)

The code will be written in Python untill i can consistently compress files, then conversion to C for algorithmic sections will take place, using Python as a wrapper.
