from hashtable.hashtable import HashTable

def hashmap_left_join(table_1, table_2):

    dict_ = []
    try:
        for  child in table_1._HashTable__buckets:
            if child:

                foreignkey = child.head.value[0]

                value = table_1.get(foreignkey)

                foreignvalue = table_2.get(foreignkey)

                updatedvalue = [value, foreignvalue]

                dict_.append({foreignkey: updatedvalue})
    except:
        return "please provide a hashmap opject as arguments"

    return dict_





#////////////////////////////////////////////////////////////////////////
# synonym_hashmap_2 = HashTable()
# synonym_hashmap_2.add('fond', 'enamored')
# synonym_hashmap_2.add('wrath', 'anger')
# synonym_hashmap_2.add('diligent', 'employed')
# synonym_hashmap_2.add('outfit', 'garb')
# synonym_hashmap_2.add('guide', 'usher')
# //////////////////////////////////////////////
# antonym_hashmap_2 = HashTable()
# antonym_hashmap_2.add('fond', 'averse')
# antonym_hashmap_2.add('wrath', 'delight')
# antonym_hashmap_2.add('diligent', 'idle')
# antonym_hashmap_2.add('guide', 'follow')
# antonym_hashmap_2.add('flow', 'jam')
# x = hashmap_left_join(antonym_hashmap_2, synonym_hashmap_2)
# print(x)


# key = "diligent"
# for c in x:
#     if c.get(key):
#         print(c.get(key))

