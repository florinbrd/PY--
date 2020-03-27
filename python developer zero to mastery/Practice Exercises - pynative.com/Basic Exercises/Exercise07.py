# Question 7: Return the number of times that the string “Emma” appears anywhere in the given string

def count_emma(str):
    substring = 'mere'
    mere_count = str.count(substring)
    return mere_count

def count_ema2(str):
    list_words = str.split()
    count_mere = list_words.count('mere')
    return count_mere

work_string = 'Florin are mere si de acolo face mere'

print(count_emma(work_string))
print(count_ema2(work_string))

