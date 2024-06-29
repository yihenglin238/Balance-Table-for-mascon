import pandas as pd
table_mascon = pd.read_excel("Mascon Data.xlsx", header = 1)
table_cust = pd.read_excel("Customer Data.xlsx", header = 1)

table_mascon = table_mascon[['Item', 'OpenQty']]
table_cust = table_cust[['Part Number', 'Order Quantity']]

table_cust = table_cust.rename(columns = {"Part Number" : "Item"})


table_mascon_uni = table_mascon
table_cust_uni = table_cust

table_mascon_uni = table_mascon_uni.groupby("Item").sum().reset_index()
table_cust_uni = table_cust_uni.groupby("Item").sum().reset_index()

table_combined = table_mascon_uni.merge(table_cust_uni,
                                        on = ['Item'],
                                        how = "outer")

unmatched = table_combined[table_combined['OpenQty'] != table_combined['Order Quantity']].reset_index(drop=True)
unmatched = unmatched.reset_index(drop=True)
unmatched = unmatched[['Item', 'OpenQty', 'Order Quantity']]
unmatched = unmatched.fillna(0)
unmatched['Item'] = unmatched['Item'].astype(str)
unmatched = unmatched.groupby("Item").sum().reset_index()
unmatched = unmatched[unmatched['OpenQty'] != unmatched['Order Quantity']].reset_index(drop=True)
print(unmatched)
unmatched.to_csv('balance table.csv')
#table_cust_uni.to_csv('balance table.csv')