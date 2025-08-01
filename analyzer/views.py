from django.shortcuts import render
from django.http import HttpResponse
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from textblob import TextBlob

# Загрузка необходимых данных NLTK
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

import nltk
nltk.download('punkt', download_dir='/app/nltk_data')
nltk.download('stopwords', download_dir='/app/nltk_data')
nltk.data.path.append('/app/nltk_data')

# View для анализа текста
def upload_text(request):
    input_text = ""
    total_words = 0
    total_filtered_words = 0
    total_characters = 0
    word_freq = []
    sentiment = None
    unique_words_count = 0

    if request.method == 'POST':
        input_text = request.POST.get('text', '').strip()

        if input_text:
            tokens = word_tokenize(input_text)
            words = [word.lower() for word in tokens if word.isalpha()]

            stop_words = set(stopwords.words('english'))
            filtered_words = [word for word in words if word not in stop_words]

            total_words = len(words)
            total_filtered_words = len(filtered_words)
            total_characters = len(input_text)
            unique_words_count = len(set(filtered_words))

            word_freq = Counter(filtered_words).most_common(10)

            blob = TextBlob(input_text)
            sentiment = blob.sentiment

    return render(request, 'analyzer/upload.html', {
        'text': input_text,
        'total_words': total_words,
        'unique_words': unique_words_count,
        'most_common': word_freq,
        'characters': total_characters,
        'polarity': sentiment.polarity if sentiment else None,
        'subjectivity': sentiment.subjectivity if sentiment else None,
    })

# Новый view для страницы с ракетой
def rocket_view(request):
    return render(request, 'analyzer/rocket.html')
