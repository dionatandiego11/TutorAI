# IA Tutor Aristóteles baseado no Gemini para a disciplina de UPx5

Este é um aplicativo de Inteligência Artificial que utiliza o modelo de linguagem Gemini para fornecer tutoria personalizada aos alunos da disciplina de UPx5. O aplicativo permite que os alunos façam perguntas e recebam respostas detalhadas, além de exercícios e explicações passo a passo.

## Recursos

- **Perguntas e Respostas**: Os alunos podem fazer perguntas sobre qualquer tópico relacionado à disciplina de UPx5, e o modelo Gemini fornecerá respostas detalhadas e precisas.
- **Exercícios Personalizados**: O aplicativo pode gerar exercícios personalizados com base no nível de conhecimento e nas áreas de dificuldade do aluno.
- **Explicações Passo a Passo**: Para conceitos mais complexos, o Gemini oferece explicações passo a passo, com exemplos e visualizações para facilitar o entendimento.
- **Feedback Instantâneo**: Os alunos recebem feedback instantâneo sobre suas respostas, permitindo que eles identifiquem e corrijam rapidamente quaisquer lacunas em seu conhecimento.

## Tecnologias Utilizadas

- **Google Generative AI**: Um conjunto de ferramentas de IA generativa desenvolvido pela Google, que permite a utilização de modelos avançados de linguagem para gerar respostas de alta qualidade e coerentes em uma ampla gama de tópicos. No código, é usado o modelo gemini-pro para responder às mensagens dos usuários.
- **Flask**: Um microframework web em Python que facilita a criação de aplicações web. Ele fornece a base para a aplicação, permitindo a definição de rotas, o processamento de requisições e a renderização de templates HTML.
- **Flask-Caching**: Uma extensão do Flask que adiciona capacidades de cache à aplicação. No código, é configurado para armazenar respostas do modelo de IA na memória, melhorando a performance ao evitar chamadas repetidas à API.
- **Flask-Session**: Uma extensão do Flask que adiciona suporte a sessões de usuário. No código, é usado para gerenciar o histórico de chat dos usuários, armazenando-o no sistema de arquivos para manter a continuidade das conversas entre requisições.

## Como Usar

1. Faça o clone deste repositório em sua máquina local.
2. Instale as dependências executando no diretório raiz.
   -  pip install flask
   -  pip install google-generativeai
   -  pip install Flask-Caching
   -  pip install flask-session
4. Inicie o servidor executando `python app.py`.
5. Acesse o aplicativo em `http://localhost:5000`.
6. Recomenda-se utilizar Anaconda, uma distribuição gratuita e de código aberto das linguagens de programação Python e R, amplamente utilizada para aprendizado de máquina e computação científica.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma sugestão de melhoria, sinta-se à vontade para abrir uma nova issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
