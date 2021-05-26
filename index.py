def make_dict(str):
    wordcounts = dict()
    words = str.split()

    for word in words:
        lowercase = word.lower()
        wordcounts[lowercase] = wordcounts.get(lowercase, 0) + 1

    big_word = None
    big_count = None
    for word, count in wordcounts.items():
        if big_count is None or count >= big_count:
            big_word = word
            big_count = count

    return (big_word, big_count)


print(make_dict('Here is a test to make sure that this test is working.'))
