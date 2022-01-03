from hashtable.hashtable import HashTable


def test_hash_table():
    # Arrange
    hashtable = HashTable()
    excepted = 2048
    #Act
    actual = hashtable._HashTable__size
    #Assert
    assert actual == excepted


def test_hash_table_hash():
    # Arrange
    hashtable = HashTable()
    excepted = 388
    #Act
    actual = hashtable._HashTable__hash('a')
    #Assert
    assert actual == excepted


def test_hash_table_hash_range():
    # Arrange
    hashtable = HashTable()
    excepted = 1656
    #Act
    actual = hashtable._HashTable__hash('bash')
    #Assert
    assert actual == excepted


def test_hash_table_hash_collision():
    # Arrange
    hashtable = HashTable()
    excepted_1 = 524
    excepted_2 = 540
    #Act
    actual_1 = hashtable._HashTable__hash('AB')
    actual_2 = hashtable._HashTable__hash('CD')
    #Assert
    assert actual_1 == excepted_1
    assert actual_2 == excepted_2

def test_hash_table_add_T():
    # Arrange
    hashtable = HashTable()
    excepted = True
    #Act
    hashtable.add('a', 1)
    actual = hashtable.contains('a')
    #Assert
    assert actual == excepted


def test_hash_table_add_F():
    # Arrange
    hashtable = HashTable()
    excepted = False
    #Act
    hashtable.add('a', 1)
    actual = hashtable.contains('b')
    #Assert
    assert actual == excepted


def test_hash_table_get():
    # Arrange
    hashtable = HashTable()
    excepted = 2
    hashtable.add('b', 2)
    #Act
    actual = hashtable.get('b')
    #Assert
    assert actual == excepted


def test_hash_table_get_None():
    # Arrange
    hashtable = HashTable()
    excepted = None
    hashtable.add('b', 2)
    #Act
    actual = hashtable.get('c')
    #Assert
    assert actual == excepted


def test_hash_table_add_collision():
    # Arrange
    hashtable = HashTable()
    excepted_1 = True
    excepted_2 = True
    hashtable.add('ABc', 1)
    hashtable.add('DEf', 2)
    #Act
    actual_1 = hashtable.contains('ABc')
    actual_2 = hashtable.contains('DEf')
    #Assert
    assert actual_1 == excepted_1
    assert actual_2 == excepted_2


def test_hash_table_get_collision():
    # Arrange
    hashtable = HashTable()
    excepted_1 = 1
    excepted_2 = 2
    hashtable.add('123', 1)
    hashtable.add('456', 2)
    #Act
    actual_1 = hashtable.get('123')
    actual_2 = hashtable.get('456')
    #Assert
    assert actual_1 == excepted_1
    assert actual_2 == excepted_2



