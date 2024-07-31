# RTSP Streamer

Este é um aplicativo Flask para iniciar e gerenciar streams RTSP usando `ffmpeg` e `multiprocessing`. A interface web permite que você adicione fluxos RTSP de entrada e saída, inicie streams, e pare streams ativos. O layout é responsivo e se ajusta bem a diferentes tamanhos de tela, incluindo dispositivos móveis.

## Estrutura do Projeto

```
flask_rtsp_streamer/
├── templates/
│   ├── index.html
├── static/
│   ├── css/
│       ├── style.css
├── app.py
```

## Requisitos

- Python 3.6+
- Flask
- ffmpeg-python
- Bootstrap 4.5.2

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/flask_rtsp_streamer.git
    cd flask_rtsp_streamer
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate  # Windows
    ```

3. Instale as dependências:
    ```sh
    pip install flask ffmpeg-python
    ```

## Uso

1. Execute o aplicativo Flask:
    ```sh
    python app.py
    ```

2. Abra o navegador e vá para `http://127.0.0.1:5000/`.

3. Use a interface para adicionar URLs RTSP de entrada e saída, e clique em "Start Stream" para iniciar um novo stream. Streams ativos serão listados abaixo com a opção de pará-los.

## Estrutura do Código

### `app.py`

Este é o arquivo principal do aplicativo Flask. Ele configura o servidor, define as rotas e gerencia os processos de streaming RTSP.

### `templates/index.html`

Este arquivo HTML define a interface do usuário usando Bootstrap para garantir um layout responsivo e estilizado.

### `static/css/style.css`

Este arquivo CSS contém estilos personalizados para o aplicativo, incluindo ajustes responsivos para diferentes tamanhos de tela.

## Funcionalidades

- **Iniciar Streams RTSP**: Adicione URLs RTSP de entrada e saída para iniciar novos streams.
- **Gerenciar Streams Ativos**: Veja a lista de streams ativos e pare qualquer um deles.
- **Interface Responsiva**: O layout se ajusta bem a diferentes tamanhos de tela, incluindo dispositivos móveis.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
```

