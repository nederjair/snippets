def get_longest(data, colCount):
    longest_list = []
    for colNum in range(colCount):
        col = [row[colNum] for row in data]
        longest = 0
        for elem in col:
            if len(str(elem)) > longest:
                longest = len(str(elem))
        longest_list.append(longest)
    return longest_list

def print_table(data):
    colCount = len(data[0])
    longest_list = get_longest(data, colCount)
    row_length = sum(longest_list) + colCount
    #print(row_length*'-')
    for row in data:
        str_to_print = ''
        colNum = 0
        for col in row:
            spaces = (longest_list[colNum] - len(str(col)))*' ' 
            str_to_print += str(col) + spaces + '|' + ' '
            colNum += 1
        print(row_length*'-')
        print(str_to_print)
    print(row_length*'-')
