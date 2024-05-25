#!/usr/bin/env python3
def return_evens(sequence):
    return [x for x in sequence if x % 2 == 0]

# Example usage:
# sequence = [1, 2, 3, 4, 5, 6]
# print(return_evens(sequence))  # Output: [2, 4, 6]


def make_exclamation(sentences):

    return [sentence + '!' for sentence in sentences]

# Example usage:
# sentences = ["Hello", "How are you", "This is great"]
# print(make_exclamation(sentences))  # Output: ["Hello!", "How are you!", "This is great!"]
