def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

# Example usage:
grams = int(input("Enter grams: "))
print(f"{grams} grams is equal to {grams_to_ounces(grams)} ounces")