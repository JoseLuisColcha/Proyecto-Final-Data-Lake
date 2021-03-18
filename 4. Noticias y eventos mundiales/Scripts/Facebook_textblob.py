import pandas
from textblob import TextBlob
import seaborn as sns
#%
   
df = pandas.read_csv('bbc_news_mundo.csv') 
  
a = list(df['texto']) 
  
b = ' '.join(str(e) for e in a) 
  
  
#%
texto=b.split('\n\n')
      
list_palabras=[]

for index in range(len(texto)):
    if index == 0:
        list_palabras.append(texto[index])
    else:
        try:
            list_palabras.append(texto[index].split('\n')[1])
        except:
            list_palabras.append(texto[index])
        
#%
df = pandas.DataFrame(columns=['texto', 'polaridad'])
df['texto'] = list_palabras
df['polaridad'] = ['' for _ in range(len(df))]
    
    
#%%
for i in range(len(df)):
    if TextBlob(df.at[i, 'texto']).sentiment.polarity < 0:
        df.at[i, 'polaridad'] = "Negativo"
    elif TextBlob(df.at[i, 'texto']).sentiment.polarity > 0:
        df.at[i, 'polaridad'] = "Positivo"
    else:
        df.at[i, 'polaridad'] = "Neutral"
    
    
#%%
df.to_csv('bbc_news_mundo_polaridad.csv')
