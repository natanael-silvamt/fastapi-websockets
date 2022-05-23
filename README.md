# API desenvolvida com o framework Python FastAPI.
### A partir de outras experiências com websockets e python, não carrego boas recordações, por isso decidi criar essa API bem simples para mostrar o funcionamento do websocket junto com o GUNICORN e com vários Workers. Sim, o gunicorn não permite vários workers com websocket, mas antes dele temos o uvicorn (servidor para o fastapi) que possibilita a conexão socket com vários workers.

#### Para subir o serviço da API, basta:
1. ```sh
      git clone https://github.com/natanael-silvamt/fastapi-websockets.git
    ```

2. ```sh
      cd /fastapi-websockets
    ```

3. ```sh
      conda env create -f environment.yml
    ```

4. ```sh
      conda activate backend
    ```

5. ```sh
      ./start_api.sh
    ```

#### Após executar os passos anteriores, API vai ta rodando em:
  ```sh
    http://localhost:5000/api/ws
  ```
