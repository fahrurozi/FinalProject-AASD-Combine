import pandas

_items_df = pandas.read_csv('items.csv')

# Use this graph_dict variable
graph_dict = dict()

COLUMNS = {'Nama', 'Harga', 'Kategori', 'Merk', 'Nominal'}
list_product = []

for column in COLUMNS:
    for index, row in _items_df.iterrows():
        # print(row['Nama'], "============")
        if column == 'Nama':
            graph_dict['Nama-' + row['Nama']] = {
                'Harga-' + row['Harga'],
                'Kategori-' + row['Kategori'],
                'Merk-' + row['Merk'],
            }
            list_product.append([row['Nama'],row['Nominal']])
        elif column == "Nominal":
            continue
        else:
            try:
                graph_dict[f'{column}-' + row[column]].add(
                    'Nama-' + row['Nama']
                )
            except KeyError:
                graph_dict[f'{column}-' + row[column]] = {
                    'Nama-' + row['Nama'],
                }





if __name__ == '__main__':
    from pprint import pprint
    pprint(graph_dict)
    # print(list_product)    
