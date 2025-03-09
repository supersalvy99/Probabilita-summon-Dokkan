import streamlit as st

def calculate_probability(drop_rate, summons):
    """Calcola la probabilità di ottenere almeno una copia del personaggio."""
    p = drop_rate 
    probability = 1 - (1 - p*0.005) ** (10*summons)
    return probability * 100  # Converti in percentuale

# Interfaccia grafica con Streamlit
st.title("Calcolatore Probabilità Dokkan Battle 🎲 by superbernoulli99")
st.write("Inserisci il numero di pg banner che cerchi e il numero di multi che vuoi fare")

drop_rate = st.number_input("Numero di pg banner che cerchi", min_value=1, max_value=10, value=1, step=1)
summons = st.number_input("Numero di multi che farai", min_value=1, value=1, step=1)

if st.button("Calcola"):
    result = calculate_probability(drop_rate, summons)
    st.success(f"Probabilità di ottenere almeno uno dei pg banner che cerchi: {result:.5f}%")
