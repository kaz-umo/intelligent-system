import nltk
import os

# Указываем директорию для загрузки
nltk_data_path = 'nltk_data'
os.makedirs(nltk_data_path, exist_ok=True)

# Добавляем путь, чтобы nltk нашёл нужные файлы
nltk.data.path.append(nltk_data_path)
nltk.data.path.append('/app/nltk_data')  # для Heroku

# Загружаем нужные ресурсы
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)

# Языки, для которых нужно проверить наличие модели
languages = ['english', 'russian', 'german', 'french', 'spanish', 'italian']

# Пробуем загрузить модели токенизаторов
for lang in languages:
    try:
        tokenizer = nltk.data.load(f'tokenizers/punkt/{lang}.pickle')
        print(f"{lang}.pickle успешно загружен.")
    except LookupError as e:
        print(f"Ошибка при загрузке модели для {lang}: {e}")
