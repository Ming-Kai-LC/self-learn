"""
Text Preprocessing for Sentiment Analysis

Handles cleaning, normalization, and preparation of text data
"""

import re
import string
from typing import List

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class TextPreprocessor:
    """Text preprocessing for sentiment analysis"""

    def __init__(self, lowercase=True, remove_stopwords=True, remove_numbers=False):
        """
        Initialize preprocessor

        Args:
            lowercase: Convert text to lowercase
            remove_stopwords: Remove English stopwords
            remove_numbers: Remove numeric characters
        """
        self.lowercase = lowercase
        self.remove_stopwords = remove_stopwords
        self.remove_numbers = remove_numbers

        # Download required NLTK data
        try:
            nltk.data.find("tokenizers/punkt")
        except LookupError:
            nltk.download("punkt", quiet=True)

        try:
            nltk.data.find("corpora/stopwords")
        except LookupError:
            nltk.download("stopwords", quiet=True)

        # Load stopwords
        if self.remove_stopwords:
            self.stopwords = set(stopwords.words("english"))
            # Keep some sentiment-bearing words
            keep_words = {
                "not",
                "no",
                "nor",
                "neither",
                "never",
                "none",
                "very",
                "too",
                "most",
                "more",
                "less",
            }
            self.stopwords = self.stopwords - keep_words
        else:
            self.stopwords = set()

    def remove_urls(self, text: str) -> str:
        """
        Remove URLs from text

        Args:
            text: Input text

        Returns:
            Text with URLs removed
        """
        url_pattern = r"https?://\S+|www\.\S+"
        return re.sub(url_pattern, "", text)

    def remove_html_tags(self, text: str) -> str:
        """
        Remove HTML tags from text

        Args:
            text: Input text

        Returns:
            Text with HTML tags removed
        """
        html_pattern = r"<.*?>"
        return re.sub(html_pattern, "", text)

    def remove_mentions_hashtags(self, text: str) -> str:
        """
        Remove @mentions and #hashtags

        Args:
            text: Input text

        Returns:
            Text with mentions and hashtags removed
        """
        text = re.sub(r"@\w+", "", text)
        text = re.sub(r"#\w+", "", text)
        return text

    def remove_extra_whitespace(self, text: str) -> str:
        """
        Remove extra whitespace

        Args:
            text: Input text

        Returns:
            Text with normalized whitespace
        """
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def remove_punctuation(self, text: str, keep_apostrophes=True) -> str:
        """
        Remove punctuation from text

        Args:
            text: Input text
            keep_apostrophes: Keep apostrophes (for contractions)

        Returns:
            Text with punctuation removed
        """
        if keep_apostrophes:
            # Keep apostrophes for contractions (don't, isn't, etc.)
            punct = string.punctuation.replace("'", "")
        else:
            punct = string.punctuation

        return text.translate(str.maketrans("", "", punct))

    def expand_contractions(self, text: str) -> str:
        """
        Expand common English contractions

        Args:
            text: Input text

        Returns:
            Text with contractions expanded
        """
        contractions = {
            "ain't": "am not",
            "aren't": "are not",
            "can't": "cannot",
            "can't've": "cannot have",
            "could've": "could have",
            "couldn't": "could not",
            "didn't": "did not",
            "doesn't": "does not",
            "don't": "do not",
            "hadn't": "had not",
            "hasn't": "has not",
            "haven't": "have not",
            "he'd": "he would",
            "he'll": "he will",
            "he's": "he is",
            "i'd": "i would",
            "i'll": "i will",
            "i'm": "i am",
            "i've": "i have",
            "isn't": "is not",
            "it'd": "it would",
            "it'll": "it will",
            "it's": "it is",
            "let's": "let us",
            "shouldn't": "should not",
            "that's": "that is",
            "there's": "there is",
            "they'd": "they would",
            "they'll": "they will",
            "they're": "they are",
            "they've": "they have",
            "wasn't": "was not",
            "we'd": "we would",
            "we'll": "we will",
            "we're": "we are",
            "we've": "we have",
            "weren't": "were not",
            "what's": "what is",
            "won't": "will not",
            "wouldn't": "would not",
            "you'd": "you would",
            "you'll": "you will",
            "you're": "you are",
            "you've": "you have",
        }

        words = text.split()
        expanded_words = []

        for word in words:
            word_lower = word.lower()
            if word_lower in contractions:
                expanded_words.append(contractions[word_lower])
            else:
                expanded_words.append(word)

        return " ".join(expanded_words)

    def tokenize(self, text: str) -> List[str]:
        """
        Tokenize text into words

        Args:
            text: Input text

        Returns:
            List of tokens
        """
        return word_tokenize(text)

    def remove_stopwords_from_tokens(self, tokens: List[str]) -> List[str]:
        """
        Remove stopwords from token list

        Args:
            tokens: List of tokens

        Returns:
            Filtered token list
        """
        return [token for token in tokens if token.lower() not in self.stopwords]

    def preprocess(self, text: str) -> str:
        """
        Complete preprocessing pipeline

        Args:
            text: Raw input text

        Returns:
            Preprocessed text
        """
        if not isinstance(text, str):
            text = str(text)

        # Remove URLs and HTML
        text = self.remove_urls(text)
        text = self.remove_html_tags(text)

        # Remove mentions and hashtags
        text = self.remove_mentions_hashtags(text)

        # Expand contractions
        text = self.expand_contractions(text)

        # Convert to lowercase
        if self.lowercase:
            text = text.lower()

        # Remove punctuation
        text = self.remove_punctuation(text, keep_apostrophes=False)

        # Remove numbers if specified
        if self.remove_numbers:
            text = re.sub(r"\d+", "", text)

        # Remove extra whitespace
        text = self.remove_extra_whitespace(text)

        # Tokenize
        tokens = self.tokenize(text)

        # Remove stopwords
        if self.remove_stopwords:
            tokens = self.remove_stopwords_from_tokens(tokens)

        # Join tokens back into string
        text = " ".join(tokens)

        return text

    def preprocess_batch(self, texts: List[str]) -> List[str]:
        """
        Preprocess batch of texts

        Args:
            texts: List of raw texts

        Returns:
            List of preprocessed texts
        """
        return [self.preprocess(text) for text in texts]


# ==================== Testing ====================

if __name__ == "__main__":
    # Test the preprocessor
    preprocessor = TextPreprocessor()

    test_texts = [
        "This is AMAZING! I can't believe how good this product is!!! 😍",
        "Terrible product. Don't waste your money on this garbage.",
        "Check out our website at https://example.com for more info!",
        "@user This isn't what I expected, but it's okay I guess...",
        "   Multiple    spaces    and weird    formatting   ",
    ]

    print("Text Preprocessing Examples:\n")
    print("=" * 80)

    for i, text in enumerate(test_texts, 1):
        print(f"\n{i}. Original:")
        print(f"   {text}")
        print(f"\n   Preprocessed:")
        print(f"   {preprocessor.preprocess(text)}")
        print("-" * 80)
