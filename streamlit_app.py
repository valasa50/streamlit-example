import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorite')
streamlit.text('\N{flexed biceps} Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{flexed biceps} Kale, Spinach & Rocket Smoothie')
streamlit.text('\N{flexed biceps} Hard-Boiled Free-Range Egg')
streamlit.text('\N{flexed biceps} Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')
import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
# Display the table on the page
streamlit.dataframe(my_fruit_list)
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
#new section to desplay Fuitverse api responce
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response.json())
# Convert from json to normelize  
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output as table
#streamlit.dataframe(fruityvice_normalized)
#streamlit.header('Fruityvice Fruit Advice!') import requests
import requests
fruit_choice = streamlit.text_input('What fruit would you like information about?','apple')
streamlit.write('The user entered ', fruit_choice)
fruityvice_repsonse = requests.get("https://fruityvice.com/api/fruit/"+"apple")
fruityvice_normalized = pandas.json_normalize(fruityvice_repsonse.json())
streamlit.dataframe(fruityvice_normalized)
import snowflake.connector
