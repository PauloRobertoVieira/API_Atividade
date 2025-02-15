# API
Repositório para atividade da disciplina de API. Pós em Agentes Inteligentes UFG

# **Configuração e Execução da API**

Este documento fornece um passo a passo para configurar e executar a API.

## **Requisitos**
- Python 3.10+
- `pip` instalado

## **Configuração de Variáveis de Ambiente**

Crie um arquivo `.env` e adicione as credenciais conforme o arquivo `.env.sample`:

```env
OPENAI_API_KEY="sua-chave-aqui"
```

## **Criando e Ativando o Ambiente Virtual**

### Windows
```bash
python -m venv venv
venv\Scripts\activate     # Para Windows
```

### Linux
```bash
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
```

## **Instalando Dependências**

```bash
pip install -r requirements.txt
```

Se `requirements.txt` não existir, crie-o:

```bash
pip freeze > requirements.txt
```

## **Executando a API**

```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`

## **Endpoints Disponíveis**

### **Cursos**
- `GET /curso/{course_id}` - Retorna dados de um curso.
  
### **Inteligência Artificial**
- `POST /classifica-curso` - Classifica um curso com IA.
- `POST /pergunta-chatgpt` - Faz uma pergunta ao ChatGPT.

### **Utilidades**
- `GET /log` - Teste de logs.

## **Testando a API**

Após iniciar a API, você pode testar os endpoints via Postman ou usando `curl`:

```bash
curl -X GET "http://127.0.0.1:8000/curso/1"
```

## **Logs**
Os logs são armazenados no console e no arquivo `logs/app.log`, facilitando a depuração de erros.

🚀
