def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char.isalpha(): #Only consider alphabetic characters
            counter[char] = counter.get(char, 0) + 1
    most_common = max(counter, key=counter.get)
    return most_common


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")