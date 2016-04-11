def start():
    game_won = False;
    print ( "-----------WELCOME TO HANGSMAN-------------" )
    print  " \nTO EXIT ANYTIME FROM GAME ENTER 0"
    target_list = ['S', 'A', 'L', 'O', 'N', 'I']
    used_letter_list = list() # Initially this will be empty
    matched_letter_list = get_initial_list(target_list)
    len_of_target_list = len(target_list)
    
    for count in range(len_of_target_list*3/2, 0, -1):
        print "YOU HAVE ", count, "CHANCES TO GUESS THE RIGHT WORD "
        used_letter = raw_input("\nENTER THE ALPHABET: ")
        if used_letter == '0':
            return
        used_letter = get_valid_letter(used_letter) 
        used_letter_list.append(used_letter.upper())
        print "USED ALPHABETS", used_letter_list
        
        position = get_letter_position(used_letter, target_list)
        if(position > -1):
            print "YEAH ALPHABET FOUND"
            matched_letter_list = get_replaced_list(used_letter, matched_letter_list, position)
            is_match = compare_list(matched_letter_list, target_list)
            if (is_match == 0):
                game_won = True;
                break
        print "---------------------------------------------------------------------------"    
        print "YOUR CURRENT WORD LOOKS LIKE ", matched_letter_list
        print "---------------------------------------------------------------------------"
    if game_won:
        print "\n----------- CONGRATS,YOU WON -----------------------------\n"
    else:
        print "\n----------- GAME OVER -------------------------------------"
        target_list = (''.join(target_list))   
        print "\nTHE CORRECT WORD WAS", target_list, "\n"  
                
                            
      
def get_letter_position(letter, list):  
    """ gives the index of the entered aplhabet in the target list 
    
        used_letter : Aplhabet entered by the user
        target_list : list which the user is trying to guess 
        
        return : This function returns the position of the aplhabet which is present in the target list
    """                     
    try:
        index = list.index(letter.upper())    
    except ValueError:
        print "OHH ALPHABATE IS NOT PRESENT IN THE WORD"
        return -1
    return index
    
               
def get_replaced_list(letter, list, position):  
    """
        replace the "-" with the alphabet guessed correctly 
        
        used_letter : Aplhabet entered by the user
        matched_letter_list : List which contains the aplhabets which are the perfect match with the aplphabets present in the target list
        position: position of the matched letter in the target list
        
        return : list which contains matched alphabets 
    """     
    list[position] = letter.upper()
    return list
    
   
def compare_list(first_list, second_list):    
    """
        comparing first_list and the second_list 
        
        first_list: list which contains alphabets that matches with the target list
        second_lsit : list which the user is trying to guess
        
        return: 
    """                
    is_match = cmp(first_list, second_list)
    return is_match

    
def get_valid_letter(letter): 
    """
        validate the  letter and returns next valid letter
        
        letter: entered by the user 
        
        return: return the valid letter
    """
    letter_len = len(letter)
    while((letter_len > 1) or not(is_letter(letter))):
        print "INVAILD INPUT, PLEASE ENTER ALPHABET ONLY"  
        letter = raw_input("ENTER THE ALPHABET: ") 
        letter_len = len(letter)
    return letter   
    
def get_initial_list(target_list):
    """ 
        target_list: word which the user is trying to guess
        
        return: initial list
    """
    initial_list = list()
    target_len = len(target_list)
    while(target_len > 0):
        initial_list.append('-')
        target_len = target_len - 1
    return initial_list
    
    
def is_letter(used_letter):
    is_letter = (ord(used_letter) >=65 and ord(used_letter) <=90) or (ord(used_letter) >=97 and ord(used_letter) <=122 )
    return is_letter
    
        
def main():
    start()

if __name__ == "__main__":
    main()



    