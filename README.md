## Estrutura

### 1. Preparação do Ambiente

- Criar repositório no GitHub
- Criar repositório Localmente
- Inicializar o git no repositório local → `git init`
- Criar um arquivo na pasta do projeto que indica qual a versão do python que será utilizada → `pyenv local *[versão do python local]*`
- Criar o ambiente virtual → `poetry init`
- Ativar o ambiente virtual → `poetry shell`
- Adicionar bibliotecas → `poetry add`
- Criar pasta `.vscode`
- Criar arquivo `settings.json` na pasta do `.vscode`  e inserir o código abaixo para desocultar a pasta do git.

    ```json
    {
        "files.exclude": {
            "**/.git": false
        }
    }
    ```

- Criar o arquivo `.gitignore` para determinar quais arquivos não devem ir para o GitHub → `ignr -p python > .gitigone`  *(modelo .gitignore da toptal)*
- Criar arquivo readme → `touch README.md`
- Criar pasta de código `app`
- Criar pasta de `test`

### 2. Subindo repositório para o GitHub

- Adicionar arquivos a stage do git local → `git add .`
- Comitar as alterações → `git commit -m *["mensagem do commit"]`*
- Subir as alterações para o GitHub → `git push` [na primeira vez que for fazer o `git push` do repositório será necessário configurar o mesmo, no repositório do GitHub terá o passo a passo de como fazer].

### 3. Desenvolver Código

- Criar pasta que terá os módulos do código
- Criar arquivos `.py` dentro da pasta criada anteriormente que serão os modulos do código
- Criar arquivo `main.py` na pasta app
- Adicionar arquivo `__init__.py` na pasta dos modulos
- Desenvolver modulos → É uma boa prática criar uma branch para cada módulo - `*git checkout -b [nome do modulo]*`
- Chamar todos os módulos na função `main.py`
- Utilizar `docstring` nas funções criadas

### 4. Testes

- Adicionando a biblioteca de testes → `poetry add pytest`
- Escrever o teste → utilizar método (arrange, act, assert)
- Rodar o teste → `pytest -v`

### 5. Padrão de Código

- PEP8 → padrão de código em python
- Adicionar bibliotecas de padronização de código:
    - `isort` → ordenação de imports e from. *[para utilizar digitar no terminal* `isort .` *]*
    - `black`→ formatação do código. *[para utilizar digitar no terminal* `black .` *] - Há a biblioteca `blue` também(vai da preferência)*
    - `pydocstyle`  → mostra todos as partes do código que deveriam ter uma `docstring` . *[para utilizar digitar no terminal*  `pydocstyle .` *]*

### 6. Automatizar Tarefas

- Instalar biblioteca `poetry add taskipy`
- Automatizar tarefas no terminal com `taskipy`, exemplo:

```json
[tool.taskipy.tasks]

format = "isort . && black ."
```

Adicionar o código acima no arquivo do `pyproject.toml`

### 7. Documentar

- Instalar biblioteca `poetry add mkdocs`
- Criar pasta de docs → `mkdocs new .`
- Visualizar documentação no browser → `mkdocs serve`
- Criar automação para encerrar a porta :8000 → `kill = "kill -9 $(lsof -t -i :8000)"`
- Adicionar algumas bibliotecas → `poetry add mkdocstrings-python pygments mkdocs-material pymdown-extensions`
- No `mkdocs.yml` eu consigo personalizar meu site do mkdocs
- Publicar site no GitHub pages → `mkdocs gh-deploy`
- Utilizar ChatGPT para ajudar a criar o markdown (Notion já está no formato de markdown)

### 8. Pré-Commir

- Instalar biblioteca de pre-commit → `poetry add pre-commit`
- Criar arquivo chamado: `.pre-commit-config.yaml`
- Utilizar site pre-commit para pegar instruções para o que deseja fazer de pre-commit
- Instalar pre-commit →  `pre-commit install`
- Sempre quando fizer um commit será feito a validação dos testes configurados - CI da máquinda

### 9. CI

- Criar pasta `.github`  e dentro dessa pasta criar pasta `workflow`
- Criar arquivo `ci.yml` [o nome pode ser o que você quiser]
- Colocar o código do `yml` , no github actions consegue encontrar o que precisa ter no código

## Links

Repositório: https://github.com/lvgalvao/DataProjectStarterKit

Meu repositório: https://github.com/datafoia/estrutura_projeto_de_dado
