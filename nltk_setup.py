import nltk
import os

# Создание папки nltk_data локально
nltk_data_path = 'nltk_data'
os.makedirs(nltk_data_path, exist_ok=True)

# Добавляем оба пути, чтобы nltk знал, где искать
nltk.data.path.append(nltk_data_path)
nltk.data.path.append('/app/nltk_data')  # для Heroku

# Загружаем все языковые токенизаторы через punkt
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)

# Языки, которые хотим проверить
languages = ['english', 'russian', 'german', 'french', 'spanish', 'italian']

# Проверяем загрузку соответствующих .pickle-файлов
for lang in languages:
    try:
        tokenizer = nltk.data.load(f'tokenizers/punkt/{lang}.pickle')
        print(f"{lang}.pickle успешно загружен.")
    except LookupError as e:
        print(f"Ошибка при загрузке модели для {lang}: {e}")
