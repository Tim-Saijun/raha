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

## Detection
```python
dataset_name = "flights"
dataset_dictionary = {
    "name": dataset_name,
    "path": os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "datasets", dataset_name, "dirty.csv")),
    "clean_path": os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "datasets", dataset_name, "clean.csv"))
}
app = Detection()
detection_dictionary = app.run(dataset_dictionary)
data = raha.dataset.Dataset(dataset_dictionary)
p, r, f = data.get_data_cleaning_evaluation(detection_dictionary)[:3]
print("Raha's performance on {}:\nPrecision = {:.2f}\nRecall = {:.2f}\nF1 = {:.2f}".format(data.name, p, r, f))
```
这段代码是在使用一个名为`Detection`的类来进行数据错误检测。首先，创建了一个`Detection`类的实例`app`。然后，调用了`app`的`run`方法来运行错误检测，输入是一个名为`dataset_dictionary`的数据集字典，输出是一个名为`detection_dictionary`的字典，其中包含了检测到的数据错误。最后，使用`dataset_dictionary`创建了一个`raha.dataset.Dataset`实例`data`。

`Detection`类的`run`方法是这个类的主要方法，它负责执行错误检测的整个过程。这个过程包括以下步骤：

1. 初始化数据集：创建一个`Dataset`实例，这个实例包含了数据集的所有信息。

2. 运行错误检测策略：运行一系列的错误检测策略来找出可能的数据错误。

3. 生成特征向量：为每个数据元素生成一个特征向量，这个特征向量描述了这个元素的各种属性。

4. 构建层次聚类模型：使用特征向量构建一个层次聚类模型，这个模型将相似的数据元素聚集在一起。

5. 迭代的基于聚类的采样和标记：反复采样和标记数据元素，直到标记的数据元素数量达到预设的标记预算。

6. 通过聚类传播用户标签：将用户的标签从一个数据元素传播到同一个聚类中的其他数据元素。

7. 训练和测试分类模型：使用标记的数据元素训练一个分类模型，然后使用这个模型预测未标记的数据元素的标签。

8. 存储结果：如果设置了保存结果，那么将结果存储起来。

这个过程的每一步都可能打印出详细的日志信息，这取决于`VERBOSE`属性的设置。最后，`run`方法返回一个字典，这个字典的键是数据元素的位置，值是检测到的错误。

## Correction
```python
dataset_name = "flights"
dataset_dictionary = {
    "name": dataset_name,
    "path": os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "datasets", dataset_name, "dirty.csv")),
    "clean_path": os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "datasets", dataset_name, "clean.csv"))
}
data = raha.dataset.Dataset(dataset_dictionary)
data.detected_cells = dict(data.get_actual_errors_dictionary())
app = Correction()
correction_dictionary = app.run(data)
p, r, f = data.get_data_cleaning_evaluation(correction_dictionary)[-3:]
print("Baran's performance on {}:\nPrecision = {:.2f}\nRecall = {:.2f}\nF1 = {:.2f}".format(dataname, p, r, f))
```
这段Python代码是用来进行数据错误修正的。首先，它定义了一个名为`dataset_name`的变量，然后创建了一个名为`dataset_dictionary`的字典，这个字典包含了数据集的名称和路径。然后，使用`dataset_dictionary`创建了一个`raha.dataset.Dataset`实例`data`，并将实际错误的字典设置为`data.detected_cells`。接着，创建了一个`Correction`类的实例`app`，并调用了`app`的`run`方法来运行错误修正，输入是`data`，输出是一个名为`correction_dictionary`的字典，其中包含了修正的数据错误。最后，使用`data.get_data_cleaning_evaluation(correction_dictionary)`方法获取了修正的精度、召回率和F1分数，并打印出了这些评估指标。

`Correction`类的`run`方法是这个类的主要方法，它负责执行错误修正的整个过程。这个过程包括以下步骤：

1. 初始化数据集：创建一个`Dataset`实例，这个实例包含了数据集的所有信息。

2. 初始化错误修正模型：初始化一些用于错误修正的模型。

3. 迭代的元组采样、标记和学习：反复采样和标记元组，直到标记的元组数量达到预设的标记预算。然后，更新模型，并预测修正。

4. 存储结果：如果设置了保存结果，那么将结果存储起来。

这个过程的每一步都可能打印出详细的日志信息，这取决于`VERBOSE`属性的设置。最后，`run`方法返回一个字典，这个字典的键是数据元素的位置，值是修正的数据错误。