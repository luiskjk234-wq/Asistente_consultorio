
import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title = "Asistente Médico",page_icon= "")

def frases_bienvenida():

    frases = [

        f"Bienvenido al Asistente. Atenderemos cualquier duda que tenga",
        f"¡Hola! Bienvenido a nuestro asistente. Donde podrá consultar cualquier información que desee",
        f"Sea bienvenido al asistente por excelencia. Nosostros nos encargaremos de todo"
    ]
    return random.choice(frases)

def mostrar_titulo():
    st.title("Torre Médica H | Demo creada por Axelbot")
    st.markdown(f"🕒 Sesión Iniciada: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    st.markdown(f"📍 Ubicación : Ciudad de México")
    st.markdown(f"💬 {frases_bienvenida()}")

def capturar_mensaje():

    mensaje = st.text_input("Escribe tu consulta aquí: ").lower()
    return mensaje

def responder_mensaje(mensaje):

    if "cita" in mensaje:
        st.success("✅ Dermatología disponible: Lunes a viernes, 9am a 5pm")
    elif "especialidades" in mensaje:
        st.success("🩺 Contamos con: Cardiología, Cosmiatría, Cirugía general")
    elif "ubicación" in mensaje:
        st.info("📍 Av. Río consulado, CDMX")
    elif "contacto" in mensaje:
        st.info("📞 Whatsapp: +52 55 1234 5678 | Tel: 55 8765 4321")
    else:
        st.warning("🤖 Lo siento, no entendí el mensaje. ¿Puedes repetirlo?")


def mensaje_demo():

    st.markdown("---")
    st.markdown("Está es una demo. La versión premium incluye integración con Whatsapp, panel de control y soporte técnico")
    st.markdown("© 2025 AxelBot. Prohibida su reproducción sin autorización.")

def ejecutar():
    mostrar_titulo()
    mensaje = capturar_mensaje()
    if mensaje:
        responder_mensaje(mensaje)
        mensaje_demo()