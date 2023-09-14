import streamlit as st
from TodoDAO import TodoDAO

def Etape19():
    print(50*'-')
    print ("")
    print(50*'-')

    st.title('Hello from the other S... treamlit')


    dao = TodoDAO('todos_db.db')

    st.button("Reset", type="primary")
    nom = st.text_input('Nom')

    if st.button('Qui es-tu ?'):
        st.balloons()
        st.snow()
        st.write(f'Bonjour ma {nom}')
    else:
        st.write('Goodbye')
        nom = ''
        st.balloons()
        st.snow()
    
    todos = dao.findAll()
    st.table(data=todos)

if __name__ == "__main__":
    Etape19()