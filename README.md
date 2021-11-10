## Django Rest Framework 学习
学习基于官方文档：https://www.django-rest-framework.org/tutorial/1-serialization/

### 测试API
查询所有(GET)：`http://127.0.0.1:8000/snippets/`

新增(POST)：`http://127.0.0.1:8000/snippets/`
```json
{
  "id": 3,
  "title": "",
  "code": "print(123)",
  "linenos": false,
  "language": "python",
  "style": "friendly"
}
```

获取单个实例详情(GET)：`http://127.0.0.1:8000/snippets/3`

更新(PUT)：`http://127.0.0.1:8000/snippets/3`
```json
{
    "id": 3,
    "title": "",
    "code": "print(456)",
    "linenos": false,
    "language": "python",
    "style": "friendly"
}
```

删除(DELETE)：`http://127.0.0.1:8000/snippets/3`