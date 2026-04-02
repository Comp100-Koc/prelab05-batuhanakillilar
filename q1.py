def longest_palindromic_substring(s):

    longest = ""
    
    for start in range(len(s)):
        for end in range(start + 2, len(s) + 1):
            curr = s[start:end]
            reverse = ""
            
            for char in curr:
                reverse = char + reverse
                
            if (curr == reverse):
                if (len(curr) > len(longest)):
                    longest = curr
                    
    return longest