import json


def load_candidates():
     """
      Открываем файл с кандидатами на чтение
      загружаем данные из файла
     """
     with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)

     """Создаем функцию для загрузки всех кандидатов из списка"""
def get_all():
    return load_candidates()

    """
     Функция перебирает список кандидатов 
     и возвращает кандитата по (pk)
    """

def get_candidate_by_pk(pk):
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return

    """
    Функция перебирает список кандитатов 
       и возвращает кандитата по навыку
    """
def get_candidate_by_skill(skill):
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates

