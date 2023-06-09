---
title: NLP Project
emoji: 🐢
colorFrom: pink
colorTo: purple
sdk: streamlit
sdk_version: 1.21.0
app_file: app.py
pinned: false
---

# NLP project

Данный проект является мультистраничным приложением для обработки естественного языка (Natural Language Processing) и был разработан с использованием платформы Hugging Face и фреймворка Streamlit. Проект включал следующих участников: Василий Севостянов, Анна Филина, Ильвир Хасанов, Иван Никифоров и Виктория Князева.
[Ознакомиться можно по ссылке](https://huggingface.co/spaces/vasevooo/NLP_project)


## 1. Классификация отзывов на фильмы на английском языке (Иван Никифоров)

В этой части проекта была разработана система классификации отзывов на фильмы на английском языке. Пользователь может ввести свой отзыв в поле ввода, после чего система предсказывает его класс (позитивный/негативный) с помощью трех моделей:

* Классический ML-алгоритм, обученный на представлении BagOfWords/TF-IDF.
* RNN или LSTM модель.
* BERT (мощная предобученная модель для работы с естественным языком).

Результаты предсказания каждой модели выводятся на экран вместе со временем, затраченным на их получение.

## 2. Генерация текста с использованием модели GPT (Ильвир Хасанов и Виктория Князева)

В данном разделе проекта была реализована генерация текста с использованием модели GPT (Generative Pre-trained Transformer). Пользователь может ввести определенное начало (prompt) текста, а также настроить параметры генерации, включая длину выходной последовательности и число генераций. Также можно контролировать температуру или использовать top-k и top-p (nucleus) для управления разнообразием и качеством генерируемого текста.

## 3. Модель question answering (Анна Филина и Василий Севостьянов)

В этой части проекта была разработана система вопросно-ответной обработки текста с использованием модели timpal0l/mdeberta-v3-base-squad2, обученной на данных SQuAD 2.0. Пользователь может ввести вопрос и контекст (в котором содержится ответ), и модель применяя алгоритм вопросно-ответного моделирования выведет ответ.

# NLP project

This project is a multipage application for Natural Language Processing (NLP) developed using the Hugging Face platform and the Streamlit framework. The project involved the following contributors: Vasily Sevostyanov, Anna Filina, Ilvir Khasanov, Ivan Nikiforov, and Victoria Knyazeva.
[You can read it by following this link](https://huggingface.co/spaces/vasevooo/NLP_project)


## 1. Film Review Classification in English (Ivan Nikiforov)

This part of the project focuses on classifying film reviews in English. Users can enter their reviews in the input field, and the system predicts the sentiment (positive/negative) using three models:

* Classic ML algorithm trained on BagOfWords/TF-IDF representation.
* RNN or LSTM model.
* BERT (a powerful pretrained model for natural language processing).

The predictions of each model are displayed along with the time taken to obtain them.

## 2. Text Generation using GPT Model (Ilvir Khasanov and Victoria Knyazeva)

In this section of the project, text generation is implemented using the GPT (Generative Pre-trained Transformer) model. Users can enter a specific starting prompt and adjust generation parameters, including the length of the output sequence and the number of generations. Temperature control or top-k and top-p (nucleus) methods can be used to manage the diversity and quality of the generated text.

## 3. Question Answering Model (Anna Filina and Vasily Sevostyanov)

This part of the project focuses on a question answering system using the timpal0l/mdeberta-v3-base-squad2 model, trained on the SQuAD 2.0 dataset. Users can input a question and the corresponding context containing the answer, and the model applies question answering algorithms to provide the answer.