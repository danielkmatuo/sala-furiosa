## **Introdução** 📖
Feito como um teste técnico para uma vaga de assistente de engenharia de software, esse software é um simples site de chat online, ao estilo whatsapp web. Houve muito mais foco na parte do back-end durante a criação do código do que em outras partes. Logo, o site esta com uma aparência bem "crua" ainda.

## **Tecnologias utilizadas** 🛠
* Python 3.12
* Django 5.2
* Django Channels 4.2.2
* Redis 
* Docker
* PostgreSQL (via Supabase)

##  **Preparação do ambiente e instalação** 🚀
1. Baixe o Docker desktop [(clique aqui)](https://www.docker.com/)
2. 2. Crie uma conta na plataforma Supabase [(clique aqui e selecione a opção de plano gratuito)](https://supabase.com/)
3. Após criar uma conta no Supabase, crie um novo projeto e nele adicione as tabelas:
* **Salas:**
   | id (primary key)| nome |
   | --              | ---- |
   |id1              |nome1 |
* **Mensagens:**
  | id (primary key)| msg | sender | sala | criada_dia | criada_hora |
  | --------------- | --- | ------ | ---- | ---------- | ----------- |
  | id1             | msg1| sender1| sala1| criada_dia1| criada_hora1|

4. (Caso esteja no Windows) Abra o powershell como administrador e instale o **WSL** utilizando o comando: `wsl --install`
5. Execute o comando no terminal: `git clone https://github.com/danielkmatuo/sala-furiosa.git`
6. Dentro do diretório do projeto clonado, crie o arquivo **.env** seguindo o exemplo do arquivo **.env.example**

## **Rodando o programa** ⚡
1. (Caso esteja no Windows) Abra o **WSL**
2. Dentro do diretório do projeto, crie um novo ambiente virtual, digitando no terminal: `python3 -m venv venv`
3. Ative o ambiente virtual com o comando: `source venv/bin/activate`
4. Baixe as dependências necessárias utilizando o comando: `pip install -r requirements.txt`
5. Cheque para ver se as dependências estão instaladas com os comandos: `pip freeze` ou `pip list`
6. Faça as migrações necessárias com o comando: `python3 manage.py makemigrations`
7. Crie o container no Docker e rode o programa com o comando: `docker-compose up --build`

## **Contatos** 📱
* email: danielkmatuo@gmail.com
* github: @danielkmatuo
