class OneEditDistance:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


        if len(s) == len(t):
            if len(s) == 0:
                return False
            i = 0
            while   i <= len(s) - 1 and s[i] == t[i]:
                i = i + 1
            if i != len(s) - 1:
                rem_s = s[i+1 : len(s)]
                rem_t = t[i+1 : len(t)]
                if rem_s == rem_t and len(rem_s) != 0 :
                    return True
                else:
                    return False
            else:
                return True
        elif len(s) > len(t):
            i = 0
            while  i <= len(t) - 1 and s[i] == t[i]:
                i = i + 1
            if i != len(t) - 1:
                rem_s = s[i+1 : len(s)]
                rem_t = t[i:len(t)]
                if rem_s == rem_t:
                    return True
                else:
                    return False
            elif t[len(t) - 1] == s[len(t)] and len(t) != 0:
                return True
            elif len(t) == 0 and len(s) == 1:
                return True
            else:
                return False
        elif len(t) > len(s):
            return self.isOneEditDistance(t,s)
        else:
            return False




if __name__ == '__main__':
    one_edit_distance = OneEditDistance()
    print(one_edit_distance.isOneEditDistance("c", "c"))
