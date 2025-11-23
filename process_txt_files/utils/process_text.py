import re

def clean_text(text: str) -> str:
    """Clean the input text by removing extra whitespace special characters, convert to lowercase.

    Args:
        text (str): The input text to be cleaned.
    Returns:
        str: The cleaned text.
    """
    if text is None:
        return ""

    # Convert to lowercase
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_stopwords(text: str, stopwords: set) -> str:
    """Remove stopwords from the input text.

    Args:
        text (str): The input text.
        stopwords (set): A set of stopwords to remove.

    Returns:
        str: The text with stopwords removed.
    """
    if text is None:
        return ""

    words = text.split()
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)

def count_words(text: str) -> int:
    """Count the number of words in the input text.

    Args:
        text (str): The input text.
    Returns:
        int: The number of words in the text.
    """
    if text is None:
        return 0

    words = text.split()
    return len(words)

def count_unique_words(text: str) -> int:
    """Count the number of unique words in the input text.

    Args:
        text (str): The input text.
    Returns:
        int: The number of unique words in the text.
    """
    if text is None:
        return 0

    words = text.split()
    unique_words = set(words)
    return len(unique_words)

def top_n_words(text: str, n: int = 5) -> list:
    """Get the top N most frequent words in the input text.

    Args:
        text (str): The input text.
        n (int): The number of top frequent words to return. Defaults to 5.

    Returns:
        list: A list of tuples containing the top N words and their counts.
    """
    if text is None:
        return []

    words = text.split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    sorted_words = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:n]