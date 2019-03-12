def remove_dollar_sign(os):
    ns=os.replace('$', '')
    return ns
os = input('dollar($): ')
print(remove_dollar_sign(os))