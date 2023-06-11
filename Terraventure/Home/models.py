from django.db import models


# Create your models here.  
class Result(models.Model):
    rank = models.IntegerField(default=None)
    title = models.TextField(max_length=1000, default='')
    link = models.TextField(unique=True, default='')
    displayLink = models.TextField(default='')
    htmlSnippet = models.TextField(default='')
    created = models.DateTimeField(default=None)

    def __str__(self):
        return self.title

    # def insert_into_table(row):
    #     rank = row['rank']
    #     title = row['title']
    #     link = row['link']
    #     displayLink = row['displayLink']
    #     htmlSnippet = row['htmlSnippet']
    #     created = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    # # Assuming you have a Django model named YourModel and its corresponding fields

    #     instance = YourModel(rank=rank, title=title, link=link,
    #                      displayLink=displayLink, htmlSnippet=htmlSnippet, created=created)
    #     instance.save()

    # def fetch_values_from_table_if_present(self, query):
    #     try:
    #         row = Result.objects.filter(title__contains=query)
    #     except:
    #         return None
    #     return row
