## 项目拆分
- 目的
    - 解耦和
    - 代码结构更清晰
    
#### 拆分方案
- 一拆六
- 以前就一个manage文件
    - manage进行全局控制
    - 在应用初始化做初始化
        - 初始化配置
        - 初始化路由
        - 初始化第三方
    - 配置文件
        - 配置项目所需各种信息
    - 视图函数
        - 用来处理业务逻辑，协调模板和模型
    - 模型文件
        - 定义模型
    - 外部扩展
        - 统一管理扩展
        
        
#### 环境
- 开发环境
    - 开发人员专用环境
- 测试环境
    - 测试环境和开发环境是不一样的
    - 它测试的时候，指的是你送测版本
- 演示环境
    - 无限接近于线上环境的
    - 要让产品确认
- 线上环境
    - 生产环境
    - 真实用户环境
    - 深夜三点
    
    
    
#### 项目结构
- manage.py             用来控制程序的
- App/__init__          初始化文件
    - 初始化整个Flask对象，以及Flask所用的各种插件
- App/settings          项目配置文件
    - 配置整个项目运行环境
- App/ext
    - 项目的扩展库
    - 第三方扩展库打包处理
- App/views
    - 视图函数
    - 处理业务逻辑
    - 协调模板和模型之间的关系
- App/models
    - 模型
    - 定义模型结构
    - 获得数据库中的表的关系映射
    
    
#### 数据迁移
- 将模型映射到数据库中
- 使用flask-migrate库
- 安装，使用
    - pip install flask-migrate
    - 初始化  需要使用app和数据库进行初始化  migrate = Migrate(app, db)
    - 配置flask-script的命令
        - manager.add_command('db', MigrateCommand)
- 指令使用
    - python manage.py db init
        - init 初始化指令，仅可调用一次
    - migrate
        - 生成迁移文件
        - 内部迁移文件使用了链表来关联关系
    - upgrade
        - 执行迁移文件
        - 数据库内容升级
        - --message MSG 对迁移添加日志
    - downgrade
        - 执行迁移文件
        - 数据库降级
        - 相当于后悔药
    - --help
        - 帮助文档    
    