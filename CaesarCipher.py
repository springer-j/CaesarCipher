class CypherFile:
    def __init__(self,doc_name):
        self.doc_name = doc_name
        self.new_name = None
        self.shift = None
        self.data = None
   
    def save_new(self):
        # APPEND .TXT IF NOT PRESENT
        if self.new_name[-4:].lower() != '.txt':
            self.new_name += '.txt'
            
        doc = open(f'docs/{self.new_name}','w')
        doc.write(self.data)
        doc.close()    
    # SHIFT ALL DATA IN TEXT FILE AND RETURN SINGLE STRING
    def shift_alpha(self):
        file = open(self.doc_name, 'r')
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
        'o','p','q','r','s','t','u','v','w','x','y','z']
        converted = ''
        for line in file:
            for char in line:
                if char.lower() in alpha:
                    # FIND ORIGINAL INDEX POSITION
                    index = alpha.index(char.lower())
                    # ADD DESIRED SHIFT TO INDEX POSITION
                    desired = int(index) + int(self.shift)
                    if desired <= 25:
                        converted += alpha[desired].upper()
                    # 'ROLLOVER' LIST IF INDEX EXCEEDS LIST RANGE
                    elif desired >= 26:
                        desired = desired - 26
                        converted += alpha[desired].upper()
        file.close()
        self.data = converted
            
    def crack(self):
        file = open(self.doc_name,'r')
        all_samples = []
        for i in range(26,0,-1):
            self.shift = i
            self.shift_alpha()
            sample = {'shift':self.shift,'sample_data':self.data[0:30]}
            all_samples.append(sample)
        print('------------------------------------\n  -SHIFT-\t\t-SAMPLE-\n------------------------------------')
        for i in range(1,26):
            print(f"  #{i} \t {all_samples[i]['sample_data']} ")
            
    def strip_words(self):   
        file = open('guess_words.txt','r')

        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
        'o','p','q','r','s','t','u','v','w','x','y','z']

        words = []
        grabbed_word = ''

        for line in file:
            for char in line:
                if char.lower() in alpha:
                    grabbed_word += char.lower()
                else:
                    if grabbed_word:
                        words.append(grabbed_word)
                        grabbed_word = ''

        print(words)
        file.close()
        new_file = open('top_words.txt','a+')
        for word in words:
            new_file.write(word + '\n')

    def smart_scan(self, obj):
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
            
        