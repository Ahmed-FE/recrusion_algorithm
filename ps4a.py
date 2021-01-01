# Problem Set 4A
# Name: Ahmed Elsayed Abdelnaby
# Collaborators:
# Time Spent: x:xx

def get_permutations(word):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    length_word=len(word)
    # here are the basic case when the number of the letter in the sequence is equal to 0 
    if length_word==1:
       result=[]
       result.append(word)
       return(result)
   # here is when we have more than one letter we take one letter then store it as aletter and remove it from the sequence 
    if length_word>1:
       letter=word[0]
       word=word.replace(word[0],'')
       # here when the recrusion happen after removing the letter the new sequence go in a new loop 
       result=get_permutations(word)
       # the first time result will be defind is when length_word=1 
       # the posint from this line is to know how many letters i have in every word now in the list so if i have ab and c is in hand 
       #that means I have 3 letters which result in 3 copies for two elements 
       length_list=len(result[0])
       number_of_elements_copy=length_list+1
       # to make copies of some list element inside the same list 
       result=[ele for ele in result for _ in range(number_of_elements_copy)] 
       #print(result)
       # this position needs to repeat every time the number of the original elements is done . so if I have two letters that means 
       # i started with list['ab,'ba']
       # the list with the copies will be ['ab','ba','ab','ba','ab','ba']
       # c needs to be added in positions 0 ,1 ,2 then again 0,1,2 so I take the number of letters inside the list to indicate how many 
       #indexes I have 
       letter_position=0
       # this part is to add the letter in my hand in its correct position .
       for index ,value in enumerate(result):
         number_of_letter_solved=len(value)
         value=list(value)
         value.insert(letter_position,letter)
         value=''.join(value)
         result[index]=value
         letter_position +=1
         if letter_position >number_of_letter_solved:
            letter_position=0
         
    return(result)
######################################################################################################################################
######################################################################################################################################
### this part is to make test cases for this problem I will need to create a factorial recrusion function to make sure the number of elements 
### from my answer is the same as the number of expected elements then I will need to make     
def factorial(a):
    """
    it is  arecrusive function that takes a number and return a factorial of this number 

    Parameters
    ----------
    a : any number .

    Returns
    -------
    result : return factorial such as factorial 3 is 3*2*1 .

    """
    if a ==1:
       result =1 
    if a>1:
        result=a*factorial(a-1)
    return (result)

if __name__ == '__main__':
    example_input = ['a','ab','abc','abcd','abcde']
    for i in example_input:
        answer=get_permutations(i)
        length_answer=len(answer)
        number_of_expected_elements=factorial(len(i))
### the first case is to check if its giving the right number of combination or not       
        try:
            assert length_answer==number_of_expected_elements
            print('the number of elments is as expected for (' + i +' )its :'+  str(length_answer) )
        except AssertionError :
            print('the number of elments is not as expected ')
### the second test case is to check if the answer list has any reptition in elements or not 
### we use set to remove any repetion in list elements so if list is [1,2,3,1,1] set will make it [1,2,3]
        length_answer=len(set(answer))
        try:
            assert length_answer==number_of_expected_elements
            print('the number of unique elments is as expected for (' + i +' )its :'+  str(length_answer) )
        except AssertionError :
            print('the number of elments is not as expected ') 
### the last case is to make sure the answer is as it should be for two cases 'abc' ,abcd'
    word='abc'
    expected_answer_for_abc=['abc','acb','bca','bac','cba','cab'] 
    script_answer_for_abc=get_permutations(word)
    number_of_element=0
    for i in expected_answer_for_abc:
        if i in script_answer_for_abc:
            number_of_element +=1
        else:
            raise ValueError('the value '+ i + ') is not in giving by the script')
        if number_of_element==6:
            print('the expected answer was ('+str(expected_answer_for_abc)+') matching the answer from the script ('+str(script_answer_for_abc)+')')
                             
            
            
        
              
                          
        
    
    
   


  
            
    

      
        


    
