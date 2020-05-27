strings = {
                ')((||||((((()))))))':5,
                '((((()))()()((((((':3,
                '()))())))(((())))))))':4,
                '))((()))))))':3,
                '(()))))))(((()':2,
                '(())))(((((((()()()()()))))))(((()':11,
                '(())))(((((((()()(())()((()()))()))))))(((()':16
          }

def func(string):
    for i in range(1,len(string)):
        ob = string.find('('*i)
        cb = string.find(')'*i,ob)
        if ob >= cb:break
        sav_ob,sav_cb = ob,cb

    ob,cb = sav_ob,sav_cb
    string = string[ob: cb + i-1]
    j = 0
    while '()' in string:
        j += string.count('()')
        string = string.replace('()','')
    return j

for i in strings:
    assert (func(i) == strings[i]), "Invalid results"

print("PASSED")
