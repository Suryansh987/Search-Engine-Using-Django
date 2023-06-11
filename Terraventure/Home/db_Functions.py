from Home.models import Result
from datetime import datetime
from django.db import IntegrityError
from django.db.models import Q

def insert_into_table(row):
        rank = row['rank']
        title = row['title']
        link = row['link']
        displayLink = row['displayLink']
        htmlSnippet = row['htmlSnippet']
        created = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    # Assuming you have a Django model named YourModel and its corresponding fields
        try:
            db = Result(rank=rank, title=title, link=link,displayLink=displayLink, htmlSnippet=htmlSnippet, created=created)
            db.save()
        except IntegrityError as e:
            pass
    

# def fetch_values_from_table_if_present(query):
#     try:
#         row = Result.objects.filter(Q(link__icontains=query) or Q(title__icontains=query)).order_by('rank')
#     except:
#         return None
#     return row

# def fetch_values_from_table_for_genral_terms(query):
#     html_snippet_list=Q()
#     html_snippet_list = Q(htmlSnippet__contains=query[0])
#     for value in range(1,len(query)):
#         html_snippet_list &= Q(htmlSnippet__contains=query[value])
#     try:
#         # print(html_snippet_list)
#         row = Result.objects.filter(html_snippet_list)
#     except:
#         return None
#     return row

def fetch_values_from_table_for_genral_terms(query):
    query_filters = Q()

    # Specify the columns to search in
    columns = ['title', 'htmlSnippet', 'displayLink']

    for column in columns:
        query_filters |= Q(**{f'{column}__contains': query})

    results = Result.objects.filter(query_filters).distinct()
    return results
