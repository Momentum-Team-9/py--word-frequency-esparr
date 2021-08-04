STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    import string
    word_count = {}
    with open(file) as file_doc:
        text = file_doc.read()
        for i in text:
            if i in string.punctuation:
                text = text.replace(i, "")
    text = text.replace("\n", " ")
    text = text.lower()
    text = text.split(" ")
    
    print(type(text))
    print(text)
    print(file_doc.closed)

# - remove punctuation
# - normalize all words to lowercase
# - remove "stop words" -- words used so frequently they are ignored
# - go through the file word by word and keep a count of how often each word is used
# - create a dictionary with value of word and a key of count. 

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
