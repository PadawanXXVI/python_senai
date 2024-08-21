# Entendendo GIT

|Comando|Descrição|
|-|-|
| git init | Inicia o monitoramento do projeto |
| git branch -M main| Renomeia a branch principal (ramificação principal) de 'master' para 'main'|
| git add <NomeDoArquivo>| Manda o arquivo para área de staging |
| git add . | Manda todos os arquivos para a área de staging |
| git stauts | Verifica a situação atual dos arquivo|
| git config --global user.name <'Nome do Usuário'> | Informa o nome do usuário proprietário |
| git congig --global user.email <'Email do Usuário'> | Informa o email do usuário proprietário |
| git config --list | Verifica os dados do usuário - username e email |
| git commit -m 'primeiro commit' | Faz o commit |
| git log | Verifica histórico de commits |
| git checkout -b NomeDaBranch | Cria e muda de branch no projeto |
| git checkout nomeDaBranch| Muda de uma branch para outra existente |
| git branch | Lista as branches existentes no projeto |
| git merge nomeDaBranch | Mescla os dados das branches|
| git branch -d nomeDaBranch| Deleta a branch -d (minúsculo) só possível com todos commites|
| git branch -D nomeDaBranch| Deleta a branch -D (maiúsculo) deleta a branch mesmo sem terem sido feitos os commits|
| git clone <'link do repositório'>| Faz uma cópia do repositório no diretório |
| git push -u origin 'nomeDaBranch'| Envia as alterações da máquina local para o repositório online |
