# DevOps与部署

### 容器化

| 英文                 | 音标                     | 中文           | 例句                 |
| -------------------- | ------------------------ | -------------- | -------------------- |
| Docker               | /ˈdɑːkər/                | Docker         | Docker container     |
| container            | /kənˈteɪnər/             | 容器           | Container runtime    |
| image                | /ˈɪmɪdʒ/                 | 镜像           | Docker image         |
| Dockerfile           | /ˈdɑːkərfaɪl/            | Dockerfile     | Dockerfile           |
| layer                | /ˈleɪər/                 | 层             | Image layer          |
| base-image           | /beɪs ˈɪmɪdʒ/            | 基础镜像       | Base image           |
| tag                  | /tæɡ/                    | 标签           | Image tag            |
| registry             | /ˈredʒɪstri/             | 镜像仓库       | Docker registry      |
| repository           | /rɪˈpɑːzətɔːri/          | 仓库           | Image repository     |
| pull                 | /pʊl/                    | 拉取           | Pull image           |
| push                 | /pʊʃ/                    | 推送           | Push image           |
| build                | /bɪld/                   | 构建           | Build image          |
| run                  | /rʌn/                    | 运行           | Run container        |
| start                | /stɑːrt/                 | 启动           | Start container      |
| stop                 | /stɑːp/                  | 停止           | Stop container       |
| restart              | /ˌriːˈstɑːrt/            | 重启           | Restart container    |
| remove               | /rɪˈmuːv/                | 移除           | Remove container     |
| exec                 | /ˈeksek/                 | 执行           | Exec into container  |
| logs                 | /lɔːɡz/                  | 日志           | Container logs       |
| inspect              | /ɪnˈspekt/               | 检查           | Inspect container    |
| volume               | /ˈvɑːljuːm/              | 卷             | Docker volume        |
| mount                | /maʊnt/                  | 挂载           | Mount volume         |
| bind-mount           | /baɪnd maʊnt/            | 绑定挂载       | Bind mount           |
| network              | /ˈnetwɜːrk/              | 网络           | Docker network       |
| bridge               | /brɪdʒ/                  | 桥接           | Bridge network       |
| host                 | /hoʊst/                  | 主机           | Host network         |
| overlay              | /ˈoʊvərleɪ/              | 覆盖           | Overlay network      |
| port-mapping         | /pɔːrt ˈmæpɪŋ/           | 端口映射       | Port mapping         |
| expose               | /ɪkˈspoʊz/               | 暴露           | Expose port          |
| environment-variable | /ɪnˈvaɪrənmənt ˈveriəbl/ | 环境变量       | Environment variable |
| entrypoint           | /ˈentripɔɪnt/            | 入口点         | Container entrypoint |
| CMD                  | /ˌsiː em ˈdiː/           | 命令           | CMD instruction      |
| WORKDIR              | /ˈwɜːrkdɪr/              | 工作目录       | Working directory    |
| COPY                 | /ˈkɑːpi/                 | 复制           | COPY instruction     |
| ADD                  | /æd/                     | 添加           | ADD instruction      |
| multi-stage          | /ˈmʌlti steɪdʒ/          | 多阶段         | Multi-stage build    |
| docker-compose       | /ˈdɑːkər kəmˈpoʊz/       | Docker Compose | Docker Compose       |
| service              | /ˈsɜːrvɪs/               | 服务           | Compose service      |
| stack                | /stæk/                   | 栈             | Docker stack         |
| swarm                | /swɔːrm/                 | 集群           | Docker Swarm         |

### Kubernetes

