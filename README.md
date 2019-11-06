# Hiris
###### Empresa: **Contagil**

Este projeto tem como finalidade realizar o download automatico de consultas no sistema de Administração Tributária e Financeira([ATF](https://www4.receita.pb.gov.br/atf/)), pertencente a Secretaria de Estado da Fazenda.

### Instalação pelo terminal

```
pip install selenium
pip install pytest
pip install datatime
```

### Instalação automatica (Linux)

> Abra o arquivo e mude a rota de acesso ao seu projeto.

Acesse a pasta [install](/src/install) e execute o arquivo install.sh

### Instalação automatica (Windows)

> Abra o arquivo e mude a rota de acesso ao seu projeto.

Acesse a pasta [install](/src/install) e execute o arquivo install.bat

_Obs: Caso não funcione a instalação automatica no windows, tente por linha de comando no terminal após realizar as devidas configurações no sistema._

### Para fazer o download dos arquivos solicitados

Acesse o terminal do seu sistema operacional e rode o comando abaixo.

```
python app.py
```

Ou execute os seguintes arquivos abaixo de acordo com o seu sistema operacional.

###### Linux

Acesse a pasta [run](/src/run) e execute o arquivo run_download.sh

###### Windows

Acesse a pasta [run](/src/run) e execute o arquivo run_download.bat
