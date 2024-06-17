## Desafio DevOps:

### Objetivo:
- Configurar uma aplicação web simples em Python (Flask) usando Docker, Kubernetes e CI/CD.

### Tarefas
- Criar uma aplicação Flask simples:
- Crie uma aplicação Flask que tenha um endpoint / que retorne a mensagem "Hello, DevOps!".

#### Dockerize a aplicação:
- Crie um Dockerfile para a aplicação Flask.
- Certifique-se de que a aplicação pode ser executada em um contêiner Docker.

#### Configurar Kubernetes:
- Crie um manifesto Kubernetes (.yaml) para implantar a aplicação Flask.
**O manifesto deve incluir:**
- Um Deployment
- Um Service (NodePort ou LoadBalancer)
- Implante a aplicação em um cluster Kubernetes local (pode usar Minikube ou Kind).

#### Configurar CI/CD com GitHub Actions:
- Configure um pipeline de CI/CD no GitHub Actions que faça o seguinte:
- Teste o código Flask.
- Construa a imagem Docker e publique-a no Docker Hub (ou outra registry de sua escolha).
- Implemente a aplicação no cluster Kubernetes.

#### Documentação:
- Crie um README.md com instruções sobre como:
- Executar a aplicação localmente.
- Construir a imagem Docker.
- Implantar a aplicação no Kubernetes.
- Configurar o pipeline CI/CD.

#### Entregáveis:
- Link para o repositório GitHub contendo o código, Dockerfile, manifestos Kubernetes e configuração do GitHub Actions.
- Link para a imagem Docker publicada (Docker Hub ou outra registry).
- Qualquer outra documentação adicional que considere relevante.

#### Critérios de Avaliação:
- Clareza e organização do código e documentação.
- Funcionamento correto da aplicação e da pipeline CI/CD.
- Adoção de boas práticas de DevOps e Kubernetes.
