#code adapted from: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
def bubble_sort(alist):
     for item in range(len(alist)-1,0,-1):
          for i in range(item):
               #if item is larger than next item, s assigned to item
               if alist[i] < alist[i+1]:    
                    s = alist[i]                 
                    alist[i] = alist[i+1]
                    alist[i+1] = s
