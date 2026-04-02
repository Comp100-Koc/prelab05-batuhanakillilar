def remove_adjacent_duplicates(s):

    duplicate = True
    
    while duplicate == True:
        
        duplicate = False
        string = ""
        i = 0
        while i < len(s):
            
            if (i < len(s) - 1 and s[i] == s[i + 1]):
                i += 2
                duplicate = True
            else:
                string += s[i]
                i += 1   
        
        s = string
        
    return s