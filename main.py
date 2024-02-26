import modulos.gestoralumnos as st

if __name__ == '__main__':
    alumnos = {}

    st.AddStudent(alumnos)
    st.AddGrades(alumnos)
    st.ListData(alumnos)
    st.os.system('pause')

    st.AddStudent(alumnos)
    st.AddGrades(alumnos)
    st.ListData(alumnos)
    st.os.system('pause')

    st.SearchStudent(alumnos)

    st.DelStudent(alumnos)
    st.DelByName(alumnos)

    st.ListData(alumnos)
    st.os('pause')