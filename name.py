from collections import Counter
from difflib import SequenceMatcher

def preprocess(name):
    words = name.split()
    name = name.lower().replace(" ", "").replace(".", "")
    name = ''.join([word for word in words if len(word) > 1])
    # print(name)
    return name

def get_ngrams(name, n=2):
    name = preprocess(name)
    return [name[i:i+n] for i in range(len(name)-n+1)]

def ngram_similarity(name1, name2, n=2):
    ngrams1 = get_ngrams(name1, n)
    ngrams2 = get_ngrams(name2, n)
    counter1 = Counter(ngrams1)
    counter2 = Counter(ngrams2)
    intersection = sum((counter1 & counter2).values())
    total = sum((counter1 | counter2).values())

    return intersection / total if total > 0 else 0

# Case 1: Use of abbreviations 
name1 = "Mr. Ravi Kumar"
name2 = "RaviKumar"
similarity_score = ngram_similarity(name1, name2, n=2)
print(f"Case 1.1: {similarity_score:.2f}")

name1 = "Mrs. Vijayalakshmi"
name2 = "Miss Vijayalakshmi"
similarity_score = ngram_similarity(name1, name2, n=2)
print(f"Case 1.2: {similarity_score:.2f}")


# Case 2: Name order differences 
name1 = "Dheeraj Manirathnam Anna"
name2 = "Manirathnam Anna Dheeraj"
similarity_score = ngram_similarity(name1, name2, n=2)
print(f"Case 2: {similarity_score:.2f}")

# Case 3: Initials vs. full names
name1 = "R. K. Narayan"
name2 = "Rasipuram Krishnaswami Narayan"
similarity_score = ngram_similarity(name1, name2, n=2)
print(f"Case 3: {similarity_score:.2f}")

# Case 4: Abbreviated names
name1 = "Vijayalakshmi"
name2 = "lakshmi"
similarity_score = ngram_similarity(name1, name2, n=2)
print(f"Case 4: {similarity_score:.2f}")

# Case 5: Surname mismatch (partial/full)
name1 = "Ravi Kumar"
name2 = "RaviKumar"
similarity_score = ngram_similarity(name1, name2, n=2)
print(f"Case 5: {similarity_score:.2f}")

# Case 6: Omission/presence of middle name/surname 
name1 = "Ravi Kumar"
name2 = "Ravi"
similarity_score = ngram_similarity(name1, name2, n=2)
print(f"Case 6: {similarity_score:.2f}")

# Case 7: Spelling variations (typos): 
name1 = "Omprakash"
name2 = "Onprakash"
similarity_score = ngram_similarity(name1, name2, n=2)
print(f"Case 7: {similarity_score:.2f}")

# Case 8: Missed or extra spaces: 
name1 = "Ravi Kumar"
name2 = "RaviKumar"
similarity_score = ngram_similarity(name1, name2, n=2)
print(f"Case 8: {similarity_score:.2f}")

# Case 9: Repetition of the word: 
name1 = "Ravi Kumar"
name2 = "Ravi Ravi Kumar"
similarity_score = ngram_similarity(name1, name2, n=2)
print(f"Case 9: {similarity_score:.2f}")

# Case 8: Missing part of name: 
name1 = "Dheeraj M Anna" 
name2 = "Dheeraj Anna"
similarity_score = ngram_similarity(name1, name2, n=2)
print(f"Case 8: {similarity_score:.2f}")
