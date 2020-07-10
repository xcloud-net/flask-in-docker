# 容器部署flask应用

```
docker network create xx
docker-compose up -d
```

### 实现功能
- 日志文件按照体积和日期分割
- 日志为json格式，方便agent收集到分布式日志系统
- 使用identity server的jwk验证jwt
- swagger集成

### 安装py jwt要注意的事项

`必须安装cryptography，否则pyjwt中的rsa算法将找不到from_jwk方法`

https://github.com/jpadilla/pyjwt/blob/dc8dc7d05d54bd5502295601c01b557caab92a76/jwt/algorithms.py#L221

``` python
if has_crypto:  # noqa: C901

    class RSAAlgorithm(Algorithm):
        ...
        ...
```