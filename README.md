# NLP Project

Проект по обработке естественного языка. 
Был выполнен студентами [Эльбрус Буткемп](https://github.com/Elbrus-DataScience): 
1. [Василий Севостьянов](https://github.com/vasevooo) 
2. [Анна Филина](https://github.com/AnnaFilinaa)
3. [Ильвир Хасанов](https://github.com/IlvirH)
4. [Иван Никифоров](https://github.com/kefkefkefkef)
5. [Виктория Князева](https://github.com/vvv-knyazeva)

Данный проект является мультистраничным приложением для обработки естественного языка (Natural Language Processing) и был разработан с использованием платформы ```Hugging Face``` и фреймворка ```Streamlit```.
Ознакомиться с работой приложения можно по [ссылке](https://huggingface.co/spaces/vasevooo/NLP_project). 

**Использованные инструменты:**
1. классические ML-алгоритмы
2. Нейросети - семейство BERT моделей, LSTM, GPT-2

## 1. Классификация отзывов на фильмы на английском языке (Иван Н.)

В этой части проекта была разработана система классификации отзывов на фильмы на английском языке. Пользователь может ввести свой отзыв в поле ввода, после чего система предсказывает его класс (позитивный/негативный) с помощью трех моделей:

* Классический ML-алгоритм, обученный на представлении ```BagOfWords/TF-IDF```
* ```LSTM``` модель
* ```BERT``` (предобученная модель для работы с естественным языком)

Результаты предсказания каждой модели выводятся на экран вместе со временем, затраченным на их получение.

## 2. Генерация текста с использованием модели GPT-2 (Ильвир Х. и Виктория К.)

В данном разделе проекта была реализована генерация текста с использованием модели `GPT-2` (Generative Pre-trained Transformer). Пользователь может ввести определенное начало (prompt) текста, а также настроить параметры генерации, включая длину выходной последовательности и число генераций. Также можно контролировать температуру или использовать top-k и top-p (nucleus) для управления разнообразием и качеством генерируемого текста. Модель была дополнительно обучена на произведении ```М. Булгакова "Марстер и Маргарита"```. 

## 3. Ответы на вопросы исходя из контектста (Анна Ф. и Василий С.)

В этой части проекта была разработана система вопросно-ответной обработки текста с использованием модели ```ROBERTA-base```, файнтюненной на данных SQuAD 2.0. Пользователь может ввести вопрос и контекст (в котором содержится ответ), и модель применяя алгоритм вопросно-ответного моделирования выведет ответ.

# NLP Project

This is a natural language processing project completed by students from [Elbrus Bootcamp](https://github.com/Elbrus-DataScience):

1. [Vasily Sevostyanov](https://github.com/vasevooo)
2. [Anna Filina](https://github.com/AnnaFilinaa)
3. [Ilvir Khasanov](https://github.com/IlvirH)
4. [Ivan Nikiforov](https://github.com/kefkefkefkef)
5. [Victoria Knyazeva](https://github.com/vvv-knyazeva)

This project is a multi-page application for natural language processing (NLP) developed using the `Hugging Face` platform and the `Streamlit` framework. You can explore the application [here](https://huggingface.co/spaces/vasevooo/NLP_project).

**Tools Used:**
1. Classic ML algorithms
2. Neural Networks - BERT models, LSTM, GPT-2

## 1. Film Review Classification in English (Ivan N.)

In this part of the project, a film review classification system for English language reviews was developed. Users can enter their review in the input field, and the system predicts its sentiment (positive/negative) using three models:

* Classic ML algorithm trained on `BagOfWords/TF-IDF` representation.
* `LSTM` model.
* `BERT` (a pretrained model for natural language processing).

The predictions of each model are displayed along with the time taken to generate them.

## 2. Text Generation using `GPT-2` Model (Ilvir K. and Victoria K.)

This section of the project focuses on text generation using the GPT-2 (Generative Pre-trained Transformer) model. Users can enter a specific starting prompt and adjust generation parameters, including the length of the output sequence and the number of generations. Temperature control or top-k and top-p (nucleus) methods can be used to manage the diversity and quality of the generated text. The model was additionally trained on the work `Mikhail Bulgakov's "The Master and Margarita"`.

## 3. Contextual Question-Answering (Anna F. and Vasily S.)

In this part of the project, a question-answering system using the `ROBERTA-base` model trained on the SQuAD 2.0 dataset was developed. Users can input a question and the corresponding context containing the answer, and the model applies question-answering algorithms to provide the answer.
