def reverse_words_order_and_swap_cases(sentence):
    # Write your code herestr
  
    str2=sentence.swapcase()
    li=str2.split()
    li.reverse()
    str1 = ' '.join([str(elem) for elem in li]) 
    return str1

