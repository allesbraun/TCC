import javalang


def count_binSearch(java_code):
    # parser = javalang.parser.Parser()
    # tree = parser.parse(java_code)
    
    # def count_recursive_calls(node, target_name, visited_methods):
    count = 0
        
        # if isinstance(node, javalang.tree.MethodInvocation) and node.member == target_name:
        #     if target_name not in visited_methods:
        #         visited_methods.add(target_name)
        #         count += 1
        
        # for child_node in node.children:
        #     count += count_recursive_calls(child_node, target_name, visited_methods)
        
    return count
    
    # target_name = "binarySearch"  # Nome do método a ser contado
    # visited_methods = set()       # Conjunto para rastrear métodos visitados
    
    # total_binary_search_calls = count_recursive_calls(tree, target_name, visited_methods)
    # return total_binary_search_calls