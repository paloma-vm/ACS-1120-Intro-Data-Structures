import random
import sys
# tuple, first try
# tuple_of_words = ("how",
#                  "now",
#                  "brown",
#                  "cow")

# second try
# list_of_words = ["how", "now", "brown", "cow"]

# third try
# list_of_words = []
# def get_words():
#     list_of_words = sys.argv[1:]
#     print("***************")
#     print(list_of_words)
#     return list_of_words
   
    # .split(" ")

list_of_words = sys.argv[1:]
# ^ got help from https://realpython.com/python-command-line-arguments/
# print("***************")
# print(list_of_words)

    
def rearrange_list_of_words():
    # print(list_of_words)
    random.shuffle(list_of_words)
    # print("-------------------------")
    # print(list_of_words)
    for word in list_of_words:
        print(word, end=" ")
    print("\n")#added this to get rid of the % at the end of the line


if __name__ == '__main__':
    rearrange_list_of_words()
    
    
    