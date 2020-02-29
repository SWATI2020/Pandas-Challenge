#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import pandas as pd

# File to Load 
file_to_load = "Codingbootcamp/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[2]:


# Total number of players
Total_players = len(purchase_data["SN"].unique())
df = pd.DataFrame({Total_players})
df


# In[12]:


# Purchasing Analysis
Number_of_unique_items = len(purchase_data["Item ID"].unique()) # Number of unique items
Average_Price = purchase_data["Price"].mean() # Average price
Number_of_purchases = len(purchase_data["Purchase ID"]) # Number of purchases
Total_Revenue = purchase_data["Price"].sum() # Total Revenue

# Display summary data frame
Summary = pd.DataFrame({"Number of Unique Items":[Number_of_unique_items],"Average Price":[Average_Price],"Number of Purchases":[Number_of_purchases],"Total_Revenue":[Total_Revenue]})
Summary


# In[13]:


# Gender Demographics

#Grouping the data by gender
group = purchase_data.groupby(["Gender"])

#Calculating the values for summary
Person_Count = group["SN"].nunique() # Number of unique persons
percentage_Count = group["SN"].nunique()/len(purchase_data["SN"].unique())*100 # percentage of unique persons

#Create dataframe for demographics summary
Demographics_Summary = pd.DataFrame({"Total Count":Person_Count,"Percentage of Players":percentage_Count})
Demographics_Summary["Percentage of Players"] = Demographics_Summary["Percentage of Players"].map("{:.2f}%".format)

Demographics_Summary


# In[14]:


#Purchasing Analysis (Gender)

#Grouping the dataframe by gender
group = purchase_data.groupby(["Gender"])

Purchase_Count = group["Purchase ID"].count() #Purchase count
Total_Purchase_Price = group["Price"].sum() # Total purchase price
Average_Purchase_Price = Total_Purchase_Price/Purchase_Count # Average purchase price
Average_Purchase_Person = Total_Purchase_Price/group["SN"].nunique() # Average purchase per person

#Create dataframe for purchasing summary
Purchasing_summary = pd.DataFrame({"Purchase Count":Purchase_Count,"Average Purchase Price":Average_Purchase_Price,"Average_Purchase_Person":Average_Purchase_Person})
Purchasing_summary


# In[24]:


#Age Demographics 
bins = [-1,9, 14, 19, 24, 29, 34, 39,1000]

# Create the names for the four bins30-34
group_names = ["<10", "10-14", "15-19", "20-24", "25-29","30-34","35-39","40+"]

#Categorizing the existing players using the age bins
purchase_data["Age Ranges"] = pd.cut(purchase_data["Age"], bins, labels=group_names)

# Grouping the data by age ranges
group1 = purchase_data.groupby(["Age Ranges"])
age_group_count = group1["Purchase ID"].count() #numbers by age group
age_avrg_purchase_price = group1["Price"].mean() #Average purchase price by age group
age_total_purchase = group1["Price"].sum() #Total purchase price by age group
age_average_price_person = group1["Price"].sum()/group1["SN"].nunique() #Average purchase price per person in age group

# Create dataframe to display age demographics
Age_demographics_summary = pd.DataFrame({"Purchase Count":age_group_count,"Average Purchase Price":age_avrg_purchase_price,"Total Purchase Value":age_total_purchase,"Avg Total Purchase per Person":age_average_price_person})

#Formatting the values of Average Purchase Price ,Total Purchase Value and Avg Total Purchase per Person
Age_demographics_summary["Average Purchase Price"] = Age_demographics_summary["Average Purchase Price"].map("${:.2f}".format)
Age_demographics_summary["Total Purchase Value"] = Age_demographics_summary["Total Purchase Value"].map("${:.2f}".format)
Age_demographics_summary["Avg Total Purchase per Person"] = Age_demographics_summary["Avg Total Purchase per Person"].map("${:.2f}".format)

#Summary of age demographics
Age_demographics_summary


# In[169]:


# Top spenders
group2 = purchase_data.groupby(["SN"])
Top_Spenders_purchase = group2["Price"].sum()
Top_Spenders_count = group2["Purchase ID"].count()
Top_Spenders_Average = group2["Price"].mean()

Top_spender_Summary = pd.DataFrame({"Purchase Count":Top_Spenders_count,"Average Purchase Price":Top_Spenders_Average,"Total Purchase Value":Top_Spenders_purchase})
#Top_spender_Summary["Total Purchase Value"] = Top_spender_Summary["Total Purchase Value"].map("${:.2f}".format)
Top_spender_Summary["Average Purchase Price"] = Top_spender_Summary["Average Purchase Price"].map("${:.2f}".format)
Top_spender_Summary.sort_values("Total Purchase Value",ascending = False).head()


# In[185]:


#Most Popular Items
Purchase_data_popular = purchase_data[["Item ID","Item Name","Price"]]
group_popular = Purchase_data_popular.groupby(["Item ID","Item Name"])

purchase_count = group_popular["Item ID"].count()
purchase_value = group_popular["Price"].sum()
item_price = purchase_value/purchase_count

Most_popular_summary = pd.DataFrame({"Purchase Count":purchase_count,"Item Price":item_price,"Total Purchase Value":purchase_value})
Most_popular_summary["Item Price"] = Most_popular_summary["Item Price"].map("${:.2f}".format)
# Most_popular_summary["Total Purchase Value"] = Most_popular_summary["Total Purchase Value"].map("${:.2f}".format)
Most_popular_summary.sort_values("Purchase Count",ascending = False).head()


# In[188]:


#Most Profitable Items

Most_popular_summary.sort_values("Total Purchase Value",ascending = False).head()


# In[ ]:




