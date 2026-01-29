def check_palindrome():
    original_string = input("")
    processed_string = original_string.relace(" ","").lower()
    n = len(processed_string)
    left = 0
    right = n-1
    is_palindrome = True
    while left<right:
        if processed_string[left]!=processed_string[right]:
            is_palindrome = False
            break
    if is_palindrome:
        print("true")
    else:
        print("false")
check_palindrome()