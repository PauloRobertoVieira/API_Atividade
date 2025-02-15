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

Após iniciar a API, você pode testar os endpoints:

### **1. Usando a Documentação Interativa (Swagger UI)**
Acesse a documentação interativa no navegador:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### **2. Usando o Postman**
Você pode importar a coleção do Postman para testar os endpoints. Siga os passos abaixo:

1. Abra o Postman.
2. Clique em **Import** e cole o link abaixo:
   ```
   http://127.0.0.1:8000/docs
   ```
3. Selecione os endpoints que deseja testar e envie as requisições.

### **3. Usando `curl` (via terminal)**
Você também pode testar os endpoints diretamente pelo terminal. Por exemplo:

```bash
curl -X GET "http://127.0.0.1:8000/curso/1"
```

## **Logs**
Os logs são armazenados no console e no arquivo `logs/app.log`, facilitando a depuração de erros.