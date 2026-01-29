def count_vowel_and_consonants():
    user_string = input("Nhập một chuỗi tiếng Anh: ")
    processed_string = ''.join(filter(str.isalpha,user_string.lower()))
    if not processed_string:
        print("*"*30)
        print("Hãy thử lại một chuỗi mới!!")
        return
    vowel_count = 0
    consonant_count = 0
    VOWEL = {"a","e","i","o","u"}
    for char in processed_string:
        if char in VOWEL:
            vowel_count +=1
        else:
            consonant_count +=1
    print("*"*30)
    print(f"--Số lượng nguyên âm trong chuỗi: {vowel_count}")
    print(f"--Số lượng phụ âm trong chuỗi: {consonant_count}")
    print("*"*30)
count_vowel_and_consonants()