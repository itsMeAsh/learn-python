def anagrams(word, words):
    is_match = sorted(word)
    return [item for item in words if is_match == sorted(item)]

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))
