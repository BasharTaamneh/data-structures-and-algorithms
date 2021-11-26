from hashmap_left_join.hashmap_left_join import hashmap_left_join
from hashtable.hashtable import HashTable


def test_hashmap_left_join_1():
    # Arrange
    synonym_hashmap_ = HashTable()
    synonym_hashmap_.add('fond', 'enamored')
    synonym_hashmap_.add('wrath', 'anger')
    synonym_hashmap_.add('diligent', 'employed')
    synonym_hashmap_.add('outfit', 'garb')
    synonym_hashmap_.add('guide', 'usher')
    # //////////////////////////////////////////////
    antonym_hashmap_ = HashTable()
    antonym_hashmap_.add('fond', 'averse')
    antonym_hashmap_.add('wrath', 'delight')
    antonym_hashmap_.add('diligent', 'idle')
    antonym_hashmap_.add('guide', 'follow')
    antonym_hashmap_.add('flow', 'jam')

    expected = [{'guide': ['usher', 'follow']}, {'wrath': ['anger', 'delight']}, {'outfit': [
        'garb', None]}, {'diligent': ['employed', 'idle']}, {'fond': ['enamored', 'averse']}]
    # Act
    actual = hashmap_left_join(synonym_hashmap_, antonym_hashmap_)
    # Assert
    assert actual == expected


def test_hashmap_left_join_2():
    # Arrange
    synonym_hashmap_ = HashTable()
    synonym_hashmap_.add('fond', 'enamored')
    synonym_hashmap_.add('wrath', 'anger')
    synonym_hashmap_.add('diligent', 'employed')
    synonym_hashmap_.add('outfit', 'garb')
    synonym_hashmap_.add('guide', 'usher')
    # //////////////////////////////////////////////
    antonym_hashmap_ = HashTable()
    antonym_hashmap_.add('fond', 'averse')
    antonym_hashmap_.add('wrath', 'delight')
    antonym_hashmap_.add('diligent', 'idle')
    antonym_hashmap_.add('guide', 'follow')
    antonym_hashmap_.add('flow', 'jam')

    expected = [{'guide': ['follow', 'usher']}, {'wrath': ['delight', 'anger']}, {
        'diligent': ['idle', 'employed']}, {'fond': ['averse', 'enamored']}, {'flow': ['jam', None]}]
    # Act
    actual = hashmap_left_join(antonym_hashmap_, synonym_hashmap_)
    # Assert
    assert actual == expected


def test_hashmap_left_join_with_none_hashabl_input_1():
    # Arrange
    expected = "please provide a hashmap opject as arguments"
    # Act
    actual = hashmap_left_join(1, [1, 2])
    # Assert
    assert actual == expected


def test_hashmap_left_join_with_none_hashabl_input_2():
    # Arrange
    expected = "please provide a hashmap opject as arguments"
    # Act
    actual = hashmap_left_join("hjgjj", [1, 2])
    # Assert
    assert actual == expected
