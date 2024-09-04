import pandas as pd

sheets_to_read = 'CTAS'
dtFrame_nuevo = pd.read_excel('padron_31_07_2024-copiaDaniCocom.xlsx', sheet_name= sheets_to_read)
dtFrame_original = pd.read_excel('padron_31_07_2024-copiaDaniCocom-copia.xlsx', sheet_name= sheets_to_read)


dtframe_Nuevo_perfiles_sheet = pd.read_excel('padron_31_07_2024-copiaDaniCocom.xlsx', sheet_name= 'PERFILES')



dtframe_Depurados = dtFrame_nuevo[~dtFrame_nuevo['LOGIN'].isin(dtFrame_original['LOGIN'])]

dtFrame_2 = dtframe_Nuevo_perfiles_sheet[~dtframe_Nuevo_perfiles_sheet['LOGIN'].isin(dtFrame_original['LOGIN'])]

# en base estos filtrar los con el original y obtener solo los que tengan ese id

with pd.ExcelWriter('depurados.xlsx') as writer:
            dtframe_Depurados.to_excel(writer, index=False, sheet_name= sheets_to_read)
            dtFrame_2.to_excel(writer, sheet_name= 'PERFILES')




# print(dtFrame_original.columns)
# print(dtFrame_nuevo.columns)


# df_combined_sheets = {}

# for sheets in sheets_to_read:

#     df_combined = pd.concat([dtFrame_original[sheets], dtFrame_nuevo[sheets]])
#     df_combined_new = df_combined.drop_duplicates(subset=['LOGIN'], keep='last')

# df_combined_sheets[sheets] = df_combined_new


# with pd.ExcelWriter('depurados.xlsx') as writer:
#     for sheets_to_read, df in df_combined_sheets.items():
#         df.to_excel(writer, sheet_name= sheets_to_read, index= False);