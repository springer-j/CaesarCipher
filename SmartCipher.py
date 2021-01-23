# alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
# 'o','p','q','r','s','t','u','v','w','x','y','z']
# f = open('top_words.txt','r')

# list = []
# hits = []
# word = ''


# for line in f:
#     for char in line:
#         if char in alpha:
#             word += char 
#         else:
#             if word:
#                 list.append(word)
#                 word = ''



# def scan(test_word):
#     known = open('docs/puffpuff.txt','r' )

#     constructed = ''
#     for line in known:
#         for char in line:
#             index = len(constructed)
#             if char.upper() == test_word[index]:
#                 constructed += char.upper()
#                 if constructed == test_word:
#                     hits.append(constructed)
#                     constructed = ''
#             else:
#                 constructed = ''    
                    
# for word in list:
#     scan(word.upper())
# print(hits)
            
                
def smart_scan(obj):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u','v','w','x','y','z']
    f = open('top_words.txt','r')
    # LISTS OF POPULAR WORDS
    pop_word = ''
    pop_list = []
    # MATCHING WORDS
    hits = []
    possible = False
    # GATHER LIST ITEM OF POPULAR WIRDS
    for line in f:
        for char in line:
            if char in alpha:
                pop_word += char 
            else:
                if pop_word:
                    pop_list.append(pop_word)
                    pop_word = ''
    # GRAB EACH WORD FROM POPULARS
    for test_word in pop_list:
        constructed = ''
        # COMPARE EACH SECTION OF TEXT TO TEST WORD
        for char in obj.data:
            index = len(constructed)
            if char.upper() == test_word[index].upper():
                # IF LETTER AND INDEX MATCHES, ADD CHAR TO GRABBED STRING
                constructed += char.upper()
                # IF COMPLETED WORD, ADD TO HITS LIST AND RESET
                if constructed.upper() == test_word.upper():
                    hits.append(constructed)
                    constructed = ''
            # IF CHARACTERS DON'T MATCH, RESET STRING
            else:
                constructed = ''  
    #RETURN TRUE IF MORE THAN THREE WORDS DETECTED
 
    return hits

