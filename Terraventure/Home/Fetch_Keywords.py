import nltk

# Function to extract main words from a query
def extract_main_words(query):
    # Tokenize the query into individual words
    words = nltk.word_tokenize(query)
    # print(words)

    # Perform part-of-speech tagging on the words
    tagged_words = nltk.pos_tag(words)
    # print(tagged_words)
    # Filter and extract only the main words (nouns and proper nouns)
    main_words = [word for word, tag in tagged_words if tag.startswith('NN')]            
    return main_words

# i=input("ENTER:")
# print(extract_main_words(i))
