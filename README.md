## Django Rest Framework 学习
学习基于官方文档：https://www.django-rest-framework.org/tutorial/1-serialization/

### 测试API（2.2版本和之前版本可用）
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

### 权限测试API（第三版可用）
数据库提供两个用户：
1. username: admin, password: 123456789
2. username: hou01, password: 123456789

打开网址：`http://127.0.0.1:8000/snippets/`
此时只能看到有一条记录，owner是admin所有，右上角有login，可以登录
登录admin，可以添加记录，不登录不可以添加，这个是初步的权限控制，只有登录的用户才可以

打开网址：`http://127.0.0.1:8000/snippets/1`
此如果是admin用户，有编辑权限，如果是其他用户，则没有编辑权限