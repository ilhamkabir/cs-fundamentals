def is_palindrome(s):
    result = True
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            result = False
    print(s, result)
    return result

def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    
    result = []
    def f(s, slate, idx_last_pipe):
        # backtrack case
        if slate[len(slate)-2] == '|':
            if len(slate) > 2:
                _is_palindrome = is_palindrome(slate[idx_last_pipe+1:len(slate)-2])
                if not _is_palindrome:
                    return
            idx_last_pipe = len(slate)-2
        # base case
        if len(s) == 0:
            if is_palindrome(slate[idx_last_pipe+1:]):
                result.append(slate[1:])
            return
        # recursive case
        #no pipe
        f(s[1:], slate+s[0], idx_last_pipe)
        # pipe 
        f(s[1:], slate+'|'+s[0], idx_last_pipe)
    
    f(s[1:], '|' + s[0], 0)
    
    return result



s = 'abracadabra'
r = generate_palindromic_decompositions(s)
print(r)

# r = is_palindrome('ab')
# print(r)