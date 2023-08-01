import javalang


def count_binSearch(content):
    tokens = list(javalang.tokenizer.tokenize(content))
    count = 0

    for i in range(len(tokens)):
        if isinstance(tokens[i], javalang.tree.MethodInvocation):
            if tokens[i].member == 'binarySearch':
                count += 1

    return count