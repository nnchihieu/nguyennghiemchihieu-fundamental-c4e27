def is_inside(diem,hcn):
    if hcn[0] <= diem[0] <= hcn[0] + hcn[2] and hcn[1] <= diem[1] <= hcn[1] + hcn[3]:
        return True
    else:
        return False
print(is_inside([125,150], [100,50,200,150]))
