from django.shortcuts import render
from django.http import HttpResponse
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from textblob import TextBlob

# Убедись, что все нужные ресурсы загружены
nltk.download('punkt')
nltk.download('stopwords')
def upload_text(request):
    input_text = ""
    total_words = 0
    total_filtered_words = 0
    total_characters = 0
    word_freq = []
    sentiment = None

    if request.method == 'POST':
        input_text = request.POST.get('text', '')

        if input_text.strip():  # проверка, что текст не пустой
            tokens = word_tokenize(input_text)
            words = [word.lower() for word in tokens if word.isalpha()]

            stop_words = set(stopwords.words('english'))
            filtered_words = [word for word in words if word not in stop_words]

            total_words = len(words)
            total_filtered_words = len(filtered_words)
            total_characters = len(input_text)

            word_freq = Counter(filtered_words).most_common(10)

            blob = TextBlob(input_text)
            sentiment = blob.sentiment

    return render(request, 'analyzer/upload.html', {
        'text': input_text,
        'total_words': total_words,
        'unique_words': len(set(filtered_words)) if input_text.strip() else 0,
        'most_common': word_freq,
        'characters': total_characters,
        'polarity': sentiment.polarity if sentiment else None,
        'subjectivity': sentiment.subjectivity if sentiment else None,
    })
