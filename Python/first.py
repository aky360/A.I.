print("Hello World")



# date 5_1_23



import random
import numpy as np
# import matplotlib as plt
# print(plt)

# print(random.randint(2, 10))
low1 = [random.randint(i**4, i**5) for i in range(10)]
low1[5] = 0
low1.append(0)
print(low1)
# print(low1.shift())
print(max(low1[-1], low1[-2]))
i = 0
newlist = []
while(i<len(low1)-1):
    # if(low1[i]!=0):
    #     newlist.append(low1[i])
    #     print(newlist[i-1])
    # else:
    #     newlist.append(low1[i-1])
    if(low1[i-1]<(low1[i]+low1[i-1])):
        newlist.append(low1[i-1])
    else:
        newlist.append(low1[i])
    i = i+1
        
        
# plt.plot(newlist, newlist)
print(newlist)

a_list = [10, 11, 14, 23, 9, 3, 35, 22]
an_array = np.array(a_list)
print(an_array)
index = np.argmax(an_array)

print(index)
    


  
 ###########################################################################################################3


# a_list = [10, 11, 14, 23, 9, 3, 35, 22]

# max_value = max(a_list)
# max_index = a_list.index(max_value)

# print(max_index)


def findMaxIndex(lst):
    max_index = lst.index(max(lst))
    return max_index-len(lst)

a_list = [10, 11, 14, 23, 9400, 3000, 35000, 2200]

def findMaxIndxInterval(val, lst):
    if(val <= 0):
        return 0
    elif(val > len(lst)):
        return 'value is beyond the list'
    else:
        maxval = 0
        for i in range(val):
            if(lst[len(lst)-1-i] > maxval):
                maxval = lst[len(lst)-1-i]
        return lst.index(maxval)-len(lst)



print(findMaxIndxInterval(8, a_list))

# maxval = 0
# for i in range(-4):
#     if a_list[i] > maxval:
#         pass

# print(findMaxIndex(a_list))

# def findMaxIndx(int1, int2):
#     pass


###########################################################################################################


a_list = [10, 11, 14, 23, 93, 3, 35, 22]
maxval = 0
for i in range(5):
    if(a_list[len(a_list)-1-i] > maxval):
        maxval = a_list[len(a_list)-1-i]
    # print(i, max(a_list[len(a_list)-1-i], a_list[len(a_list)-1-i-1]), ' ', a_list[len(a_list)-1-i])
    
    
print(a_list.index(35)-len(a_list))
print(maxval)
    # print(a_list[i])

  
  ############################################################################################################
  
  
  
  def highestbars(df):
    df['maxval'] = 0
    for ii in range(len(df)):
        maxval = max(df['high'].values[ii-1], df['high'].values[ii])
        if maxval == df['high'].values[ii]:
            df['maxval'][ii] = 0
        else:
            df['maxval'][ii] = -1
    return df['maxval']
  
  
  
  ##################################################################################################################
  
  
  
  def findMaxIndxInterval(val, lst):
    if(val <= 0):
        return 0
    elif(val > len(lst)):
        return 'value is beyond the list'
    else:
        maxval = 0
        for i in range(val):
            if(lst[len(lst)-1-i] > maxval):
                maxval = lst[len(lst)-1-i]
        return lst.index(maxval)-len(lst)



print(findMaxIndxInterval(4, a_list))

