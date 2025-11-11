import string
from collections import Counter
def analyze_text_and_frequency():
    print("\n" + "=" * 50)
    print("Phân tích đoạn văn, đếm từ")
    print("=" * 50)
    paragraph = input("Vui lòng nhập một đoạn văn bản tiếng Anh: ")
    if not paragraph.strip():
        print("Bạn đã nhập một đoạn văn rỗng.")
        return
    translator = str.maketrans('', '', string.punctuation)  
    cleaned_paragraph = paragraph.translate(translator).lower()  
    words = cleaned_paragraph.split()  
    if not words:
        print("Sau khi loại bỏ dấu câu, không còn từ nào để phân tích.")
        return
    word_counts = Counter(words)
    sorted_word_counts = word_counts.most_common()
    print("\n--- KẾT QUẢ PHÂN TÍCH ---")
    print(f"Tổng số từ (bao gồm trùng lặp): {len(words)}")
    print(f"Tổng số từ duy nhất: {len(word_counts)}")
    print("-" * 35)
    print("Tần suất xuất hiện (Giảm dần):")

    # In ra kết quả
    for word, count in sorted_word_counts:
        # căn lề cho đẹp
        print(f"   - {word.ljust(15)}: {count} lần")
    print("=" * 50)

analyze_text_and_frequency()