from rest_framework.response import Response

from data_analyzer import *
from data_classificators.autogluon_classificator import autogluon_classifier


def data_response(content, file):
    response_data = {
        'num_if': count_ifs(content), # Number of if statements in the code #OK
        'num_else': count_elses(content), # Number of else statements in the code #OK
        'num_switch': count_switches(content), #Number of switch statements #OK
        'num_loop': count_loops(content), # Number of loops, including for and while statements #OK
        'num_break': count_breaks(content), # Number of break statements #OK
        'num_priority': count_priority(content), # Number of priority queues instantiated #OK
        'num_binSearch': count_binSearch(content), # Number of calls for a binary search #
        'num_minMax': count_minMax(content), # Number data of calls for min() or max() functions #OK
        'num_sort': count_sorts(content), # Number of calls for the sort() function #OK
        'num_hash_map': count_hash_maps(content), # Number of hash maps instantiated #OK
        'num_hash_set': count_hash_sets(content), # Number of hash sets instantiated #OK
        'num_recursive': count_recursive(content), # Number of recursive calls for a given function #OK
        'num_nested_loop': count_nested_loops(content), # Depth of nested loops no código #OK
        'num_vari': count_variables(content), # Number of variables declared #
        'num_method': count_methods(content), # Number of methods declared #OK
        'num_state': count_statements(content), # Number of statements #OK
        'filename': file.name, #OK
    }
    
    # Converter o dicionário para lista de listas
    headers = list(response_data.keys())
    values = list(response_data.values())

    # Criar a lista de listas para o arquivo CSV
    csv_data = [headers, values]
    #complexity = autogluon_classifier(csv_data)
    # merged_database = create_merged_database()
    return autogluon_classifier(csv_data)
 
    #return csv_data
    # response = create_merged_database().to_list()
    # return Response(response)