import streamlit as st
import matplotlib.pyplot as plt

# Set the page title and header
st.title("Reserva de Salones CESDE")
st.header("Bienvenido al sistema de reserva de salones")

# Hero Section with image and project description
st.image('static/datasets/reserva.png')
st.write("**Descripción del proyecto:** Plataforma para que los estudiantes del CESDE reserven computadores en los salones de estudio.")

# Project Overview
st.subheader("Resumen del Proyecto")
st.write("- **Facilidad de Uso:** Sistema intuitivo y fácil de usar para todos los estudiantes.")
st.write("- **Acceso Rápido:** Reserva rápida y eficiente de computadores en los salones.")
st.write("- **Optimización del Espacio:** Asegura una mejor distribución y uso de los recursos.")

# Features and Benefits
st.subheader("Características y Beneficios")
st.write("**Reserva en Línea:** Reserva computadores desde cualquier lugar y en cualquier momento.")
st.write("**Historial de Reservas:** Accede a tu historial de reservas y gestiona tus próximas citas.")

# Interactive Chart or Visualization (Optional)
# Replace with your specific data and visualization
data = [25, 35, 20, 10, 10]
labels = ["Reservas Completadas", "Reservas Pendientes", "Computadores Disponibles", "Computadores en Mantenimiento", "Computadores No Disponibles"]
fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct="%1.1f%%")
st.pyplot(fig)

# Call to Action
st.subheader("¡Reserva Ahora!")
st.write("**Visite nuestro sitio web:** [Enlace al sitio web del proyecto](https://www.cesde.edu.co/)")


# Footer with team members and project information
st.subheader("Equipo y Contacto")
st.write("**Miembros del equipo:**")
st.write("- Nombre 1: Coordinador del Proyecto.")
st.write("- Nombre 2: Desarrollador Principal.")
st.write("- Nombre 3: Soporte Técnico.")
st.write("**Información de contacto:**")

