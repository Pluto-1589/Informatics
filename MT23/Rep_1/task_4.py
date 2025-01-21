def strings_containing(strings:list, word:str) -> list:
    return [s for s in strings if word.lower() in s.lower()]
    
    
    
print( strings_containing(["Hello", "there", "friend"], "he" ) )
print( strings_containing(["abc", "cde", "DEF"], "de" ) )