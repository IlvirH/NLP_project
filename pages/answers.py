import random
import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from streamlit_extras.let_it_rain import rain

rain(
    emoji="❔",
    font_size=54,
    falling_speed=5,
    animation_length="infinite",
)

model_name = "deepset/roberta-base-squad2"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

pairs = [
    {
        'context': "In recent years, climate change has become a pressing global issue. Rising temperatures, melting ice caps, and extreme weather events are all indicators of the changing climate. Governments around the world are implementing measures to reduce carbon emissions and promote renewable energy sources. The Paris Agreement, signed in 2015, aims to limit global warming to well below 2 degrees Celsius. Despite these efforts, challenges remain in achieving sustainable development while mitigating climate change.",
        'question': "What are some measures governments are taking to address climate change?"
    },
    {
        'context': "The field of artificial intelligence (AI) has seen significant advancements in recent years. Machine learning algorithms are being used to develop intelligent systems capable of performing complex tasks. From autonomous vehicles to virtual assistants, AI is transforming various industries. However, ethical concerns arise with AI, such as bias in algorithms and potential job displacement. It is essential to strike a balance between technological progress and ethical considerations.",
        'question': "What are some ethical concerns associated with artificial intelligence?"
    },
    {
        'context': "The COVID-19 pandemic has had a profound impact on societies worldwide. Governments implemented lockdowns, travel restrictions, and social distancing measures to curb the spread of the virus. The pandemic also highlighted the importance of healthcare systems and the need for global cooperation in addressing public health crises. Vaccination campaigns have played a crucial role in controlling the virus, but equitable access to vaccines remains a challenge.",
        'question': "How did the COVID-19 pandemic impact healthcare systems?"
    },
    {
        'context': "The advent of the internet revolutionized communication and information sharing. Today, social media platforms have become essential tools for connecting people and disseminating news. However, concerns over privacy and the spread of misinformation have emerged. Cybersecurity measures and fact-checking initiatives are being implemented to address these challenges and ensure a safe online environment.",
        'question': "What are some measures to combat the spread of misinformation on social media?"
    },
    {
        'context': "The world's population is projected to reach 9.7 billion by 2050. This rapid population growth poses significant challenges, including food security, resource scarcity, and urbanization. Sustainable agricultural practices, renewable energy sources, and smart city solutions are being explored to mitigate the impact of population growth and create a more sustainable future.",
        'question': "How can sustainable agricultural practices help address the challenges of population growth?"
    },
    {
        'context': "The exploration of space has captivated human curiosity for centuries. In recent decades, significant milestones have been achieved, including the moon landing and the establishment of the International Space Station. Space agencies and private companies are working together to advance space exploration and pave the way for future human missions to Mars and beyond.",
        'question': "What are some recent milestones in space exploration?"
    },
    {
        'context': "Education plays a vital role in personal and societal development. Traditional classrooms are evolving with the integration of technology, online learning platforms, and personalized teaching methods. The COVID-19 pandemic accelerated the adoption of remote learning, highlighting both the opportunities and challenges of digital education.",
        'question': "How has the COVID-19 pandemic impacted education?"
    },
    {
        'context': "Renewable energy sources, such as solar and wind power, are gaining prominence as alternatives to fossil fuels. The transition to clean energy is driven by the need to reduce greenhouse gas emissions and combat climate change. Investments in renewable energy infrastructure and advancements in energy storage technologies are key drivers of this transition.",
        'question': "What are some advantages of renewable energy sources?"
    }
]


def get_answer(context, question):
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    QA_input = {'question': question, 'context': context}
    res = nlp(QA_input)
    answer = res['answer']
    return answer


def main():
    st.title("Question Answering App :robot_face:")
    st.divider()
    st.markdown("### **Enter the context and question, then click on ':blue[Get Answer]' to retrieve the answer:**")

    context = st.text_area("**:blue[Context]**", "Enter the context here...")
    question = st.text_input("**:blue[Question]**", "Enter the question here...")

    if st.button(":blue[**Get Answer**]"):
        if context.strip() == "" or question.strip() == "":
            st.warning("Please enter the context and question.")
        else:
            answer = get_answer(context, question)
            st.success(f"Answer: {answer}")

    if st.button(":blue[**Random Example**]"):
        pair = random.choice(pairs)
        context = pair['context']
        question = pair['question']
        st.text_area(":blue[**Context**]", value=context)
        st.text_input(":blue[**Question**]", value=question)


if __name__ == "__main__":
    main()