import os
from serpapi import GoogleSearch
from google_scholar_organic_results import organic_results

def cite_results():
    print("extracting cite results..")

    citation_results = [] # создаем временный список для хранения извлеченных данных

    for citation in organic_results():
        params = {
            "api_key": os.getenv("API_KEY"), # ключ для аутентификации в SerpApi
            "engine": "google_scholar_cite", # движок для парсинга цитируемых результатов
            "q": citation["result_id"]
        }
        search = GoogleSearch(params) # парсинг на бэкенде SerpApi
        results = search.get_dict() # JSON конвертируется в словарь

        print(f"Currently extracting {citation['result_id']} citation ID.")

        for result in results["citations"]:
            cite_title = result["title"]
            cite_snippet = result["snippet"]

            citation_results.append({
                "organic_result_title": citation["title"], # чтобы понимать откуда берутся Цитируемые результаты
                "organic_result_link": citation["link"], # чтобы понимать откуда берутся Цитируемые результаты
                "citation_title": cite_title,
                "citation_snippet": cite_snippet
            })
    return citation_results