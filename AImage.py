# crear app para generar imagenes con texto con streamlit
import streamlit as st
from PIL import Image
import io
import os
import warnings
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


st.set_page_config(page_title="AI-tech", layout="wide", page_icon="⚡")


# API key
# To get your API key, visit https://beta.dreamstudio.ai/membership
os.environ['STABILITY_KEY'] = 'sk-cChmyPGSntNExJP1g520x545GOAHvoSoGoSitl6UNkaRsjGj'

stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],
    verbose=True,
)

# the object returned is a python generator
st.title("Generador de Imagenes con Inteligencia Artificial 🪐🚀")
#agregar parrafo
st.write("Esta aplicacion te permite generar imagenes con un texto ingresado por el usuario")
st.write("Nuestra tecnologia cuenta con una poderosa API que te permite crear millones de diseños creativos con texto")

answers = stability_api.generate(
        prompt=st.text_input("Ingrese un texto")
)

def get_image(answers):
    try:
        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    warnings.warn(
                        "Your request activated the API's safety filters and could not be processed."
                        "Please modify the prompt and try again.")
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(io.BytesIO(artifact.binary))
                    st.image(img, use_column_width=True)

    except ValueError:
        st.write("Por favor ingrese un texto")


if st.button("Generar Imagen"):
    #ejecutar get_image
    get_image(answers)

st.write("Artificial intelligence service created by R0sinver Vasquez 👨‍🚀") 


# no guardar cache
st.cache(False)

    



    