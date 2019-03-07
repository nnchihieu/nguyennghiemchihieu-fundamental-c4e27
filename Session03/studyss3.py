
# #1
# nested list trong python có thể dc hiểu như là 1 mảng dưới dạng ma trận kích cỡ mxn
l = [[2,2,2],[3,3,3],[4,4,4]
for i1 in xrange(len(l)):
    for i2 in xrange(len(l[i1])):
        print i1, i2, l[i1][i2]
# #2
# trong list có thể dùng cả str và int
a=['hieu', 1, 'jk', 2]
print(a) 