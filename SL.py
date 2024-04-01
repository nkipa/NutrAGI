import streamlit as st
import pandas as pd


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('MVP_NUTRITION_4_1_2024.csv',on_bad_lines='skip',low_memory=False)

df.index = range(1,len(df)+1)
st.set_page_config(
   page_title="NutrAGI - Nutritional Assistant",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)


st.title("NutrAGI - Nutritional Assistant")
st.subheader ("Meal Suggestion and Traking App")
#x = st.number_input ("Food Number [1-1500]",max_value=1500, min_value=0)


col1,col2,col3,col4=st.columns(4)
col11,col12,col13,col14=st.columns(4)



#st.write(f'Food {x}')

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
df.columns = df.columns.str.replace('_', ' ')
df.rename(columns={"R": "Restaurant", "M": "Supermarket", "H": "Home", "P": "Preferred", "I": "Indifferent", "K": "Avoid", "Q":"Quantity","C": "Cost"},inplace=True)
df.columns=df.columns.str.capitalize()


#dfq=df.loc[(df["Name"] == f"Food {x}")]

#sol=dfq.loc[:, ~(dfq == 0).all()].T
#sol['Total'] = sol.iloc[2::].sum(axis = 1)
#sol['Total'] = sol['Total'].fillna('')
#st.write(sol)

#st.line_chart(sol)
with col1:
    meal = st.radio(
        "Choose meal type",
        ["Breakfast", "Morning Snack", "Lunch", "Afternoon Snack","Dinner", "Evening Snack", "Other"]
    )
    meal=meal.replace('Morning Snack',"Snack")
    meal=meal.replace('Afternoon Snack',"Snack")
    meal=meal.replace('Evening Snack',"Snack")

with col11:
    st.write("You selected:",meal)
with col2:
    location = st.radio(
        "Location of the meal",
        ['Restaurant', 'Supermarket','Home','Other']
)
with col12:    
    st.write("Your location is:", location)
with col3:
    preference = st.radio(
        'Select the level of likeness of food',
        ['Preferred', 'Indifferent','Avoid','Other']
        
)
with col13:
    st.write('You selected:', preference)

dfsol=df[(df[meal]==1)&(df[location]==1)&(df[preference]==1)]
with st.expander("Food List available for your choise"):
    st.dataframe(dfsol)

list=list(dfsol.Name)
#dfsol
with col4:
    y = st.multiselect (
        "Food Selector (Select Food Number from dropDown Menu)",
        list                   
    )

#st.write('You selected:', y)
#df1=dfsol.loc[(dfsol["Name"] == y)]

    sol=dfsol[dfsol["Name"].isin(y)].T
cola,col1b=st.columns(2)

with cola:
    #sol=df1.loc[:, ~(df1 == 0).all()].T
    sol['Total'] = sol.iloc[2::].sum(axis = 1)
    #sol['Total'] = sol['Total'].fillna('')
    sol=sol.loc[['Name', 'Breakfast', 'Snack', 'Restaurant', 'Supermarket', 'Cost',
              'Serving size', 'Quantity', 'Calories', 'Fat','Total fat', 'Saturated fat',
                'Cholesterol', 'Sodium', 'Choline', 'Folate', 'Niacin', 'Pantothenic acid'
                , 'Riboflavin', 'Thiamin', 'Carotene alpha', 'Vitamin b12', 'Vitamin b6', 
                'Vitamin c', 'Vitamin d', 'Vitamin e', 'Vitamin k', 'Calcium', 'Copper', 
                'Iron', 'Magnesium', 'Manganese', 'Phosphorous', 'Potassium', 'Selenium', 
                'Zink', 'Protein', 'Carbohydrate', 'Fiber', 'Glucose', 'Sucrose',
                  'Alcohol', 'Ash', 'Water']]
    with st.expander("Food Consumed"):
            st.dataframe(sol)
#  
#sol.Total
#sol.Total = pd.to_numeric(sol.Total, errors='coerce')
#sol.Total = sol.Total.map('{:.3f}'.format)
#st.dataframe(data=None, width=None, height=None, use_container_width=True, hide_index=None, column_order=None, column_config=None)
#sol

#st.write(f'Food {y}')

#dfq=df.loc[(df["Name"] == f"Food {x}")]

#sol=dfq.loc[:, ~(dfq == 0).all()].T
#sol['Total'] = sol.iloc[2::].sum(axis = 1)
#sol['Total'] = sol['Total'].fillna('')
#st.write(sol)
