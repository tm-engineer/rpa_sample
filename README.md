# セットアップ  

  1. VM作成(docker-machine)  
  ```
  docker-machine create --driver virtualbox rpa-sample
  ```

  1. 作成したVMを適用  
  ```
  eval $(docker-machine env rpa-sample)
  ```

  1. コンテナビルド  
  ```
  docker-compose up -d --build
  ```

  1. コンテナ起動  
  ```
  docker exec -it app /bin/bash
  ```

  1. Django起動  
  ```
  python manage.py runserver 0.0.0.0:8000
  ```

  1. ポートフォワード  
  ```
  docker-machine ssh rpa-sample -L 8000:localhost:8000

  # docker-machine ssh {DockerMachine名} -L {ホストマシンの待ち受けポート} : {アドレス} : {VM内の待ち受けポート}
  ```
