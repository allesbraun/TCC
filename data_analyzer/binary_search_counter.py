import javalang


def count_binSearch(content):
    tree = javalang.parse.parse(content)
    count = 0
    for _, node in tree.filter(javalang.tree.MethodInvocation):
        if node.member == 'binarySearch':
            count += 1
    return count