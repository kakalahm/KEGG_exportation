from bs4 import BeautifulSoup
import pandas as pd

with open("C:\LULU\KEGG\standard_html.txt", "r") as f:
    doc_txt = f.read().replace("\n", "")
soup = BeautifulSoup(doc_txt,'lxml')
level_groups = soup.find_all('b')
# print(level_groups)
obser = {'level1':[],'level2':[],'level3':[],'genes':[]}
for level1_group in level_groups:
    level1_name = level1_group.string.strip()
    level2_groups = level1_group.next_sibling.next_sibling
    level2_uls = level2_groups.find_all('ul')

    for ul in level2_uls:
        level2_name = ul.previous_sibling.string.strip()
        # print("\t level2: {}".format(level2_name))

        # print(level2_name)
        for li in ul.find_all('li'):
            level3_name = li.a.string.strip()
            # print(level3_name)
            # exit()
            gene_nodes = li.div.find_all('a')
            # print("\t\t level3: {}".format(level3_name))

            for gene_node in gene_nodes:
                gene = gene_node.next_sibling.next_sibling.next_sibling.string.strip()
                obser['level1'].append(level1_name)
                obser['level2'].append(level2_name)
                obser['level3'].append(level3_name)
                obser['genes'].append(gene)
                # print("\t\t\t level4: {}".format(gene))
                # pass
df = pd.DataFrame(obser)
df2 = df.groupby(['level1','level2','level3']).count()
df["genes"] += "; "
df3 = df.groupby(['level1','level2','level3']).sum()
df3['gene_counts'] = df2['genes']
df3.to_csv("C:\LULU\KEGG\df3.csv",sep='\t')






