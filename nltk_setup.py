import nltk
import os
import urllib.request

# Папка, где будут храниться данные NLTK
nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')
punkt_path = os.path.join(nltk_data_path, 'tokenizers', 'punkt')
os.makedirs(punkt_path, exist_ok=True)

# Указываем пути для поиска
nltk.data.path.append(nltk_data_path)
nltk.data.path.append('/app/nltk_data')  # для Heroku

# Загружаем базовые ресурсы
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)

# Языки и их файлы
languages = {
    'english': 'english.pickle',
    'russian': 'russian.pickle',
    'german': 'german.pickle',
    'french': 'french.pickle',
    'spanish': 'spanish.pickle',
    'italian': 'italian.pickle'
}

base_url = "https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt/"

# Скачиваем модели
for lang, filename in languages.items():
    dest_path = os.path.join(punkt_path, filename)
    if not os.path.exists(dest_path):
        print(f"Скачиваем {filename}...")
        try:
            urllib.request.urlretrieve(base_url + filename, dest_path)
            print(f"{filename} сохранён в {dest_path}")
        except Exception as e:
            print(f"Ошибка при скачивании {filename}: {e}")
    else:
        print(f"{filename} уже существует.")

# Проверка загрузки
for lang, filename in languages.items():
    try:
        tokenizer = nltk.data.load(f'tokenizers/punkt/{filename}')
        print(f"{filename} успешно загружен.")
    except LookupError as e:
        print(f"Ошибка при загрузке {filename}: {e}")
