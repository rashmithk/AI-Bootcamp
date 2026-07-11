typeval=input("Enter a sentence: ")
totalchars= len(typeval)
totalwords= len(typeval.split())
up= typeval.upper()
low= typeval.lower()
titlecase= typeval.title()
rev= " ".join(typeval.split()[::-1])
vowels = "aeiouAEIOU"
vowel_count = 0
space_count = 0
for char in typeval:
    if char in vowels:
        vowel_count += 1
    elif char == " ":
        space_count += 1
print(f"Total characters: {totalchars}")
print(f"Total words: {totalwords}")
print(f"Upper case: {up}")
print(f"Lower case: {low}")
print(f"Title case: {titlecase}")
print(f"Reversed sentence: {rev}")
print(f"Total Vowels: {vowel_count}")
print(f"Total Spaces: {space_count}")
