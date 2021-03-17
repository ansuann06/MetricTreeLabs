import pandas as pd

"""Out Put Display Setting """
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)

data = pd.read_excel("D:\office\office/bill\Data Science Question.xlsx", skiprows=5)
data['PERIOD'] = pd.to_datetime(data['PERIOD'])
data['Year'] = data['PERIOD'].dt.year
data['sum VOL_SQCM'] = data.groupby(['PUBLICATION', 'Year'])['VOL_SQCM'].transform('sum')
player1 = data[data['PUBLICATION'] == 'PLAYER 1']
player1_sum = player1[['Year', 'PUBLICATION', 'sum VOL_SQCM']].drop_duplicates()
player2 = data[data['PUBLICATION'] == 'PLAYER 2']
player2_sum = player2[['Year', 'PUBLICATION', 'sum VOL_SQCM']].drop_duplicates()

per_player1 = player1[['PUBLICATION', 'SUPER CATEGORY', 'ADVERTISER', 'AD TYPE(CLR/BW)', 'VOL_SQCM', 'Year']]
per_player1['sum VOL_SQCM'] = per_player1.groupby(['PUBLICATION', 'SUPER CATEGORY', 'ADVERTISER',
                                                   'AD TYPE(CLR/BW)'])['VOL_SQCM'].transform('sum')
per_player1.drop_duplicates(subset={'PUBLICATION', 'SUPER CATEGORY', 'ADVERTISER',
                                                   'AD TYPE(CLR/BW)',  'sum VOL_SQCM'}, inplace=True)

per_player1.sort_values(by=['sum VOL_SQCM'], ascending=[False], inplace=True)
print(per_player1[['SUPER CATEGORY', 'ADVERTISER', 'sum VOL_SQCM', 'AD TYPE(CLR/BW)']].drop_duplicates()[:50])

per_player2 = player2[['PUBLICATION', 'SUPER CATEGORY', 'ADVERTISER', 'AD TYPE(CLR/BW)', 'VOL_SQCM', 'Year']]
per_player2['sum VOL_SQCM'] = per_player2.groupby(['PUBLICATION', 'SUPER CATEGORY', 'ADVERTISER',
                                                   'AD TYPE(CLR/BW)'])['VOL_SQCM'].transform('sum')
per_player2.drop_duplicates(subset={'PUBLICATION', 'SUPER CATEGORY', 'ADVERTISER',
                                                   'AD TYPE(CLR/BW)',  'sum VOL_SQCM'}, inplace=True)

per_player2.sort_values(by=['sum VOL_SQCM'], ascending=[False], inplace=True)
print(per_player2[['SUPER CATEGORY', 'ADVERTISER', 'sum VOL_SQCM', 'AD TYPE(CLR/BW)']].drop_duplicates()[:50])

yr_per_py1 = player1[['PUBLICATION', 'SUPER CATEGORY', 'ADVERTISER', 'AD TYPE(CLR/BW)', 'VOL_SQCM', 'Year']]

yr_per_py1['sum VOL_SQCM'] = yr_per_py1.groupby([ 'ADVERTISER'])['VOL_SQCM'].transform('sum')
yr_per_py1.sort_values(by=['sum VOL_SQCM',  'ADVERTISER'], ascending=[ False,  True], inplace=True)
print(yr_per_py1[['PUBLICATION','SUPER CATEGORY', 'ADVERTISER', 'sum VOL_SQCM',  'sum VOL_SQCM']].drop_duplicates()[:50])

