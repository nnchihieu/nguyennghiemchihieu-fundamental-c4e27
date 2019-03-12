def get_even_list(ls):
    for i in list(ls):
        if i%2 !=0:
            ls.remove(i)
    return(ls)
even_list = get_even_list([-15,-10,-5,0,5,10,15])
if set(even_list) == set([-10,0,10]):
    print('your function is correct')
else:
    print('Ooops, bugs detected')