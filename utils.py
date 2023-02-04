import json


def write_csv(df,name,index=False):
    df.to_csv(name+'.csv', sep = ',', encoding='utf-8',index=index)

def print_json(object,name):      
    with open(name+'.json','w') as f:
        json.dump(object,f)