| 英文               | 音标                     | 中文            | 例句                      |
| ------------------ | ------------------------ | --------------- | ------------------------- |
| Kubernetes         | /ˌkuːbərˈnetɪs/          | Kubernetes      | Kubernetes cluster        |
| K8s                | /keɪ eɪts/               | K8s             | K8s abbreviation          |
| cluster            | /ˈklʌstər/               | 集群            | K8s cluster               |
| node               | /noʊd/                   | 节点            | Worker node               |
| master             | /ˈmæstər/                | 主节点          | Master node               |
| control-plane      | /kənˈtroʊl pleɪn/        | 控制平面        | Control plane             |
| pod                | /pɑːd/                   | Pod             | Kubernetes pod            |
| container          | /kənˈteɪnər/             | 容器            | Pod container             |
| deployment         | /dɪˈplɔɪmənt/            | 部署            | Deployment resource       |
| replica            | /ˈreplɪkə/               | 副本            | Pod replica               |
| ReplicaSet         | /ˈreplɪkə set/           | 副本集          | ReplicaSet                |
| StatefulSet        | /ˈsteɪtfəl set/          | 有状态集        | StatefulSet               |
| DaemonSet          | /ˈdiːmən set/            | 守护集          | DaemonSet                 |
| Job                | /dʒɑːb/                  | 任务            | Batch job                 |
| CronJob            | /krɑːn dʒɑːb/            | 定时任务        | Cron job                  |
| service            | /ˈsɜːrvɪs/               | 服务            | K8s service               |
| ClusterIP          | /ˈklʌstər aɪ piː/        | 集群IP          | ClusterIP service         |
| NodePort           | /noʊd pɔːrt/             | 节点端口        | NodePort service          |
| LoadBalancer       | /loʊd ˈbælənsər/         | 负载均衡器      | LoadBalancer service      |
| Ingress            | /ˈɪnɡres/                | 入口            | Ingress controller        |
| ConfigMap          | /kənˈfɪɡ mæp/            | 配置映射        | ConfigMap                 |
| Secret             | /ˈsiːkrət/               | 密钥            | Secret resource           |
| volume             | /ˈvɑːljuːm/              | 卷              | Persistent volume         |
| PV                 | /ˌpiː ˈviː/              | 持久卷          | Persistent Volume         |
| PVC                | /ˌpiː viː ˈsiː/          | 持久卷声明      | Persistent Volume Claim   |
| StorageClass       | /ˈstɔːrɪdʒ klæs/         | 存储类          | Storage class             |
| namespace          | /ˈneɪmspeɪs/             | 命名空间        | K8s namespace             |
| label              | /ˈleɪbl/                 | 标签            | Pod label                 |
| selector           | /sɪˈlektər/              | 选择器          | Label selector            |
| annotation         | /ˌænəˈteɪʃn/             | 注解            | Resource annotation       |
| resource-quota     | /ˈriːsɔːrs ˈkwoʊtə/      | 资源配额        | Resource quota            |
| limit-range        | /ˈlɪmɪt reɪndʒ/          | 限制范围        | Limit range               |
| horizontal-scaling | /ˌhɔːrɪˈzɑːntl ˈskeɪlɪŋ/ | 水平扩展        | Horizontal Pod Autoscaler |
| HPA                | /ˌeɪtʃ piː ˈeɪ/          | 水平Pod自动扩展 | HPA                       |
| liveness-probe     | /ˈlaɪvnəs proʊb/         | 存活探针        | Liveness probe            |
| readiness-probe    | /ˈredinəs proʊb/         | 就绪探针        | Readiness probe           |
| startup-probe      | /ˈstɑːrtʌp proʊb/        | 启动探针        | Startup probe             |
| rolling-update     | /ˈroʊlɪŋ ʌpˈdeɪt/        | 滚动更新        | Rolling update            |
| rollback           | /ˈroʊlbæk/               | 回滚            | Deployment rollback       |
| kubectl            | /ˈkuːbˌsiː tiː el/       | kubectl         | kubectl command           |

### CI/CD

| 英文                   | 音标                       | 中文              | 例句                   |
| ---------------------- | -------------------------- | ----------------- | ---------------------- |
| CI/CD                  | /ˌsiː aɪ ˌsiː ˈdiː/        | 持续集成/持续部署 | CI/CD pipeline         |
| continuous-integration | /kənˈtɪnjuəs ˌɪntɪˈɡreɪʃn/ | 持续集成          | Continuous integration |
| continuous-delivery    | /kənˈtɪnjuəs dɪˈlɪvəri/    | 持续交付          | Continuous delivery    |
| continuous-deployment  | /kənˈtɪnjuəs dɪˈplɔɪmənt/  | 持续部署          | Continuous deployment  |
| pipeline               | /ˈpaɪplaɪn/                | 流水线            | Build pipeline         |
| stage                  | /steɪdʒ/                   | 阶段              | Pipeline stage         |
| job                    | /dʒɑːb/                    | 任务              | CI job                 |
| build                  | /bɪld/                     | 构建              | Build job              |
| test                   | /test/                     | 测试              | Test stage             |
| deploy                 | /dɪˈplɔɪ/                  | 部署              | Deploy stage           |
| artifact               | /ˈɑːrtɪfækt/               | 构建产物          | Build artifact         |
| trigger                | /ˈtrɪɡər/                  | 触发器            | Pipeline trigger       |
| webhook                | /ˈwebhʊk/                  | Webhook           | Git webhook            |
| poll                   | /poʊl/                     | 轮询              | SCM polling            |
| Jenkins                | /ˈdʒeŋkɪnz/                | Jenkins           | Jenkins CI             |
| GitLab-CI              | /ˈɡɪtlæb siː aɪ/           | GitLab CI         | GitLab CI/CD           |
| GitHub-Actions         | /ˈɡɪthʌb ˈækʃnz/           | GitHub Actions    | GitHub Actions         |
| Travis-CI              | /ˈtrævɪs siː aɪ/           | Travis CI         | Travis CI              |
| CircleCI               | /ˈsɜːrkl siː aɪ/           | Circle CI         | Circle CI              |
| agent                  | /ˈeɪdʒənt/                 | 代理              | Build agent            |
| runner                 | /ˈrʌnər/                   | 运行器            | GitLab runner          |
| executor               | /ɪɡˈzekjətər/              | 执行器            | Pipeline executor      |
| workspace              | /ˈwɜːrkspeɪs/              | 工作空间          | Build workspace        |
| checkout               | /ˈtʃekaʊt/                 | 检出              | Checkout code          |
| compile                | /kəmˈpaɪl/                 | 编译              | Compile stage          |
| unit-test              | /ˈjuːnɪt test/             | 单元测试          | Unit test              |
| integration-test       | /ˌɪntɪˈɡreɪʃn test/        | 集成测试          | Integration test       |
| code-coverage          | /koʊd ˈkʌvərɪdʒ/           | 代码覆盖率        | Code coverage          |
| static-analysis        | /ˈstætɪk əˈnæləsɪs/        | 静态分析          | Static code analysis   |
| SonarQube              | /ˈsoʊnɑːr kjuːb/           | SonarQube         | SonarQube analysis     |