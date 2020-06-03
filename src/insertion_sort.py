class Sorting:
    def insertion_sort(self, l):

        #l is  [int]
        for i in range(len(l) - 1):
            j = i
            while l[j] < l[i+1] and j < i+1 :
                j += 1

            ## the insertion point is found
            index = j
            temp = l[i+1]
            while j < i+1:
                l[j+1] = l[j]
                j +=1
            l[index] = temp
        return l

if __name__ == '__main__':
    sorting = Sorting()
    l = sorting.insertion_sort([3,1,2])
    print (l)



