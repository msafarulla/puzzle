string=')))()((((ljlkj||||((((()))))))'
for i in range(1,len(string)+1):
    where_ob = string.find(i*'(')
    where_cb = string.find(i*')',where_ob)
    if where_ob < where_cb:
        a,b=where_ob+i,where_cb+1,
    else:
        print(a, b, i-1)
        break






