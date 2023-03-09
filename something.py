# s snakes
# r x c matrix
#l : length of snake
# come out of the wormhole (col, row)
import random

with open('input.txt') as f:
    lines = f.readlines()
    
first_line = lines[0].split()
second_line = lines[1].split()
restLines = lines[2:]

cols, rows, snakesNumber = map(int, first_line)
l0, l1, l2, l3, l4 = map(int, second_line)
wormhole_exits = [[2, 7], [4,3] ,[4,3]]

# Otan tha mpainei sto if tha tou les
# ama einai wormhole kane pop to prwto stoixeio tou global list kai parto san cur_pos

snake_data = [[l0,[0,0],['R','R','D','R','R']], [l1,[1, 6],[ 'L', 'U', 'L', 'D', 'L', 'U']], [l2, [1,1], [ 'R', 'R', 'R', 'R']], [l3,[1,7],[ 'D', 'L']], [l4,[0,9], ['U', 'L']]]

def exists_in_list(lst, element):
    """Checks if an element exists in a list."""
    return element in lst      
                
def test_function(matrix_list, moves_list, initial_pos):
    flag = True
    relevance_list = list()
    position_list = list()
    snake_move_list = list()
    

    cur_pos = initial_pos
    position_list.append(cur_pos)
    relevance_list.append(matrix_list[cur_pos[0]][cur_pos[1]])
    matrix_list[cur_pos[0]][cur_pos[1]] = 'X'     
    while flag:
        for move in moves_list:
            if move == 'R':
                cur_pos = [cur_pos[0], cur_pos[1] + 1]
                if exists_in_list(position_list, cur_pos) == True:
                    break
                if cur_pos[1] > cols-1:
                    cur_pos[1] = 0
                if isinstance(matrix_list[cur_pos[0]][cur_pos[1]], int):
                    relevance_list.append(matrix_list[cur_pos[0]][cur_pos[1]])  
                    snake_move_list.append('R')
                else:
                    if matrix_list[cur_pos[0]][cur_pos[1]] == 'X':
                        print('A snake already passed from here') 
                        return
                       
                    cur_pos = wormhole_exits.pop(0)
                    snake_move_list.append(str(cur_pos[1]))
                    snake_move_list.append(str(cur_pos[0]))
                matrix_list[cur_pos[0]][cur_pos[1]] = 'X'     
            elif move == 'L':
                cur_pos = [cur_pos[0], cur_pos[1] - 1]
                if exists_in_list(position_list, cur_pos) == True:
                    break
                if cur_pos[1] < 0:
                    cur_pos[1] = cols-1
                if isinstance(matrix_list[cur_pos[0]][cur_pos[1]], int):
                    relevance_list.append(matrix_list[cur_pos[0]][cur_pos[1]])
                    snake_move_list.append('L')  
                else:
                    if matrix_list[cur_pos[0]][cur_pos[1]] == 'X':
                        print('A snake already passed from here') 
                        return           
                    cur_pos = wormhole_exits.pop(0)
                    snake_move_list.append(str(cur_pos[1]))
                    snake_move_list.append(str(cur_pos[0]))
                matrix_list[cur_pos[0]][cur_pos[1]] = 'X'   
            elif move == 'U':
                cur_pos = [cur_pos[0] - 1, cur_pos[1]]
                if exists_in_list(position_list, cur_pos) == True:
                    break
                if cur_pos[0] < 0:
                    cur_pos[0] = rows-1
                if isinstance(matrix_list[cur_pos[0]][cur_pos[1]], int):
                    relevance_list.append(matrix_list[cur_pos[0]][cur_pos[1]]) 
                    snake_move_list.append('U')
                else:
                    if matrix_list[cur_pos[0]][cur_pos[1]] == 'X':
                        print('A snake already passed from here') 
                        return         
                    cur_pos = wormhole_exits.pop(0)
                    snake_move_list.append(str(cur_pos[1]))
                    snake_move_list.append(str(cur_pos[0]))
                matrix_list[cur_pos[0]][cur_pos[1]] = 'X'  
            elif move == 'D':
                cur_pos = [cur_pos[0] + 1, cur_pos[1]]
                if exists_in_list(position_list, cur_pos) == True:
                    break
                if cur_pos[0] > rows-1:
                    cur_pos[0] = 0
                if isinstance(matrix_list[cur_pos[0]][cur_pos[1]], int):
                    relevance_list.append(matrix_list[cur_pos[0]][cur_pos[1]])
                    snake_move_list.append('D')  
                else:
                    if matrix_list[cur_pos[0]][cur_pos[1]] == 'X':
                        print('A snake already passed from here') 
                        return 
                    cur_pos = wormhole_exits.pop(0)
                    snake_move_list.append(str(cur_pos[1]))
                    snake_move_list.append(str(cur_pos[0]))
                matrix_list[cur_pos[0]][cur_pos[1]] = 'X' 
        else:
            for list_items in [[2, 7], [4,3] ,[4,3]]:
                matrix_list[list_items[0]][list_items[1]] = '*'
            flag = False
        exit_string = " ".join(snake_move_list)
        exit_string = str(initial_pos[1]) + ' ' + str(initial_pos[0]) + ' ' + exit_string
        return exit_string
    # print(relevance_list)



######## Main ########

for i in range(0, len(restLines)):
    restLines[i] = restLines[i].split()
    
for i in range(len(restLines)):
    for j in range(len(restLines[i])):
        if restLines[i][j] != '*':  # Skip the '*' character
            restLines[i][j] = int(restLines[i][j])

output_list = list()

for snake in snake_data:
    # call function that moves the entire first snake from start to the end
    output_list.append(test_function(restLines, snake[2], snake[1]))

print(output_list)

with open('output.txt', 'w') as f:
    for i in range(0, len(output_list)):
         f.write(output_list[i] + '\n')