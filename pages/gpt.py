from transformers import GPT2LMHeadModel, GPT2Tokenizer
import streamlit as st
import torch
import textwrap
import plotly.express as px

from streamlit_extras.let_it_rain import rain

rain(
    emoji="⭐",
    font_size=54,
    falling_speed=5,
    animation_length="infinite",
)

st.header(':green[Text generation by GPT2 model]')

tokenizer = GPT2Tokenizer.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2')
model = GPT2LMHeadModel.from_pretrained(
    'sberbank-ai/rugpt3small_based_on_gpt2',
    output_attentions = False,
    output_hidden_states = False,
)

model.load_state_dict(torch.load('models/model.pt', map_location=torch.device('cpu')))


length = st.sidebar.slider('**Generated sequence length:**', 8, 256, 15)
if length > 100:
    st.warning("This is very hard for me, please have pity on me. Could you lower the value?", icon="🤖")
num_samples = st.sidebar.slider('**Number of generations:**', 1, 10, 1)
if num_samples > 4:
    st.warning("OH MY ..., I have to work late again!!! Could you lower the value?", icon="🤖")
temperature = st.sidebar.slider('**Temperature:**', 0.1, 10.0, 3.0)
if temperature > 6.0:
    st.info('What? You want to get some kind of bullshit as a result? Turn down the temperature', icon="🤖")
top_k = st.sidebar.slider('**Number of most likely generation words:**', 10, 200, 50)
top_p = st.sidebar.slider('**Minimum total probability of top words:**', 0.4, 1.0, 0.9)


prompt = st.text_input('**Enter text 👇:**')
if st.button('**Generate text**'):
    image_container = st.empty()
    image_container.image("pict/wait.jpeg", caption="that's so long!!!", use_column_width=True)
    with torch.inference_mode():
        prompt = tokenizer.encode(prompt, return_tensors='pt')
        out = model.generate(
            input_ids=prompt,
            max_length=length,
            num_beams=8,
            do_sample=True,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            no_repeat_ngram_size=3,
            num_return_sequences=num_samples,
            ).cpu().numpy()
        image_container.empty()
        st.write('**_Результат_** 👇')
        for i, out_ in enumerate(out):
            # audio_file = open('pict/pole-chudes-priz.mp3', 'rb')
            # audio_bytes = audio_file.read()
            # st.audio(audio_bytes, format='audio/mp3')
            
            with st.expander(f'Текст {i+1}:'):
                st.write(textwrap.fill(tokenizer.decode(out_), 100))
                st.image("pict/wow.png")
            





