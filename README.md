## #Pokemon Data Analysis Project

Este projeto em Python utiliza a Pokémon API para coletar, tratar e armazenar dados para análise e visualização. O objetivo é permitir que o usuário obtenha informações sobre um Pokémon específico a partir de um ID fornecido, aplicando técnicas de manipulação e armazenamento de dados.

* Funcionalidades

Coleta de Dados: A aplicação se conecta à Pokémon API e recupera informações detalhadas sobre o Pokémon identificado pelo ID fornecido.

Armazenamento de Dados: Os dados coletados são tratados e exportados para um arquivo CSV, além de serem armazenados em uma tabela SQLite3 para facilitar consultas e manipulação.

Análise e Visualização: A tabela de dados é usada como fonte para gerar gráficos e visualizações utilizando bibliotecas de visualização de dados, como Matplotlib e Seaborn. Essas visualizações são apresentadas em um Jupyter Notebook para facilitar a análise exploratória e tornar as informações mais acessíveis.

* Tecnologias Utilizadas

Python: Linguagem principal do projeto.

SQLite3: Para armazenamento estruturado dos dados coletados.

Jupyter Notebook: Para criação de relatórios interativos e análise exploratória dos dados.

Bibliotecas de Visualização: Seaborn e Matplotlib para criar gráficos que facilitam a compreensão dos dados.

* Como Executar

Clone este repositório.

Instale as dependências usando pip install -r requirements.txt.

Execute o script principal para coletar os dados do Pokémon.

Abra o Jupyter Notebook para realizar a análise visual e gerar gráficos.

Este projeto é ideal para estudantes e profissionais interessados em explorar dados de Pokémons, aprimorar suas habilidades em coleta e manipulação de dados, e criar visualizações informativas e atrativas usando Python.

** Próximos passos:
 - Adicionar um menu para o usuário selecionar quer adicionar a base de dados um novo pokemon ou removê-lo;
 - Implementar uma lógica para não ser possível repetir pokemons no db;
 - Adicionar mais atributos a tabela pokemon para construir mais insights analíticos através de gráficos.