# game-server

## Requirement

- docker
- docker-compose

## Usage
コンテナの作成.
```bash
docker-compose up -d
```

コンテナにアクセス．
```bash
docker exec -it server bash
```
コンテナ内の操作．
```bash
# 初回のみ必要
python manage.py migrate
# サーバー起動
python manage.py runserver 0.0.0.0:8000
```

## Devlopment URL
Admin site : localhost:8000/admin/  
API docs : localhost:8000/docs/