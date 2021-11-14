class KTree:
    def __init__(self, n, lst_=[]):
        self._tree = lst_
        self._n = n

    def child_pointers(self, i):
        #returns list of the indices of the children of i
        tree = self._tree
        n = self._n
        result = []
        for k in range(n*i+1, n*i+n+1):
            if k < len(tree):
                result.append(k)
        return result

    def fizz_buzz_tree(self):
        result = []
        stack = []
        stack.append(0)
        k = 0
        while k < len(stack):
            value = self._tree[stack[k]]
            if value % 3 == 0 and value % 5 != 0:
                value = "Fizz"
            elif value % 5 == 0 and value % 3 != 0:
                value = "Buzz"
            elif value % 15 == 0:
                value = "FizzBuzz"
            elif value % 15 != 0:
                value = str(value)
            result.append(value)
            for index in self.child_pointers(k):
                stack.append(index)
            k += 1
        stack = []
        return result


if __name__ == "__main__":
    list_ = []
    for _ in range(0, 16):
        list_.append(_)
        ktree = KTree(4, list_)
    print(ktree.fizz_buzz_tree())
