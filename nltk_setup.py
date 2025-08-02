import nltk
import os

# Указываем директорию для загрузки
nltk_data_path = 'nltk_data'
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)

# Добавляем путь, чтобы nltk нашёл нужные файлы
nltk.data.path.append('/app/nltk_data')

# Указываем нужные языки
languages = ['english', 'russian', 'german', 'french', 'spanish', 'italian']

# Проверяем, что директория существует
punkt_dir = os.path.join(nltk_data_path, 'tokenizers', 'punkt')
os.makedirs(punkt_dir, exist_ok=True)

# Загружаем языковые модели
for lang in languages:
    try:
        nltk.download('punkt', download_dir=nltk_data_path)
        tokenizer = nltk.data.load(f'tokenizers/punkt/{lang}.pickle')
        with open(os.path.join(punkt_dir, f'{lang}.pickle'), 'wb') as f:
            f.write(tokenizer._params.serialize())
        print(f"{lang}.pickle сохранён.")
    except LookupError as e:
        print(f"Ошибка для {lang}: {e}")
