# Controle de Visitantes - Aplicativo Python
Este é um aplicativo Python para controle de visitantes em um condomínio. O aplicativo possui uma interface gráfica onde você pode registrar informações de visitantes, consultar informações com base no número de documento e exibir imagens relacionadas.

## Requisitos
- Python 3.x
- Biblioteca `tkinter` para a criação da interface gráfica
- Biblioteca `Pillow` (PIL) para a manipulação de imagens
- (biblioteca para manipulação de arquivos CSV já está incluída na biblioteca padrão do Python)

Você pode instalar as bibliotecas Python necessárias usando o `pip`:

`pip install Pillow`

## Como usar

1. Clone este repositorio

git clone https://github.com/samuellgsDev/controle-de-visitantes.git

2. Navegue até o diretório do projeto:

cd controle-de-visitantes

3. execute o programa

python controle_de_visitantes.py

### ----------------------------------
A interface gráfica será exibida. Você pode usar as seguintes funcionalidades:

Registrar um novo visitante, preenchendo os campos de Nome, Documento de Identificação, Placa do Veículo e selecionando uma imagem.
Consultar informações de visitantes registrados com base no número de documento.
A imagem do visitante será exibida em miniatura ao lado das informações do visitante quando consultada