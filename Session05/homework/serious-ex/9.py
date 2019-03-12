def get_even_list(ls):
    for i in list(ls):
        if i%2 !=0:
            ls.remove(i)
    return(ls)
print(get_even_list([-15,-10,-5,0,5,10,15]))