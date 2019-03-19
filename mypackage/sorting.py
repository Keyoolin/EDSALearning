def bubble_sort(items):
    count = 0
    for i in range(len(items)-1):
        if items[i]>items[i+1]:
            temp = items[i]
            items[i] = items[i+1]
            items[i+1]=temp
            count+=1
    if count == 0:
        return items
    else:
        return bubble_sort(items)

def merge_sort(items):
    sort = []

    if len(items)>2:
        merge1 = merge_sort(items[:round(len(items)/2)])
        merge2 = merge_sort(items[round(len(items)/2):])

        while (len(merge1) != 0) & (len(merge2)!=0):
            if merge1[0]<=merge2[0]:
                sort.append(merge1[0])
                merge1 = merge1[1:]
            else:
                sort.append(merge2[0])
                merge2 = merge2[1:]
        return (sort + list(merge1) + list(merge2))

    else:
        if len(items)==1:
            return items
        elif items[0]>items[1]:
            temp = items[0]
            items[0]=items[1]
            items[1]=temp
        return items

def quick_sort(items):

    if len(items) <= 1:
        return items

    items = list(items)
    pivot = items[-1]
    new_list = [pivot]
    count = 0

    for i in range(len(items)-1):
        if items[i]<pivot:
            new_list = [items[i]]+ new_list
            count+=1
        else:
            new_list = new_list + [items[i]]

    return quick_sort(new_list[:count])+[pivot]+quick_sort(new_list[count+1:])
    
