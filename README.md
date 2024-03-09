<div align="center">
<h1 style="color:#1597e8">
    Análise de Sentimentos em Tweets 🐦<br/>
    <span style="font-size:18px; color:gray">Coletados durante a pandemia da COVID-19 🦠</span>
</h1>
</div>
<div align="center">
<!-- python -->
<img src="https://img.shields.io/badge/3.10-%233776AB?style=flat-square&logo=python&logoColor=white&label=Python" alt="Python 3.10">
<!-- pré-commit -->
<img src="https://img.shields.io/badge/pre--commit-%23000000?style=flat-square&logo=pre-commit&logoColor=white" alt="pre-commit">
<br/>
<!-- pandas -->
<img src="https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas">
<!-- matplotlib -->
<img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=flat-square&logo=Matplotlib&logoColor=black" alt="Matplotlib">
<!-- sklearn -->
<img src="https://img.shields.io/badge/-Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn">
<!-- spacy -->
<img src="https://img.shields.io/badge/-Spacy-09A8E3?style=flat-square&logo=spacy&logoColor=white" alt="Spacy">
<!-- poetry -->
<img src="https://img.shields.io/badge/-Poetry-4B32C3?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry">


<p>Projeto de análise de sentimentos em tweets utilizando técnicas de NLP e Machine Learning.</p>
<figure align="center">
<img src="https://img.freepik.com/free-vector/messenger-concept-illustration_114360-860.jpg?w=900&t=st=1709998370~exp=1709998970~hmac=5bf95343bea4785fe16891486268abb6c4047235ac6498f61f0ea412301abdc7" height=300>
<br/>
<figcaption>Imagem de <a href="https://www.freepik.com/free-vector/messenger-concept-illustration_6199003.htm#fromView=search&page=1&position=20&uuid=5d4efd58-f6fd-4d35-8037-4edfc7d04b91">storyset</a> no <a href="https://www.freepik.com/">Freepik</a></figcaption>
<figure>
</div>

## 📚 Sobre o Projeto

A pandemia de COVID-19 trouxe consigo uma série de mudanças na vida das pessoas, desde a forma de trabalhar até a forma de se comunicar. Com o isolamento social, as redes sociais se tornaram um dos principais meios de comunicação entre as pessoas, e com isso, a quantidade de informações e opiniões compartilhadas aumentou consideravelmente.

A análise de sentimentos em textos é uma assunto dentro da área Processamento de Linguagem Natural (NLP) que tem como objetivo identificar e extrair informações sobre as emoções e opiniões expressas em textos. Neste projeto, realizamos a análise dos tweets e a classificação dos sentimentos expressos neles, utilizando técnicas de NLP e aprendizado de máquina.

## 📦 Conteúdo

- [Sobre o Projeto](#-sobre-o-projeto)
- [Conteúdo](#-conteúdo)
- [Dados](#-dados)
- [Objetivos](#-objetivos)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como Executar o Projeto](#-como-executar-o-projeto)
- [Licença](#-licença)

## 📊 Dados

Para esse estudo, usamos os dados coletados do Twitter, disponível no [Kaggle](https://www.kaggle.com/datatattle/covid-19-nlp-text-classification). Esse conjunto, composto por 41.557 *tweets*, foi coletado entre os dias 16 de março e 14 de abril de 2020. As 6 colunas presentes nele são:

1. `OriginalTweet`: O texto original do *tweet*, contendo a mensagem relacionada à pandemia de COVID-19. Esse campo é o principal objeto de análise do projeto.
2. `Sentiment`: O sentimento predominante no *tweet*, categorizado em 5 classes:
   - **Extremamente Negativo**
    - **Negativo**
    - **Neutro**
    - **Positivo**
    - **Extremamente Positivo**

3. `TweetAt`: A data em que o *tweet* foi publicado, permitindo a análise temporal dos dados.
4. `Location`: A localização cadastrada pelo usuário que publicou o *tweet*.
5. `ScreenName`: O nome de usuário do *Twitter* codificado, protegendo a identidade dos autores dos tweets.
6. `UserName`: A arroba (@) do usuário do *Twitter* codificada, complementando a informação do `ScreenName`.

### Exemplo de mensagens por sentimento:

a) **Extremamente Negativo**:
```
Matters have gotten desperate in Not a single shop grocery provision store has been allowed to open for 3 days inspite of assurances by If we step out looking for bread we are beaten by cops Starvation will kill is before
```

b) **Negativo**:
```
Just because the sun is shining doesn't mean it's going to save you, your neighbours nor your family and friends from covid-19. I have to work at a supermarket so people can still get food. Just stay the fuck inside or have you not heard that nearly 5000 Britons have died?
```

c) **Neutro**:
```
Here we go. Today the #Coronavirus has arrived in the next county over, and my regular grocery store is starting to get cleaned out.
```

d) **Positivo**
```
Stay home this is a #pandemic #churches need to do the services online do your grocery shopping online  and tip well I will be doing the same if you do go out wear a mask #stayhome #coronavirus #covid19 #CoronavirusPandemic
```

e) **Extremamente Positivo**
```
The Berkshire Dream Center in is working to help families in need stock up and stay prepared with basic necessities amid the outbreak Food diaper distribution is taking place today on Tyler Street Details here
```

## 🎯 Objetivos
### Objetivo Geral
Explorar e analisar os dados do conjunto de tweets coletados sobre a COVID-19, buscando identificar padrões e *insights* relevantes sobre a percepção da população durante a pandemia.

### Objetivos Específicos:
1. **Análise Exploratória de Dados:**
    - Descrever as características estatísticas do conjunto de dados, como distribuição de frequências dos sentimentos, localização dos usuários e datas dos tweets.
    - Visualizar os dados por meio de gráficos e tabelas para compreender distribuição dos sentimentos.
2. **Pré-processamento de Texto:**
    - Aplicar técnicas de pré-processamento como remoção de stopwords, lematização e normalização para minúsculas para a análise.
    - Avaliar o impacto do pré-processamento na performance dos modelos de classificação de sentimentos.
3. **Extração de Características:**
    - Testar diferentes técnicas de vetorização, como *Bag of Words* (BOW), TF-IDF, *Word Embeddings* e *Sentence Embeddings*, para identificar a melhor representação do texto para a tarefa de classificação de sentimentos.
    - Comparar o desempenho dos modelos de classificação com as diferentes técnicas de vetorização, usando métricas de avaliação como acurácia, precisão, recall e F1-score.
4. **Classificação de Sentimentos:**
   - Treinar e avaliar diferentes modelos de classificação de sentimentos, como Máquina de Vetores de Suporte (SVM), Regressão Logística, Floresta Aleatória e Redes Neurais, para identificar o modelo com melhor desempenho.
5. **Análise de Resultados:**
   - Interpretar os resultados da classificação de sentimentos e identificar os principais tópicos e sentimentos presentes nos tweets.



## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Scikit-Learn](https://scikit-learn.org/stable/)
- [Spacy](https://spacy.io/)
- E outras bibliotecas de Python


## 🚀 Como Executar o Projeto

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)
- [Pip](https://pypi.org/project/pip/)

Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

### 🧭 Rodando o Jupyter Notebook

```bash
# Clone este repositório
$ git clone https://github.com/jessicacardoso/sentiment-analysis-tweets.git
```
```bash
# Acesse a pasta do projeto no terminal/cmd
$ cd sentiment-analysis-tweets
```
```bash
# Instale as dependências
$ pip install -r requirements.txt
```
```bash
# Execute o Jupyter Notebook
$ jupyter notebook
```

## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).
