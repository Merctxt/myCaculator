# Calculadora em Python com PyQt

Esta é uma calculadora gráfica desenvolvida em Python usando a biblioteca PyQt. O projeto inclui uma interface de usuário intuitiva e diversas funcionalidades.

![Captura de Tela da Calculadora]

(https://github.com/user-attachments/assets/a6f1dd18-a6c0-4686-9e84-c9c41a1e6323)

## Funcionalidades!

- Adição
- Subtração
- Multiplicação
- Divisão
- Potenciação
- Contas negativas
- Limpar tela
- Suporte a números flutuantes

## Estrutura do Projeto

- `main.py`: Arquivo principal que inicializa a aplicação.
- `buttons.py`: Define os botões da calculadora.
- `display.py`: Gerencia a exibição dos resultados.
- `main_window.py`: Configura a janela principal da aplicação.
- `utils.py`: Funções utilitárias usadas pela calculadora.
- `info.py`: Contém informações adicionais sobre a aplicação.
- `path.py`: Gerencia os caminhos dos arquivos.
- `Calculadora.spec`: Arquivo de especificação para criar o executável.
- `build`, `dist`, `files`: Diretórios usados durante a construção do executável.



## Como Executar

1. Clone este repositório:
   bash
   git clone (https://github.com/Merctxt/myCaculator.git)
   
2. Navegue até a pasta do projeto:
   bash
   cd SEU_REPOSITORIO/calculadora_QT
   
3. Abra a pasta do projeto no VS Code:
   bash
   code .
   
4. Execute a aplicação a partir do arquivo `main.py`:
   - No VS Code, abra o terminal integrado (Ctrl+`).
   - Certifique-se de que está no ambiente virtual correto, caso esteja usando um.
   - Execute o arquivo `main.py`:
     bash
     python main.py
     

## Como Construir o Executável

1. Certifique-se de ter o PyInstaller instalado:
   bash
   pip install pyinstaller
   
2. Use o PyInstaller para criar o executável:
   bash
   pyinstaller Calculadora.spec
   

## Contribuições

Contribuições são bem-vindas. Por favor, abra uma issue ou um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
