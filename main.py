import streamlit as st

# Título del cuestionario
st.image("logo.jpeg")
st.subheader("¿Qué tan woke eres?")

# Inicializar una variable para sumar los resultados
total_score = 0

# Crear los sliders para las 10 preguntas (1 al 10)
total_score += st.slider("El lenguaje inclusivo es importante para avanzar hacia una sociedad más igualitaria.", 1, 10, 5)
total_score += st.slider("Es necesario cuestionar y modificar las tradiciones que perpetúan desigualdades.", 1, 10, 5)
total_score += st.slider("El cambio climático es la crisis más urgente que enfrenta nuestra generación.", 1, 10, 5)
total_score += st.slider("Las empresas deben ser responsables por los impactos sociales y ambientales de sus productos.", 1, 10, 5)
total_score += st.slider("El activismo en redes sociales es una forma efectiva de generar cambios.", 1, 10, 5)
total_score += st.slider("Deberían existir más leyes para asegurar la equidad de género y racial en el trabajo.", 1, 10, 5)
total_score += st.slider("Es importante ser consciente de los privilegios propios para ser parte de la solución.", 1, 10, 5)
total_score += st.slider("La cultura de la cancelación es una herramienta necesaria para responsabilizar a quienes actúan mal.", 1, 10, 5)
total_score += st.slider("La justicia social debe estar en el centro de las políticas públicas.", 1, 10, 5)
total_score += st.slider("El respeto por las diferentes identidades de género es fundamental para una sociedad justa.", 1, 10, 5)

# Crear un botón para ver los resultados
if st.button('Ver resultados'):
    # Mostrar globos
    st.balloons()

    # Calcular el resultado final
    st.write("Tu puntaje final es:", total_score)

    # Mostrar resultado usando st.success
    if total_score <= 30:
        st.success("**Boomer Alert!** Parece que aún no estás muy convencido del discurso woke.")
    elif total_score <= 70:
        st.success("**Moderado.** Estás en el medio del debate, ni muy woke ni demasiado tradicional.")
    else:
        st.success("**Super Woke!** Tu mentalidad está alineada con los valores progresistas actuales.")
