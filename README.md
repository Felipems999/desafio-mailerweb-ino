🚀 Booking App Manager
Sistema de gerenciamento de reuniões e reservas de salas. O projeto utiliza uma arquitetura moderna com FastAPI no backend, React no frontend e infraestrutura conteinerizada para serviços de suporte.

🛠 Pré-requisitos
Antes de começar, você precisará ter instalado em sua máquina:

Python 3.12+

React.js + Vite & pnpm

Docker & Docker Compose

⚙️ Configuração das Variáveis de Ambiente
O projeto utiliza arquivos .env para gerenciar credenciais e conexões. Este passo é obrigatório antes de iniciar os servidores.

Backend
Navegue até a pasta backend/.

Copie o arquivo de exemplo:

```
cp .env.example .env
```
Abra o arquivo .env e ajuste as credenciais se necessário.

Nota Importante: No seu docker-compose.yml, o PostgreSQL está mapeado para a porta 15432. Certifique-se de que sua DATABASE_URL no .env reflete isso:
DATABASE_URL="postgresql://user:securepassword123@localhost:15432/backend"

Frontend (Opcional/Ajuste)
Certifique-se de que a REACT_PUBLIC_API_URL aponta para onde seu FastAPI está rodando (geralmente http://localhost:8000).

## Rodando o projeto

🏗️ Passo 1: Infraestrutura (Docker)
O backend depende de serviços como PostgreSQL, RabbitMQ e MailHog. Todos estão configurados no Docker Compose dentro da pasta backend/.

Acesse a pasta do backend:

```
cd backend
```

Certifique-se de ter um arquivo .env com as credenciais necessárias.

Suba os containers:

```
docker-compose up -d
```

Serviços disponíveis após o boot:

PostgreSQL: localhost:15432

pgAdmin (Gestão DB): localhost:16543 (Acesse com o e-mail do seu .env)

RabbitMQ: localhost:15672 (Painel de gerenciamento)

MailHog: localhost:8025 (Interface para visualizar e-mails de teste)

🐍 Passo 2: Backend (FastAPI)
Com os containers rodando, instale as dependências do Python:

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

```
pip install -r requirements.txt
```

Inicie o servidor de desenvolvimento:

```
fastapi run dev app/main.py
```

O backend estará rodando em: http://localhost:8000

Documentação interativa (Swagger): http://localhost:8000/docs

⚛️ Passo 3: Frontend (React + MUI)
Abra um novo terminal e acesse a pasta do frontend:

```
cd frontend
```

Instale as dependências usando o pnpm:

```
pnpm install
```

Inicie o servidor web:

```
pnpm run dev
```

O frontend estará disponível em: http://localhost:5173 (ou a porta indicada no terminal).

🧪 Executando Testes
Backend (Pytest)

```
cd backend
python -m pytest
Frontend (Vitest)
```

```
cd frontend
pnpm test
```

💡 Notas Adicionais
Fuso Horário: Certifique-se de que o frontend está enviando datas no formato ISO com offset para evitar conflitos de agendamento no backend.

MailHog: Todas as notificações de confirmação de reserva enviadas pelo sistema podem ser visualizadas localmente em http://localhost:8025.
