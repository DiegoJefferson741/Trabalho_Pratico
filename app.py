import pandas as pd
import streamlit as st
#from pycaret.regression import *
import joblib 

# loading the trained model.
model = joblib.load('modelo-final-RF.pkl')

# carregando uma amostra dos dados.
dataset = pd.read_csv('StudentsPerformace.csv') 
#classifier = pickle.load(pickle_in)


# título
st.title("Data App - Predição de Notas")

# subtítulo
st.markdown("Este é um Data App utilizado para exibir a solução de Machine Learning para o problema de predição de notas.")

st.sidebar.subheader("Defina os atributos do aluno para predição de notas.")

# mapeando dados do usuário para cada atributo
gender = st.sidebar.selectbox("Sexo",("Masculino","Feminino"))
#race_ethnicity = st.sidebar.selectbox("Etinia",("group A","group B","group C","group D"))
#parental_level= st.sidebar.selectbox("Estudo",("bachelor degree","some college","master degree","associate degree","high school"))
lunch= st.sidebar.selectbox("Almoco",("standard","free/reduced"))
test_preparation_course = st.sidebar.selectbox("Teste Preparatorio",("none","completed"))

reading_score = st.sidebar.number_input("Nota leitura")
writing_score = st.sidebar.number_input("Nota Escrita")


### transformando o dado de entrada em valor binário ###

### ---------------------- gender  -------------------
gender = 0 if gender == "Feminino" else 1

### ---------------------- race_ethnicity  -------------------
race_ethnicity  = st.sidebar.selectbox("Etinia",(
                            "group A"
                            ,"group B"
                            ,"group C"
                            ,"group D"
                            )
                        )

if race_ethnicity== "group A":
    race_ethnicity = 1
if race_ethnicity == "group B":
    race_ethnicity = 2
if race_ethnicity == "group C":
    race_ethnicity = 3
if race_ethnicity == "group D":
    race_ethnicity = 4
    
### ---------------------- parental_level -------------------

parental_level = st.sidebar.selectbox("Estudo",(
                            "bachelor degree"
                            ,"some college"
                            ,"master degree"
                            ,"associate degree"
                            ,"high school"
                            )
                        )

if parental_level== "bachelor degree":
    parental_level = 1
if parental_level == "some college":
    parental_level = 2
if parental_level == "some college":
    rparental_level = 3
if parental_level == "associate degree":
    parental_level = 4
if parental_level == "high school":
    parental_level = 5
    
### ---------------------- lunch -------------------    

lunch = 1 if lunch == "standard" else 0


### ---------------------- test_preparation_course -------------------  

test_preparation_course = 1 if test_preparation_course == "none" else 0


#Botao de Prediçao
btn_predict = st.sidebar.button("Realizar Predição")

# verifica se o botão foi acionado
if btn_predict:
    #data_teste = pd.DataFrame()
    data_teste = pd.dataset()

    data_teste["gender"] =	[gender]
    data_teste["race_ethnicity"] =	[race_ethnicity]    
    data_teste["parental level"] = [parental_level]
    data_teste["lunch"] = [lunch]	
    data_teste["test preparation course"] = [test_preparation_course]
    data_teste["reading score"] = [reading_score]
    data_teste["writing score"] = [writing_score]

    #imprime os dados de teste    
    print(data_teste)

    #realiza a predição
    result = model.predict(data_teste)
    
    st.subheader("A nota de Matematica é:")
    result = "R$ "+str(round(result[0],2))
    
    st.write(result)


