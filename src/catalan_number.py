class CatalanNumber():
    def get_catalan(self, n):

        catalan = []
        catalan.append(1)
        catalan.append(1)


        if n >= 2:

            j = 2
            while j <= n:
                sum_value = 0
                for i in range(j):
                    sum_value += catalan[i] * catalan[j - i -1]
                catalan.append(sum_value)
                j += 1
        return catalan[n]

if __name__ == '__main__':

    catalan_number = CatalanNumber()
    print(catalan_number.get_catalan(0))
    print(catalan_number.get_catalan(1))
    print(catalan_number.get_catalan(2))
    print(catalan_number.get_catalan(3))
    print(catalan_number.get_catalan(4))
    print(catalan_number.get_catalan(5))
    print(catalan_number.get_catalan(6))
    # print(catalan_number.get_catalan(7))
    # print(catalan_number.get_catalan(16))
