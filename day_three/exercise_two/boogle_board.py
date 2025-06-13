import string
import random

class BoggleBoard():

    def __init__(self):
        self.alphabet = list(string.ascii_uppercase)
        self.bare_board = print('____\n' * 4)
        self.dice_keys = list(range(1,17))
        self.dice_dic = {
            1: "AAEEGN",
            2: "ELRTTY",
            3: "AOOTTW",
            4: "ABBJOO",
            5: "EHRTVW",
            6: "CIMOTU",
            7: "DISTTY",
            8: "EIOSST",
            9: "DELRVY",
            10: "ACHOPS",
            11: "HIMNQU",
            12: "EEINSU",
            13: "EEGHNW",
            14: "AFFKPS",
            15: "HLNNRZ",
            16: "DEILRX"
        }
    
    def shake(self):
        board_list = []
        die = self.dice_keys.copy()
        random.shuffle(die)
        string = ""
        for x in range(1,17):
            i = random.randint(0, 5)
            char = self.dice_dic[die[x - 1]][i]
            if char == 'Q':
                string += 'Qu'
            else:
                string += char
                
            if x % 4 == 0:
                board_list.append(string)
                string = ""
        return "\n".join(board_list)
        

            
bb = BoggleBoard()

print(bb.shake())

def check_for_word(word, board):
    row_length = len(board)
    column_length = len(board[0])
    directions = [(0,1), (1,1), (-1,1), (1,0), (-1,0), (-1,-1), (1,-1), (0,-1)]

    def check_if_index_within_2d_list(row_index, column_index):
        return 0 <= row_index < row_length and 0 <= column_index < column_length 

    count = 0
    if word[count] in board:
        idx1, idx2 = board.index(word[count])
        count += 1
        for d in directions:
            if board[(idx1 + d[0]), (idx2 + d[1])] == word[count]:
                idx1, idx2 = board[d[0], d[1]]
                count += 1
                if count + 1 == len(word):
                    return True
    return False


