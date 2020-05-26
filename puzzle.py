strings = {
                '))))))))))))))':0,
                '((((((((':0,
                ')((ljlkj||||((((()))))))':5,
                '((((()))()()((((((':3,
                '()))())))(((())))))))':4,
                '))((()))))))':3,
                '(()))))))(((()':2,
                '(())))(((((((()()()()()))))))(((()':7,
                '(())((((((((((((((((((((((((()))))))))))))))))))))))))':25,

          }

def func(string=''):
    for i in range(1,len(string)+1):
        if '()' not in string: break
        if  (ob:=string.find(i * '(')) >= (cb:=string.find(i *')', ob)):
           break
    return (i-1)


for i in strings:
    assert (func(i) == strings[i]), "Invalid results"

print("PASSED")