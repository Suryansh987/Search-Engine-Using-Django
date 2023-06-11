from html import escape
from django.db.models.query import QuerySet

result_template='''
<p class="site">{rank}: {displayLink}</p>
<a href="{link}" class="title">{title}</a>
<p class="snippet">{snippet}</p>
'''

def parse_checker(res_df):
    result=""
    if isinstance(res_df, QuerySet):
        result=display(res_df)
    else: 
        # print(res_df)
        # result+=res_df.apply(lambda x:show(x),axis=1)
        # print(result.to_string)
        # print(res_df.loc[1,'title'])
        result = show(res_df)
    return result


#for db type object(QUERYSET)
def display(res_df):
    result=""
    i=1
    global result_template
    for data in res_df:
        result += result_template.format(rank=i,displayLink=data.displayLink,link=data.link,title=data.title,snippet=data.htmlSnippet)
        i+=1
        # print(result)
    return result


#for dataframe object
def show(res_df):
    result=""
    global result_template
    i=1
    for index in range(0,res_df.shape[0]):
        result += result_template.format(rank=i,displayLink=res_df.loc[index,'displayLink'],link=res_df.loc[index,'link'],title=res_df.loc[index,'title'],snippet=res_df.loc[index,'htmlSnippet'])
        i+=1
    return result
    # result=""
    # global result_template
    # i=1
    # result += result_template.format(rank=i,displayLink=res_df[3],link=res_df[2],title=res_df[1],snippet=res_df[4])
    # i+=1
    # return result
