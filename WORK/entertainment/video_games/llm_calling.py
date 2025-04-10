from gigachat import GigaChat
from langchain_core.prompts import PromptTemplate
import os
from getpass import getpass
from pathlib import Path

# Переменная с директорией для сохранения файлов
concepts_dir = Path("path_to_directory")
concepts_dir.mkdir(parents=True, exist_ok=True)

# Список тем для генерации
concepts = {
    "computer_game": "Компьютерная игра",
    "game_janr": "Жанр игры",
    "game_developers": "Разработчик",
    "game_publisher": "Издатель",
    "game_engine": "Игровой движок",
    "game_mechanics": "Игровая механика",
    "story": "Сюжет",
    "game_character": "Игровой персонаж",
    "multiplayer_mode": "Многопользовательский режим",
    "gaming_community": "Игровое сообщество",
    "eSport": "Киберспорт",
    "additional_reality": "Дополненная реальность (AR)",
    "vr": "Виртуальная реальность (VR)",
    "gamification": "Геймификация",
    "gaming_platform": "Игровая платформа"
}



def create_markdown_file(filename, content):
    """Создает MD-файл с заданным содержанием"""
    filepath = concepts_dir / filename
    filepath.write_text(content, encoding="utf-8")
    print(f"Файл создан: {filepath}")

AUTH_TOKEN = ''

# Подключаемся к GigaChat
llm = GigaChat(credentials=AUTH_TOKEN, verify_ssl_certs=False, model='GigaChat-Pro')

# Улучшенный промпт с эмодзи и понятными примерами
prompt = """
Представь, что ты специалист по видеоиграм, который отлично умеет объяснять сложные вещи простым языком. Ты хорошо разбираешься в играх и знаешь всё про то, как они создаются, работают и становятся популярными.

Твоя задача — тебе будут приходить понятия, связанные с видеоиграми. Тебе нужно написать длинную, интересную, яркую, весёлую и познавательную статью по заданному понятию. Пиши для ребёнка 7 лет. 

Все термины, которые связаны с другим понятием, **пометь звёздочками**. Вот список понятий, которые мы будем обсуждать:

- **Компьютерная игра**
- **Жанр игры**
- **Разработчик**
- **Издатель**
- **Игровой движок**
- **Игровая механика**
- **Сюжет**
- **Игровой персонаж**
- **Многопользовательский режим**
- **Игровое сообщество**
- **Киберспорт**
- **Дополненная реальность (AR)**
- **Виртуальная реальность (VR)**
- **Геймификация** 
- **Игровая платформа**

---

### Правила:
1. На выходе должна быть markdown страница.
2. Пиши простыми словами.
3. Используй примеры из игр и жизни детей, чтобы объяснить понятия.
4. Каждый термин, который связан с другим понятием, отмечай звёздочками и добавляй сноски с определениями.
5. Начинай с простого определения, затем рассказывай интересную историю или аналогию.
6. В конце делай небольшой вывод, чтобы легко запомнить материал.
7. Пиши структурированно и увлекательно.

---

Пример запроса:  
- Понятие: **Компьютерная игра**  
- Ожидаемый ответ: Полная статья о том, что такое компьютерная игра, как она создаётся, кто её делает, как люди играют и почему это интересно.

Готов писать статьи, которые будут понятны и интересны детям? Начинаем!

Понятие: {query}
"""

for eng_name, rus_name in concepts.items():
    formatted_prompt = PromptTemplate(input_variables=['query'], template=prompt).format(query=rus_name)
    
    # Отправляем запрос в GigaChat
    response = llm.chat(formatted_prompt)
    
    # Создаем MD-файл с сгенерированным контентом, имя файла – английское название
    create_markdown_file(f'{eng_name}.md', response.choices[0].message.content)