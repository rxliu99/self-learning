# Romain to Integer

# https://leetcode.com/problems/roman-to-integer/

## Takeaways: ##
#	Use dictionary to store conversion relationship
#	The usage of string.replace(original_str, new_str)

## Solution: ##
# Reverse the Romain string, so the numerials are now from smallest to largest from left to right
# If the current numerial is less than the previous numerial, an excpetion occurs and the current value is subtracted from total
# If the current numerial is greater than or equal to the previous numerial, add the current value to total
def romanToInt(s):
	total, prev = 0, 0
	sym_to_val = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
	for i in s[::-1]:
		if sym_to_val[i] >= prev:
			total += sym_to_val[i]
		else:
			total -= sym_to_val[i]
		prev = sym_to_val[i]
	
	return total
	
## Alternative solution: ##
# Replace the two-letter patterns with one-letter patterns that have the same numerical value
# This approach violates the rules of Romain numericals, but does the job cleverly
def romanToInt(self, s: str) -> int:
	translations = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000
	}
	total = 0
	
	s = s.replace("IV", "IIII")\
	     .replace("IX", "VIIII")\
		 .replace("XL", "XXXX")\
         .replace("XC", "LXXXX")\
         .replace("CD", "CCCC")\
		 .replace("CM", "DCCCC")
	
	for char in s:
		total += translations[char]
	
	return number
