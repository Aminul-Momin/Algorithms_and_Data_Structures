
def decode_encoded_str(s):
    stk = []
    
    for cur_char in s:
        if cur_char == "]":
            cur_str = ""
            while stk[-1] != "[": cur_str = stk.pop() + cur_str
            
            stk.pop()
            
            cur_count = ""
            while stk and stk[-1].isdigit(): cur_count = stk.pop() + cur_count
            
            stk.append(cur_str*int(cur_count))

        else: stk.append(cur_char)

    return "".join(stk)


def _test_decode_encoded_str():

    test_cases = [
        ("", ""),
        ("a", "a"),
        ("1[a]", "a"),
        ("3[a]2[bc]", "aaabcbc"), 
        ("3[a2[c]]", "accaccacc"), 
        ("2[abc]3[cd]ef", "abcabccdcdcdef")
    ]

    for test_case, expected in test_cases:
        returned1 = decode_encoded_str(test_case)
        try:
            assert returned1 == expected
        except:
            print(f"Given: {test_case} \n\tReturned:{returned1} \n\tExpected: {expected}")
#==================================================================================

if __name__ == "__main__":
    _test_decode_encoded_str()