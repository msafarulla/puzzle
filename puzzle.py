#Assumption: There would be at least one '()' in the string
strings = {
                ')((ljlkj||||((((()))))))':5,
                '((((()))()()((((((':3,
                '()))())))(((())))))))':4,
                '))((()))))))':3,
                '(()))))))(((()':2,

          }

def fun(string):
    a,b=0,0
    for i in range(1,len(string)+1):
        where_ob = string.find(i*'(')
        where_cb = string.find(i*')',where_ob)
        if where_ob < where_cb:
            a,b=where_ob+i,where_cb+1,
        else:break
    return (i-1)


for i in strings:
    assert (fun(i) == strings[i]), "Invalid results"

print("PASSED")




