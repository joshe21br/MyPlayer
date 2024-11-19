# My Player

O **My Player** é um simples reprodutor de músicas desenvolvido em Python utilizando as bibliotecas **Flet** e **Pygame**. Ele permite ao usuário carregar, salvar e controlar a reprodução de uma playlist de músicas. Além disso, o player oferece uma interface gráfica para gerenciar as faixas, ajustar o volume e navegar entre as músicas.

## Funcionalidades

- **Carregar Playlist**: O player carrega automaticamente a playlist de um arquivo `playlist.json`.
- **Salvar Playlist**: Você pode salvar a playlist atual no arquivo `playlist.json`.
- **Reprodução de Músicas**: Permite tocar, pausar, retomar e parar músicas.
- **Controle de Faixas**: Avançar e retroceder entre as músicas da playlist.
- **Ajuste de Volume**: Controle o volume da música com um slider.
- **Gerenciamento da Playlist**: Adicionar, excluir músicas e limpar a playlist.
- **Carregar Arquivos**: Através de um seletor de arquivos, você pode adicionar várias músicas à playlist.

## Requisitos

Para executar o Joshe Player, você precisa ter Python 3.x instalado em sua máquina, além das seguintes bibliotecas:

- [Flet](https://flet.dev) — Para a criação da interface gráfica.
- [Pygame](https://www.pygame.org/) — Para o controle da reprodução de áudio.

### Instalação das dependências

1. Clone este repositório:

   ```bash
   git clone https://github.com/joshe21br/MyPlayer.git
   cd my-player
   ```

2. Instale as dependências com `pip`:

   ```bash
   pip install flet pygame
   ```

## Uso

1. **Inicie o aplicativo**:
   
   Após a instalação das dependências, execute o script Python para iniciar o player:

   ```bash
   python my_player.py
   ```

2. **Carregar músicas**:
   Clique no ícone de "Folder" para selecionar os arquivos de música que deseja adicionar à playlist.

3. **Reproduzir música**:
   - Selecione a música da playlist e clique no ícone de "Play" para começar a reprodução.
   - Você pode usar os botões de "Pause", "Stop", "Next" e "Prev" para controlar a reprodução.

4. **Ajustar volume**:
   Use o slider de volume para controlar o nível de áudio da música em reprodução.

5. **Salvar a playlist**:
   Clique no ícone de "Save" para salvar a playlist atual em um arquivo `playlist.json`.

6. **Excluir ou limpar a playlist**:
   Você pode excluir a playlist ou remover todas as faixas clicando no ícone de "Clear All".

## Estrutura do Projeto

```plaintext
- my_player.py           # Arquivo principal do aplicativo
- playlist.json             # Arquivo onde a playlist é salva
- /img                      # Diretório com imagens (exemplo: image.jpg)
```

## Como Funciona

1. O player é inicializado e a interface gráfica é carregada utilizando a biblioteca Flet.
2. As músicas da playlist são exibidas em uma lista e você pode interagir com cada faixa para reproduzi-la.
3. A música é carregada e controlada pelo Pygame, que gerencia a reprodução, pausa e controle de volume.
4. O arquivo `playlist.json` é utilizado para armazenar a lista de músicas, permitindo que a playlist seja carregada automaticamente ao iniciar o aplicativo.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Desenvolvedor

- **Joshe**  
- **E-mail**: joshuasotero@protonmail.com  


## Agradecimentos

Agradecimentos à comunidade do [Flet](https://flet.dev) e ao [Pygame](https://www.pygame.org/) por suas incríveis bibliotecas, que tornaram este projeto possível!
