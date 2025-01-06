# import streamlit as st
# import pandas as pd
# from sklearn.datasets import load_iris
# from sklearn.ensemble import RandomForestClassifier

# @st.cache_data
# def load_data():
#     iris = load_iris()
#     df = pd.DataFrame(iris.data, columns = iris.feature_names)
#     df['species'] = iris.target
#     return df , iris.target_names

# df , target_names = load_data()

# model = RandomForestClassifier()
# model.fit(df.iloc[:, :-1], df.iloc[:, -1])


# #sidebar
# st.title('Iris Flower Prediction App')
# sepal_length = st.slider('Sepal Length', float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
# sepal_width = st.slider('Sepal Width', float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
# petal_length = st.slider('Petal Length', float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
# petal_width = st.slider('Petal Width', float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

# input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# #prediction
# prediction = model.predict(input_data)
# predicted_species = target_names[prediction][0]


# #prediction species
# st.write(f'The predicted species is {predicted_species}')  # Output: The predicted species is
                        
                        