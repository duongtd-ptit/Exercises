def count_words_in_sentence():
    sentence = input("Vui lòng nhập một câu bất kỳ: ")
    word_list = sentence.split()
    word_count = len(word_list)
    print("\n" + "=" * 40)
    print(f"Câu bạn đã nhập: '{sentence}'")
    print("-" * 40)
    if word_count == 0:
        print("Câu này không chứa từ nào (có thể chỉ chứa khoảng trắng hoặc rỗng).")
    else:
        print(f"Tổng số lượng từ trong câu là: **{word_count}**")
        print("=" * 40)
count_words_in_sentence()