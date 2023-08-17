import javalang
from javalang import tree


class Counter:
    def count_statements(self, content):
        count = 0
        tokens = javalang.tokenizer.tokenize(content)
        parser = javalang.parser.Parser(tokens)
        parsed_tree = parser.parse()

        # for _, node in parsed_tree:
        #     count += node.

        return count

    