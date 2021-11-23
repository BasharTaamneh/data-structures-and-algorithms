from hashtable.hashtable import HashTable


def tree_intersection(tree_1, tree_2):

    hashtable = HashTable()

    def hash_add(tree_1):
        if tree_1.left:
            hash_add(tree_1.left)

        hashtable.add(str(tree_1.data), tree_1.data)

        if tree_1.right:
            hash_add(tree_1.right)

    hash_add(tree_1)

    def hash_contains(tree_2, intersections):
        if tree_2:

            if hashtable.contains(str(tree_2.data)):
                intersections.append(tree_2.data)

            if tree_2.left:
                hash_contains(tree_2.left, intersections)

            if tree_2.right:
                hash_contains(tree_2.right, intersections)

            return intersections
    if hash_contains(tree_2, []) == []:
        return "There is no intersections in this trees"
    return set(hash_contains(tree_2, []))

