
import pandas as pd
import numpy as np
import pygsheets


gc = pygsheets.authorize(client_secret='creds.json') 

sh = gc.open('Retos')
wks = sh.worksheet_by_title('Reto1')



sheet_id = "1DRD97TAw2WIuTCG0Nh6BW-aVvDKAgY1wvJb38V-3vU8"
sheet_name = "Reto1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url)
df['value'] = df['Sentiment']
df = df.drop_duplicates()



dfres =df.pivot_table(index=['Author','Sentiment'], columns=['Country'] ,values="value" , aggfunc=lambda x: np.logical_or(x == 'Neutral',np.logical_or(x == 'Positive', x == 'Negative')) ).fillna(False)

dfres1 =df.pivot_table(index=['Author','Sentiment'], columns=['Theme'] ,values="value" , aggfunc=lambda x: np.logical_or(x == 'Neutral',np.logical_or(x == 'Positive', x == 'Negative'))).fillna(False)


index_country = []
for i in dfres.columns:
    index_country.append("Country")
col = pd.MultiIndex.from_arrays([index_country,
                                    dfres.columns])
dfres.columns = col   

index_theme = []
for i in dfres1.columns:
    index_theme.append("Theme")


col = pd.MultiIndex.from_arrays([index_theme,
                                    dfres1.columns])
dfres1.columns = col                     
print(dfres)
df_left = pd.merge(dfres, dfres1, on=['Author','Sentiment'], how='right')

wks.set_dataframe(df_left,(1,1),copy_index=True, copy_head=True, extend=True, fit=False, escape_formulae=False)

writer = pd.ExcelWriter('output.xlsx')
# write dataframe to excel
df_left.to_excel(writer)
# save the excel
writer.save()

