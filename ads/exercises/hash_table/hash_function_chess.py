"""
The state of a game of chess is determined by what piece is present on each square, as illustrated inFigure 72.2 on the following page. Each square may be empty, or have one of six classes of pieces;each piece may be black or white. Thus flog(1 + 6 x 2)l = 4 bits suffice per square, which means thatatotal of &x4=2i6bitscanrepresentthestateof thechessboard. (Theactualstateof thegameisslightly more complex, as it needs to capture which side is to move, castling rights, en pnssant, etc.,but we will use the simpler model for this question.)Chess playing computers need to store sets of states, e.g., to determine if a particular state hasbeen evaluated before, or is known to be a winning state. To reduce storage, it is natural to applya hash function to the 256 bits of state, and ignore collisions. The hash code can be computed bya conventional hash function for strings. However, since the computer repeatedly explores nearbystates, it is advantageous to consider hash functions that can be efficiently computed based onincremental changes to the board.Design a hash function for chess game states. Your function should take a state and the hash codefor that state, and a move, and efficiently compute the hash code for the updated state.
"""