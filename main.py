import sys

from stats import count_characters, get_book_text, sort_count

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
elif len(sys.argv) == 2:
    path = sys.argv[1]
else:
    print("One at a time, please!")
    sys.exit(1)
width = 60
# print(sys.argv)
print(f"{' BOOKBOT ':=^{width}}")
print(f"Analyzing book found at {path}...")
print(f"{' Word Count ':-^{width}}")
s = get_book_text(path)
print(f"Found {len(s.split())} total words")
counted: dict[str, int] = count_characters(get_book_text(path))
# print(f"Counter: {counted}")
sorted = sort_count(counted)
print(f"{' Character Count ':-^{width}}")
for i in range(len(sorted)):
    print(f"{sorted[i]['char']}: {sorted[i]['num']}")
print(f"{' END ':=^{width}}")
