from itertools import groupby
from random import randint
# ========================================================================

# Pythonic solution uses the power of itertools.groupby().
def look_and_say_pythonic(n: int) -> str:
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + key for key, group in groupby(s))
    return s

def look_and_say(n: int) -> str:
    
    def get_cur_seq(seq):
        if not seq: return ''
        count, seq_parts = 0, []
        
        for idx, char in enumerate(seq):
            if idx and char != seq[idx-1]:
                seq_parts.append(str(count) + seq[idx-1])
                count = 1
            else: count += 1
        
        seq_parts.append(str(count) + seq[-1])
                
        return ''.join(seq_parts)
    
    if not n: return ''
    if n == 1: return '1'
    cur_seq = '1'
    
    for i in range(2, n+1):
        cur_seq = get_cur_seq(cur_seq)
    
    return cur_seq

def _test_look_and_say():
    for i in range(1, 11):
        n = randint(10, 50)
        returned = look_and_say(n)
        expected = look_and_say_pythonic(n)
        # print(ret, look_and_say(i))
        try:
            # print(f"Given {n}", f"Expected {expected}", f"Returned {returned}", '='*60, sep='\n')
            assert returned == expected
        except:
            print(f"Given {n}", f"Expected {expected}", f"Returned {returned}", '='*60, sep='\n')
# ===============================================================        
# ===============================================================   

if __name__ == "__main__":
    _test_look_and_say()