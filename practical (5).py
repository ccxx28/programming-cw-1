'''
2138473
CS917 Algorithm Assignment
Question 9
'''
import itertools
import collections
#import pdb

def morseDecode(inputStringList):
    """
    This method should take a list of strings as input. Each string is equivalent to one letter
    (i.e. one morse code string). The entire list of strings represents a word.

    This method should convert the strings from morse code into english, and return the word as a string.

    """
    # Please complete this method to perform the above described function
    
    morse_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '--.': 'G', '..-.': 'F', '....': 'H'
        , '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P'
        , '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y'
        , '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6'
        , '--...': '7', '---..': '8', '----.': '9', '-----': '0'}
    
    if inputStringList == []:
        return None
    
    word_to_decode = ""
    for i in inputStringList:
        word_to_decode += morse_dict[i]
        
    return word_to_decode

    pass

def possibleDecode(inList):
    
    element_list = ['.','-']
    replacement = [''.join(i) for i in (itertools.product(element_list, repeat=len(inList)))]
    
    possible_list = []
    for combination in replacement:
        possible_code = []
        i = 0
        for string in inList:
            string = combination[i] + string[1:]
            possible_code.append(string)
            i += 1
        possible_list.append(possible_code)
    
    possible_decoded = []
    for s in possible_list:
        possible_decoded.append(morseDecode(s))
    
    return possible_decoded
    
    pass

def morsePartialDecode(inputStringList):
    """
    This method should take a list of strings as input. Each string is equivalent to one letter
    (i.e. one morse code string). The entire list of strings represents a word.

    However, the first character of every morse code string is unknown (represented by an 'x' (lowercase))
    For example, if the word was originally TEST, then the morse code list string would normally be:
    ['-','.','...','-']

    However, with the first characters missing, I would receive:
    ['x','x','x..','x']

    With the x unknown, this word could be TEST, but it could also be EESE or ETSE or ETST or EEDT or other permutations.

    We define a valid words as one that exists within the dictionary file provided on the website, dictionary.txt
    When using this file, please always use the location './dictionary.txt' and place it in the same directory as
    the python script.

    This function should find and return a list of strings of all possible VALID words.
    """

    if inputStringList == []:
        return None
    
    words = possibleDecode(inputStringList)
    
    dictionaryFileLoc = './dictionary.txt'
    with open(dictionaryFileLoc) as f:
        valid_words_dict = {line.rstrip().upper() for line in f} 
    
    valid_decode = []
    for i in words:
        if i in valid_words_dict:
            valid_decode.append(i)
    
    return valid_decode
    # Please complete this method to perform the above described function
    pass

class Maze:
    def __init__(self):
        """
        Constructor - You may modify this, but please do not add any extra parameters
        """
        self.width = 0
        self.height = 0
        self.grid = {}
        pass

    def addCoordinate(self,x,y,blockType):
        """
        Add information about a coordinate on the maze grid
        x is the x coordinate
        y is the y coordinate
        blockType should be 0 (for an open space) of 1 (for a wall)
        """
        if x > self.width:
            self.width = x + 1

        if y > self.height:
            self.height = y + 1

        self.grid[(x, y)] = blockType        

        # Please complete this method to perform the above described function
        pass

    def printMaze(self):
        """
        Print out an ascii representation of the maze.
        A * indicates a wall and a empty space indicates an open space in the maze
        """
        maze_grid = ''
        for y in range(0, self.height):
            for x in range(0, self.width):
                if (x,y) not in self.grid or self.grid[(x,y)] == 1:
                    maze_grid += '*'
                else:
                    maze_grid += ' '
            maze_grid += '\n'
            
        print(maze_grid)       
        # Please complete this method to perform the above described function
        pass     
        
    
    def findRoute(self,x1,y1,x2,y2):
        """
        This method should find a route, traversing open spaces, from the coordinates (x1,y1) to (x2,y2)
        It should return the list of traversed coordinates followed along this route as a list of tuples (x,y),
        in the order in which the coordinates must be followed
        If no route is found, return an empty list
        """
        upcoming_nodes = collections.deque([[(x1,y1)]])
        visited_nodes = set([(x1,y1)])
        while upcoming_nodes:
            route = upcoming_nodes.popleft()
            x,y = route[-1]
            if x == x2 and y == y2:
                return route

            for x,y in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):  
                if (x,y) in self.grid.keys() and (x, y) not in visited_nodes :
                    if 0 <= y <= self.height and 0 <= x <= self.width and self.grid[(x,y)] == 0:
                        upcoming_nodes.append(route + [(x, y)])
                        visited_nodes.add((x, y))
                    
        if route is not None:
            return route
        else:
            return []
        
        pass

