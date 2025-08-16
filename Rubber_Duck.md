use codes and buffers for encoding decoding

I believe 3 bit codes will be sufficient
like op codes with functions

000 & 001 could be a zero/one fill and the next 2 bits can be how many bytes to read for the number of bits to fill.

010, can be to "save this x bits as a pattern" and then if we call 011 we can say "use x pattern here". so the table is only generated as it's needed.
    we should aim to save a predictable amount of patterns, that way we dont need to dynamically change the amount of bits to use as a calling card. so 2 bits can represent 4 patterns

100 could be to progress past x bits since we couldnt compress it on this iteration

101 could be to modify a saved pattern and use it as the next block
    we'd need to have a simple way to determine the modification, like a xoring with b (a action turns into b). 

110 this can represent a different set of actions TBD

111 can be to terminate this encoding iteration

the first few bits of a passed compressed bitstream should be the number of iterations to decode on
    every time we compress the stream, we can then recompress the compressed stream incase theres new overlap detected


we need a function that can modularly check if usage of an OP code will be profitable

we need to detect running lengths of 0 or 1
    determining length is the priority

we need to recognize a sequence that can be saved and used repetitively
    this sequence needs to be used in the current compression iteration or potentially future iterations
    we can potentially recognize the sequence by using a tree that counts the amount of times a node is hit and it'll just be 0's and 1's going left or right. 
    whichever node has a large number is the most common sequence of that length

we need to check if a saved function can be easily modified into the next chunk of code.
    we can use the saved sequence / binary tree to see if the current codes inverse or "mate" exists as a popular sequence

we need to write the compressed file in a way that we can read it again for subsequent iterations/ passes

we have to determine when we should terminate (there will be no more OP codes after this one / break iteration)

we need to repeat all processes on the written compression until we dont make any more progress



ok so the first pass through the binary should check for running 0/1's and construct a tree when not in a repetative sequence
    need to ensure that when the repatition is swapped to an opcode, that the tree doesnt have invalid additions due to that binarys removal
    we could also construct a second tree for complements to see if theres a popular pattern that can be used to change the current chunk into running sequences which can be swapped out and paired with the xor to get it back

the second pass should swap the repeat sections with the opcode, insert opcodes for when to save/use a sequence, and check sequence, and utilize the complement tree 


things to consider:
    when should we determine the length of a code for our tree? what if the first half of the binary is the same as the second half?

    if something repeats itself and we swap it half-assed with shorter codes than optimal, would it still not be repetative after the added opcode?
    would another pass then detect that pattern?
    would our OPcodes not be extremely repetative and qualify for substitution with a pattern, or given their short length would the modular funciton checker block it since it wont be profitable.



    using a tree would eventually need to utilize disk space for long binary sequences (potentially trying to save billions of elements)
    we could have a pointer run twice as fast as the main pointer, that way when it hits the end, we know we are halfway through the code and we can prune the tree of any invalid candidates
    but we'd still have n/2 saved on diskspace

    but thats only for compression, the decompression would only store a single OPcode with a length of memory to save, to reuse that code no matter how long it is.

    so if we save half the code and magically can use it for the last half, then we'd find the most optimal pattern possible
