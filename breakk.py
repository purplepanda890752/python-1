num = input("Enter a word: ")  
count = num.count("T") + num.count("t")  # Count occurrences of both 'T' and 't'

if count > 0:
    print(f"'T' appears {count} times in your input.")
else:
    print("The letter 'T' is not found.")

