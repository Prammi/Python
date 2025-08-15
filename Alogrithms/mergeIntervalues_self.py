intervals = [[1, 6], [2, 7], [8, 10], [15, 18],[16,100],[17,1000]]
output=[]
tempResult=[intervals[0]]
for i in range(1,len(intervals)):
    if intervals[i][0]<tempResult[-1][1]:
        tempResult[-1][1]=max(intervals[i][1], tempResult[-1][1])
    else:
        tempResult.append(intervals[i])
        
print(tempResult)