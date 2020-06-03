from my_class.person import Person
def test_assert():
    p = Person()
    p.x = 2
    assert p.x != None
    assert p.x ==2

class Solution:
    def selfDividingNumbers(self, left, right):
        result = [i for i in range(left, right + 1) if self.self_dividing(i) ]
        return result

    def self_dividing(self, i):
        if "0" in str(i):
            return False
        else:
            for h in str(i):
                print i ,h
                if i % int(h) != 0:
                    return False
            return True



class Solution2:
    def diStringMatch(self, S):
        mylist = [ i for i in range(0, len(S) + 1)]
        output_list = []
        if S[0] == 'I':
            output_list.append(0)
            mylist.remove(0)
        elif S[0] == 'D':
            output_list.append(len(S))
            mylist.remove(len(S))

        print S[1:]
        for i in S:

            if i =='I':
                output_list.append(mylist[len(mylist) - 1])
                mylist.remove(mylist[len(mylist) - 1])

            elif i =='D':
                output_list.append(mylist[0])
                mylist.remove(mylist[0])

            print mylist
            print output_list
        return output_list

if __name__ == '__main__':
    sol = Solution2()
    print sol.diStringMatch("IDID")