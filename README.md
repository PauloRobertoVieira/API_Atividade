# API
Repositório para atividade da disciplina de API. Pós em Agentes Inteligentes UFG

# **Configuração e Execução da API**

Este documento fornece um passo a passo para configurar e executar a API.

## **Requisitos**
- Python 3.10+
- `pip` instalado

## **Criando e Ativando o Ambiente Virtual**

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows
```

## **Instalando Dependências**

```bash
pip install -r requirements.txt
```

Se `requirements.txt` não existir, crie-o:

```bash
pip freeze > requirements.txt
```

## **Configuração de Variáveis de Ambiente**

Crie um arquivo `.env` e adicione:

```env
openai_api_key="sua-chave-aqui"
secret_token="seu-token-seguro"
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