def morseCodeTest():
    """
    This test program passes the morse code as a list of strings for the word
    HELLO to the decode method. It should receive a string "HELLO" in return.
    This is provided as a simple test example, but by no means covers all possibilities, and you should
    fulfill the methods as described in their comments.
    """

    hello = ['....','.','.-..','.-..','---']
    print(morseDecode(hello))

def partialMorseCodeTest():

    """
    This test program passes the partial morse code as a list of strings 
    to the morsePartialDecode method. This is provided as a simple test example, but by
    no means covers all possibilities, and you should fulfill the methods as described in their comments.
    """

    # This is a partial representation of the word TEST, amongst other possible combinations
    test = ['x','x','x..','x']
    print(morsePartialDecode(test))

    # This is a partial representation of the word DANCE, amongst other possible combinations
    dance = ['x..','x-','x.','x.-.','x']
    print(morsePartialDecode(dance))

def mazeTest():
    """
    This sets the open space coordinates for the example
    maze in the assignment.
    The remainder of coordinates within the max bounds of these specified coordinates
    are assumed to be walls
    """
    myMaze = Maze()
    myMaze.addCoordinate(1,0,0) # Start index
    myMaze.addCoordinate(1,1,0)
    myMaze.addCoordinate(1,3,0)
    myMaze.addCoordinate(1,4,0)
    myMaze.addCoordinate(1,5,0)
    myMaze.addCoordinate(1,6,0)
    myMaze.addCoordinate(1,7,0)

    myMaze.addCoordinate(2,1,0)
    myMaze.addCoordinate(2,2,0)
    myMaze.addCoordinate(2,3,0)
    myMaze.addCoordinate(2,6,0)

    myMaze.addCoordinate(3,1,0)
    myMaze.addCoordinate(3,3,0)
    myMaze.addCoordinate(3,4,0)
    myMaze.addCoordinate(3,5,0)
    myMaze.addCoordinate(3,7,0)
    myMaze.addCoordinate(3,8,0) # End index

    myMaze.addCoordinate(4,1,0)
    myMaze.addCoordinate(4,5,0)
    myMaze.addCoordinate(4,7,0)

    myMaze.addCoordinate(5,1,0)
    myMaze.addCoordinate(5,2,0)
    myMaze.addCoordinate(5,3,0)
    myMaze.addCoordinate(5,5,0)
    myMaze.addCoordinate(5,6,0)
    myMaze.addCoordinate(5,7,0)

    myMaze.addCoordinate(6,3,0)
    myMaze.addCoordinate(6,5,0)
    myMaze.addCoordinate(6,7,0)

    myMaze.addCoordinate(7,1,0)
    myMaze.addCoordinate(7,2,0)
    myMaze.addCoordinate(7,3,0)
    myMaze.addCoordinate(7,5,0)
    myMaze.addCoordinate(7,7,0)

    # TODO: Test your findRoute method
    
    myMaze.printMaze()
    
    print(myMaze.findRoute(1,0,3,8))


def main():
    morseCodeTest()
    partialMorseCodeTest()
    mazeTest()

if __name__ == "__main__":
    main()