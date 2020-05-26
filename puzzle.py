strings = {
                '))))))))))))))':0,
                '((((((((':0,
                ')((ljlkj||||((((()))))))':5,
                '((((()))()()((((((':5,
                '()))())))(((())))))))':6,
                '))((()))))))':3,
                '(()))))))(((()':3,
                '(())))(((((((()()()()()))))))(((()':14,
                '(())))(((((((()()(())()((()()))()))))))(((()':19
          }

def func(string):
    j=0
    while '()' in string:
        j+=string.count('()')
        string = string.replace('()','')
    return j

for i in strings:
    assert (func(i) == strings[i]), "Invalid results"

print("PASSED")
