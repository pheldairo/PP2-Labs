a = "Hello"
print(a) 

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) # Or use ''' instead of """ to make multiple line string

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

print(len(a))

txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
  print("Yes, 'free' is present.")
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


print(a[2:5])
print(a[2:])
print(a[:5])
print(a[-5:-2])

print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))

a = "Hello"
b = "World"
c = a + b
print(c)

age = 36
txt = f"My name is Daniil, I am {age}"
# txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)
txt = f"The price is {price:.2f} dollars" 
print(txt)
txt = f"The price is {20 * 59} dollars" 
print(txt)

# Escape characters
# \ - Single Quote
# \\ - Backslash
# \n - New Line
# \r - Carriage Return
# \t - Tab
# \b - Backspace
# \f - Form Feed
# \ooo - Octal value
# \xhh - Hex value