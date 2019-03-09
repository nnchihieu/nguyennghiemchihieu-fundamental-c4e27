inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll'],
}
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory["backpack"].remove("dagger")
inventory["gold"] += 50
print("hàng tồn kho: ", inventory)