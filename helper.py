def is_isbn_or_key(kwy_word):
    isbn_or_key = 'key'
    if len(kwy_word) == 13 and kwy_word.isdigit():
        isbn_or_key = 'isbn'
    if '-' in kwy_word and len(kwy_word.replace('-', '')) == 10 and kwy_word.replace('-', '').isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
