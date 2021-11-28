import sqlparse

keywords=["SELECT", 'UPDATE', 'DELETE', 'INSERT INTO', 'FROM', 'INNER JOIN','OUTER JOIN' ,'SET', 'WHERE', 'VALUES', "GROUP BY","ORDER BY" ,"LEFT JOIN", "RIGHT JOIN", "BETWEEN"]

def format_query(query):
    if query[-1]==';': query=query[:-1]
    a = sqlparse.format(query, reindent=True, keyword_case='upper')
    a=a.split('\n')
    di={}
    lastkeyword=None
    for line in a:
        for keyword in keywords:
            if line.startswith(keyword):
                di[keyword]=line[len(keyword)+1:]
                lastkeyword=keyword
            elif line.startswith(" "):
                di[lastkeyword]+=' ' + (line).lstrip()
                break
    for i in di:
        if i=='SELECT':
            k=di[i].split(',')
            for z in range(len(k)):
                if " AS " in k[z]:
                    f=k[z].split(' AS ')[0]
                    if '(' in f:
                        f=f.split('(')
                        f={f[0]:f[1][:-1]}
                    k[z]=f
            di[i]=k
        if i=='FROM':
            k=di[i].lstrip().rstrip()
            if k[0]=='(':
                di[i]=format_query(k[1:-1])
            else:
                di[i]=[di[i]]
        if i.endswith("JOIN"):
            k=di[i]
            f=k.split(' ON ')
            di[i]={f[0]:f[1]}
        if i=="INSERT INTO":
            k=di[i]
            if '(' in k:
                a=k.index('(')
                b=k.index(')')
                di[i]={k[:a-1]: k[a+1:b].split(',')}
            else:
                di[i]=[k]
        if i.endswith(" BY"):
            di[i]=di[i].split(',')
        if i=="BETWEEN":
            di[i]=di[i].split(' AND ')
    return di


