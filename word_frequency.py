STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with', ''
    ]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    word_count = {}

    with open(file) as file_doc:
        text = file_doc.read()

    text = text.replace("\n", " ")

    text = remove_punctuation(text)

    text = text.lower()
    word_list = text.split(" ")

    stop_word_set = set(STOP_WORDS)
    filtered_word_list = [item for item in word_list if item not in stop_word_set]
    sorted_word_list = sorted(filtered_word_list)

    for i in word_list:
        if i not in word_count:
            for i in sorted_word_list:
                word_count[i] = sorted_word_list.count(i)

    value_sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

    for key, value in value_sorted_word_count.items():
        print(key.rjust(15), ' | ', str(value).center(2), value * ('*'))

    # print(type(text))
    # print(file_doc.closed)

def remove_punctuation(text):
    import string
    result = ""
    for i in text:
        if i not in string.punctuation:
            result += i
    return result

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
