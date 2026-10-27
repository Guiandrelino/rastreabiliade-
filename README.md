# Rastreabilidade Industrial

Projeto de estudo em Python sobre processamento de imagens e leitura de códigos de barras e QR Codes, utilizando OpenCV e pyzbar. Os exemplos trabalham com uma imagem local e apresentam recursos básicos que podem apoiar aplicações de rastreabilidade industrial.

## Funcionalidades

- **`aula01.py`**: carrega a imagem de exemplo e exibe a versão original e uma versão em tons de cinza.
- **`aula02.py`**: busca códigos de barras e QR Codes na imagem, imprime o tipo e o conteúdo dos códigos encontrados no terminal e destaca suas posições com retângulos e textos na imagem.

A identificação depende da presença e da qualidade dos códigos na imagem; a detecção não é garantida para toda imagem.

## Estrutura do repositório

```text
.
├── aula01.py
├── aula02.py
├── coca cola espumante.jpg
└── README.md
```

## Pré-requisitos

- Python 3 e `pip` instalados.
- Ambiente gráfico disponível para abrir as janelas do OpenCV.
- Biblioteca nativa **ZBar**, utilizada pelo pyzbar (veja as instruções abaixo).

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Guiandrelino/rastreabiliade-.git
cd rastreabiliade-
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
```

No Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

> Dependendo da instalação, utilize `python3` no lugar de `python`.

### 3. Instale as dependências Python

```bash
python -m pip install opencv-python pyzbar
```

Use `opencv-python`, e não a variante `opencv-python-headless`, pois os exemplos abrem janelas para exibir imagens.

### 4. Verifique a dependência ZBar

**Windows:** os pacotes binários do pyzbar normalmente incluem as DLLs do ZBar. Caso a importação apresente erro de DLL, consulte as [instruções do pyzbar para Windows](https://github.com/NaturalHistoryMuseum/pyzbar#windows).

**Ubuntu/Debian:**

```bash
sudo apt-get update
sudo apt-get install libzbar0
```

**macOS (Homebrew):**

```bash
brew install zbar
```

## Como executar

Execute os comandos a partir da raiz do repositório, pois os scripts procuram a imagem pelo caminho relativo `coca cola espumante.jpg`.

### Exibir a imagem em tons de cinza

```bash
python aula01.py
```

Serão abertas duas janelas: uma com a imagem original e outra com a imagem em tons de cinza.

### Ler códigos na imagem

```bash
python aula02.py
```

O script informa no terminal se encontrou códigos. Quando encontra, exibe o tipo e o conteúdo de cada código, além de marcar a região correspondente na janela **Rastreabilidade Industrial**.

Com uma das janelas em foco, pressione uma tecla para encerrar a execução e fechar as janelas.

## Usar outra imagem

Altere o nome do arquivo passado para `cv2.imread(...)` no script desejado:

```python
imagem = cv2.imread('minha_imagem.jpg')
```

Coloque a imagem na pasta de execução ou informe o caminho correto para o arquivo. Os scripts não recebem o caminho da imagem por argumentos de linha de comando.

## Limitações e solução de problemas

- **Imagem não encontrada:** confira o nome do arquivo e a pasta de execução. Em `aula01.py`, não há validação do carregamento; em `aula02.py`, uma mensagem de erro é impressa, mas a execução não é interrompida. Assim, ambos podem gerar erros nas operações seguintes se a imagem não for carregada.
- **Nenhum código encontrado:** tente uma imagem com melhor resolução, boa iluminação e o código completo e nítido.
- **Janelas não abrem:** execute em um ambiente com interface gráfica e verifique se está usando `opencv-python`, sem a variante `headless`.
- **Escopo atual:** os exemplos processam uma imagem estática; não há captura por câmera, banco de dados ou histórico de rastreamento implementados.

## Tecnologias

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar)
- [ZBar](https://zbar.sourceforge.net/)
