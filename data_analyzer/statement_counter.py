import javalang


def count_statements(content):
    tree = javalang.parse.parse(content)
    count = 0

    for _, node in tree:
        if isinstance(node, javalang.tree.Statement):
            count += 1

    return count

