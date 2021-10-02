from main import Tree


def test_insert_int():
    values = list(range(5))
    tree = Tree()

    for v in values:
        tree.insert(v)

    assert tree.to_list() == values


def test_insert_str():
    values = list(map(str, list(range(5))))
    tree = Tree()

    for v in values:
        tree.insert(v)

    assert tree.to_list() == values


def test_revert_int():
    values = list(range(5))
    tree = Tree()

    for v in values:
        tree.insert(v)

    values.reverse()
    assert tree.reverse().to_list() == values


def test_revert_str():
    values = list(map(str, list(range(5))))
    tree = Tree()

    for v in values:
        tree.insert(v)

    values.reverse()
    assert tree.reverse().to_list() == values
