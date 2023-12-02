# Raha和她的妹妹Baran
检测和纠正错误值是数据清洗的关键步骤。错误检测/纠正系统通常需要用户以完整性约束或统计参数的形式提供输入配置。然而，为每个新数据集提供一套完整且正确的配置是繁琐且容易出错的，因为用户必须事先了解数据集和数据清洗系统。

Raha和Baran是新的无配置错误检测和纠正系统。在抽象层面上，Raha和Baran都遵循同样的新型两步错误检测/纠正任务公式，实现了高精度和召回率。首先，每个基础错误检测器/纠正器生成一组初始的潜在数据错误/纠正。这一步特别增加了错误检测/纠正任务的可达召回率上限。然后，Raha/Baran以半监督的方式将这些基础错误检测器/纠正器的输出集成到一个最终的数据错误/纠正集中。实际上，Raha/Baran会迭代地要求用户注释一个元组，即标记/修复一些数据错误。Raha/Baran学习将用户提供的错误检测/纠正示例推广到数据集的其余部分。这一步特别保留了错误检测/纠正任务的高精度。此外，两个系统都可以利用历史数据，根据迁移学习优化当前数据集的数据清洗任务。

## 安装
要安装Raha和Baran，你可以运行：
```console
pip3 install raha
```

使用github仓库安装Raha和Baran：
```console
git clone git@github.com:BigDaMa/raha.git
pip3 install -e raha
```

要卸载它们，你可以运行：
```console
pip3 uninstall raha
```

## 使用
运行Raha和Baran很简单！
   - **基准测试**：如果你有一个脏数据集和其对应的干净数据集，并且你想对Raha和Baran进行基准测试，请查看`raha/benchmark.py`，`raha/detection.py`和`raha/correction.py`中的示例代码。
   - **使用Raha和Baran进行交互式数据清洗**：如果你有一个脏数据集，并且你想交互式地检测和纠正数据错误，请查看`raha`文件夹中的交互式Jupyter笔记本。Jupyter笔记本提供了图形用户界面。
   ![数据注释](pictures/ui.png)   
   ![有前途的策略](pictures/ui_strategies.png)   
   ![深入研究](pictures/ui_clusters.png)   
   ![仪表板](pictures/ui_dashboard.png) 

提示：
仓库内的预训练模型只是使用笔记本的一个示例。请不要依赖它进行你的实验。如果你需要使用Baran的预训练模型，请下载维基百科的修订历史并使用Baran训练模型。

