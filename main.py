import sys 
import os 
from subprocess import call
from CaesarCipher import CypherFile

operation_type = ''

#########################################################################
### UI FUNCTIONS ###

def new_scrn():
    call('clear')
    print('\n\n\n##########################################')
    print('\n\t/// CAESER CIPHER ///')
    if operation_type:
        print(f'\n\t ~ {operation_type.upper()} ~\n\n')
    else:
        print('\n\n')


# CHECK INPUT
def take():
    select = input('\n > ')
    if select.lower() == 'q':
        call('clear')
        sys.exit()
    else:
        return select


def create_object():
    new_scrn()
    selected_file_name = 'docs/'
    print(' > ENTER FILE TO CIPHER:')
    selected_file_name += take()
    if selected_file_name[-4:].lower() == '.txt':
        doc = selected_file_name
    else:
        doc = selected_file_name + '.txt'
    created_cc = CypherFile(doc)
    return created_cc


# MAIN SCREEN
def main_ui():
    global operation_type
    operation_type = ''
    new_scrn()
    print(' > SELECT AN OPTION:')
    print(' 1. CREATE CIPHER')
    print(' 2. BREAK CIPHER')
    print(' 3. QUICK CIPHER')
    print(' > [Q] TO QUIT AT ANY TIME')
    menu_select = take()
    if menu_select == '1':
        operation_type = 'create'
        create_cipher()
    elif menu_select == '2':
        operation_type = 'break'
        break_cipher()
    elif menu_select == '3':
        operation_type = 'quick'
    else: 
        main_ui()
 
 
 # RETURN SHIFTED DATA AND SAVE       
def summary(obj):
    new_scrn()
    print(f' > COMPLETED CONVERSION OF {obj.doc_name[5:].upper()}')
    print('\n\n > SAVE FILE? [Y/N]')
    save_confirm = take()
    if save_confirm.lower() == 'y':
        new_scrn()
        print(' > ADD NEW FILENAME FOR CIPHER')
        new_file_name = take()
        obj.new_name = new_file_name
        obj.save_new()
        confirm(obj)
    elif save_confirm.lower() == 'n':
        main_ui()
        
        
# PRINT RESULTS AND RETURN TO MAIN 
def confirm(obj):
    new_scrn()
    print(' [+] FILE SAVED!')
    print(f' [+] FILE NAME: {obj.new_name.upper()}')
    print(f' > SHIFT: {obj.shift}')
    print(f' > PREVIEW: {obj.data[0:30]}')
    print(' > PRESS [ENTER] TO RETURN TO HOME SCREEN')
    take()
    main_ui()
    
          
#######################################################
### OBJECT CREATE AND METHODS ###

def create_cipher():
    created_cc = create_object()
    new_scrn()
    print(' > ENTER POSITIONS TO SHIFT')
    entered_shift = take()
    created_cc.shift = int(entered_shift)
    created_cc.shift_alpha()
    summary(created_cc)

        
 # BREAK GIVEN CIPHER
def break_cipher():
    created_cc = create_object()
    for i in range(0,27):
        created_cc.shift = i
        created_cc.shift_alpha()
        scan = created_cc.smart_scan(created_cc)
        if len(scan) > 5:
            new_scrn()
            print(' > POSSIBLE MATCH FOUND!\n')
            print(' > ' + created_cc.data) 
            print('\n > HITS:')
            print(scan)
            print(' > SAVE? [Y/N]')
            smart_confirm = take()
            if smart_confirm.lower() == 'y':
                summary(created_cc)       
    created_cc.crack() 
    print('\n\n > ENTER DESIRED SHIFT: ')
    shift = int(take())
    created_cc.shift = -shift
    created_cc.shift_alpha()
    summary(created_cc)  



if __name__ == '__main__':
    main_ui()     
    