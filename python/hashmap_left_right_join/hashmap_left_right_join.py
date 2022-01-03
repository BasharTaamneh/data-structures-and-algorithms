
def hashmap_left_right_join(left_hashmap: dict, right_hashmap: dict, left_join=False, right_join=False):
    """
    hashmap_left_right_join --> returns the joined or updated data from the left or right hashmap, depending on the action key if ( right_join OR left_join ) is True, even if there are no matches in the right table from the left table will return the original left table  updated with (None) values and versa vise.

    If the left_join action key is True it will return all data from the left_hashmap table, even if there are no matches in the right_hashmap table. If it has matches on the right_hashmap table, it'll return the values along with the corresponding data from the left_hashmap, if not, they'll be replaced by (None) value and versa vise.

    --------------------------------

    Arguments:
    ---
        left_hashmap: --> HashTable or dict
        right_hashmap: --> HashTable or dict
        left_join: --> default=False
        right_join: --> default=False

    --------------------------------

    Return: List of dicts containing the joined values --> [{"key", [values] }, {"key", [values] }].
    """
    dict_ = []

    if left_join:
        try:
            for key in left_hashmap.get_keys():

                if right_hashmap.contains(key):
                    value = left_hashmap.get(key)

                    foreignvalue = right_hashmap.get(key)

                    updatedvalue = [value, foreignvalue]

                    dict_.append({key: updatedvalue})
                else:
                    value = left_hashmap.get(key)

                    dict_.append({key: [value, None]})

        except:
            return "please provide a hashmap opject as arguments"
        return dict_

    if right_join:
        try:
            for key in right_hashmap.get_keys():

                if left_hashmap.contains(key):
                    value = right_hashmap.get(key)

                    foreignvalue = left_hashmap.get(key)

                    updatedvalue = [value, foreignvalue]

                    dict_.append({key: updatedvalue})
                else:
                    value = right_hashmap.get(key)

                    dict_.append({key: [value, None]})

        except:
            return "please provide a hashmap opject as arguments"
        return dict_


# if __name__ == "__main__":
#     #////////////////////////////////////////////////////////////////////////
#     from hashtable.hashtable import HashTable
#     #////////////////////////////////////////////////////////////////////////
#     synonym_hashmap_ = HashTable()
#     synonym_hashmap_.add('fond', 'enamored')
#     synonym_hashmap_.add('wrath', 'anger')
#     synonym_hashmap_.add('diligent', 'employed')
#     synonym_hashmap_.add('outfit', 'garb')
#     synonym_hashmap_.add('guide', 'usher')
#     # //////////////////////////////////////////////
#     antonym_hashmap_ = HashTable()
#     antonym_hashmap_.add('fond', 'averse')
#     antonym_hashmap_.add('wrath', 'delight')
#     antonym_hashmap_.add('diligent', 'idle')
#     antonym_hashmap_.add('guide', 'follow')
#     antonym_hashmap_.add('flow', 'jam')
#     #////////////////////////////////////////////////////////////////////////
#     x = hashmap_left_right_join(synonym_hashmap_, antonym_hashmap_, right_join=True)
#     print(x)


    # key = "outfit"
    # for c in x:
    #     if c.get(key):
    #         print(c.get(key)[0])




