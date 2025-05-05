## **Introdução** 📖
Feito como um teste técnico para uma vaga de assistente de engenharia de software, esse software é um simples site de chat online, ao estilo whatsapp web. Houve muito mais foco na parte do back-end durante a criação do código do que em outras partes. Logo, o site esta com uma aparência bem "crua" ainda.

## **Tecnologias utilizadas** 🛠
* Python 3.11.11
* Django 5.2
* Django Channels 4.2.2
* Redis (via Upstash Redis)
* Docker
* PostgreSQL (via Supabase)
* Render

##  **Preparação do ambiente e instalação (Caso queira rodar o site localmente)** 🚀
1. Baixe o Docker desktop [(clique aqui)](https://www.docker.com/)
2. Crie uma conta na plataforma Supabase [(clique aqui e selecione a opção de plano gratuito)](https://supabase.com/)
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
5. Crie uma conta no Upstash Redis [clique aqui para se cadastrar no site](https://upstash.com/)
6. Execute o comando no terminal: `git clone https://github.com/danielkmatuo/sala-furiosa.git`
7. Dentro do diretório do projeto clonado, crie o arquivo **.env** seguindo o exemplo do arquivo **.env.example**

## **Rodando o programa localmente** ⚡
1. (Caso esteja no Windows) Abra o **WSL**
2. Dentro do diretório do projeto, crie um novo ambiente virtual, digitando no terminal: `python3 -m venv venv`
3. Ative o ambiente virtual com o comando: `source venv/bin/activate`
4. Baixe as dependências necessárias utilizando o comando: `pip install -r requirements.txt`
5. Cheque para ver se as dependências estão instaladas com os comandos: `pip freeze` ou `pip list`
6. Faça as migrações necessárias com o comando: `python3 manage.py makemigrations`
7. Crie o container no Docker e rode o programa com o comando: `docker-compose up --build`

## **Acessando o site via link do Google Forms** 💻
1. Cole o link fornecido no Google Forms no navegador
2. O site abre na página principal, onde existem duas opções: Login e Registro
3. Caso não tenha uma conta ainda no site da Sala Furiosa, clique no botão "Registro" e forneça os dados para realização do cadastro
4. Com isso, o site irá te direcionar para a página de login, onde você pode acessar sua conta utilizando tanto o nome de usuário quanto o endereço de email
5. O site te levará para uma página de acesso de salas, onde você poderá criar uma nova sala, ou se juntar a uma sala já existente, tudo isso simplesmente digitando o nome da sala e clicando em "Criar"
6. Com isso, você será redirecionado para o chat da sala, onde poderá enviar mensagens utilizando a barra inferior e clicando e "Enviar" para mandar as mensagens no chat

## **Contatos** 📱
* email: danielkmatuo@gmail.com
* github: @danielkmatuo
