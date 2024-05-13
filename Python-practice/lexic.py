import numpy as np


def disposition(clear_records, _records, ci):
    # Getting all the words for all entries for certain CI
    words = [record["ITEMS"].split(",") for record in clear_records
             if record["CI"] == str(ci) and isinstance(record["ITEMS"], str)]

    # Parameters for the operation
    entries, max_list = len(words), max(len(lst) for lst in words)

    header = _records.ci_words[str(ci)]["words"]
    # Create a matrix with the position of appearance for each different word
    evaluate = {}
    for head in header:
        indexes = []
        for word in words:
            if head in word:
                indexes.append(word.index(head)+1)
        evaluate[head] = sorted(indexes)

    # Store and make the sum for all the different words to obtain the lexical index
    lexical_index = {}
    for head in header:
        value = 0
        for i in set(evaluate[head]):
            # Count frequency and sum value for each word position
            freq = evaluate[head].count(i)
            # value += 2.71828**(-2.3 * (i-1) / (max_list - 1)) * freq / entries
            value += np.exp(-2.3 * (i-1) / (max_list - 1)) * freq / entries
        # Calculate value for lexical index
        lexical_index[head] = value
    # Sort the lexical_index dictionary by values in descending order
    lexical_index = dict(sorted(lexical_index.items(), key=lambda item: item[1], reverse=True))

    return lexical_index


def disposition_index(clear_records, _records):
    disp = {}
    for i in _records.ci_words.keys():
        ci = disposition(clear_records, _records, i)
        disp[i] = ci
    return disp
