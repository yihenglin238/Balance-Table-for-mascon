import pandas as pd
table_mascon = pd.read_excel("Mascon Data.xlsx", header = 1)
table_cust = pd.read_excel("Customer Data.xlsx", header = 1)

table_mascon = table_mascon[['Item', 'CustPO', 'OpenQty']]
table_cust = table_cust[['Part Number', 'Order No.', 'Order Quantity']]


table_cust = table_cust.rename(columns = {"Part Number" : "Item"})
#table_cust = table_cust.rename(columns = {"Order Quantity" : "OpenQty"})

table_mascon_uni = table_mascon
table_cust_uni = table_cust


table_mascon_uni = table_mascon_uni.groupby("Item")["OpenQty"].sum().to_frame('OpenQty').reset_index()
table_mascon_uni = table_mascon_uni.rename(columns = {'index':'Item'}).reset_index(drop=True)
table_cust_uni = table_cust_uni.groupby("Item")["Order Quantity"].sum().to_frame('Order Quantity').reset_index()
table_cust_uni = table_cust_uni.rename(columns = {'index':'Item'}).reset_index(drop=True)

table_combined = table_mascon_uni.merge(table_cust_uni,
                                        on = ['Item'],
                                        how = "outer")
unmatched = table_combined[table_combined['OpenQty'] != table_combined['Order Quantity']].reset_index(drop=True)
unmatched = unmatched.reset_index(drop=True)
table_mascon_uni = table_mascon_uni.rename(columns = {'index':'i'}).reset_index(drop=True)

unmatched = unmatched[['Item', 'OpenQty', 'Order Quantity']]
print(unmatched)
unmatched.to_csv('balance table.csv')
