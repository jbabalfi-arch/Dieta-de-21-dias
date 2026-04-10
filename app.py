import streamlit as st

st.set_page_config(page_title="Desafío 21 Días", page_icon="🍏")

st.title("🍏 Desafío 21 Días: Sin Harinas ni Azúcares")
st.write("Basado en el plan de Maria Eugenia Zini López")

nivel = st.sidebar.selectbox("Selecciona tu Nivel:", ["Principiante (Nivel 1)", "Intermedio (Nivel 2)", "Avanzado (Nivel 3)"])

if nivel == "Principiante (Nivel 1)":
    st.header("Nivel 1: Sin harinas refinadas ni azúcares")
    st.subheader("🚫 No Permitidos")
    st.write("- Pan, galletas, pastas, pizzas, harinas de trigo/maíz/arroz, dulces y gaseosas.")
    st.subheader("✅ Permitidos")
    st.write("- Carnes, huevos, semillas, frutos secos y vegetales de hoja verde.")

elif nivel == "Intermedio (Nivel 2)":
    st.header("Nivel 2: Sin harinas, azúcares ni almidones")
    st.subheader("🚫 No Permitidos")
    st.write("- Todo lo del Nivel 1 + Tubérculos (papa, batata), legumbres y frutas como banana.")
    st.subheader("✅ Permitidos")
    st.write("- Carnes, huevos, frutos secos y vegetales bajos en almidón.")

else:
    st.header("Nivel 3: Avanzado")
    st.subheader("🔥 Restricción Máxima")
    st.write("- Sin harinas, sin azúcares, sin almidones y muy poca fructosa.")
    st.subheader("🍓 Frutas Permitidas (Moderadas)")
    st.write("- Frutillas, frambuesas, moras (2 veces por semana), palta, limón y coco.")

st.divider()
st.subheader("🛒 Tip de Compra")
st.info("La base de tu alimentación será: Carnes, Huevos y Vegetales de hoja verde.")
