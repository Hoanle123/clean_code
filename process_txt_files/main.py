import os
base_dir = os.path.dirname(os.path.abspath(__file__))
from utils.process_text import clean_text
from utils.load_txt import load_text
from utils.process_text import *
from utils.save_json import save_json
from config.config import FILE_PATH, OUTPUT_JSON_PATH, STOPWORDS
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='process_txt_files.log',  # chỉ định log file
    filemode='w'  # 'w' để ghi đè mỗi lần chạy, 'a' để append
)

def main():
    try:
        # Load text from file
        logging.info("Loading text from file.")
        text = load_text(os.path.join(base_dir, FILE_PATH))
    except Exception as e:
        logging.error(f"An error occurred while loading the text: {e}")
        return

    try:
        # Process text
        logging.info("Processing text.")
        cleaned_text = clean_text(text)
        text_no_stopwords = remove_stopwords(cleaned_text, set(STOPWORDS))
        word_count = count_words(text_no_stopwords)
        unique_word_count = count_unique_words(text_no_stopwords)
        top_words = top_n_words(text_no_stopwords, n=5)

    except Exception as e:
        logging.error(f"An error occurred while processing the text: {e}")
        return

    # Prepare data to save
    result_data = {
        "word_count": word_count,
        "unique_word_count": unique_word_count,
        "top_words": top_words
    }

    # Save results to JSON file
    try:
        logging.info("Saving results to JSON file.")    
        save_json(result_data, os.path.join(base_dir, OUTPUT_JSON_PATH))
    except Exception as e:
        logging.error(f"An error occurred while saving the JSON file: {e}")
        
if __name__ == "__main__":
    main()