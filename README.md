# 格雷科技6预算器

计算格雷科技6合成物品所需原料的工具

## 合成表

合成表以json形式存放在craft/内，文件名为所合成物品

json文件格式

```
some_item.json
{
	"<some_subitem>": {
		"": <count>,
		"certain_material": <count>,
		...
	},

	"<another_subitem>": {
		"certain_material": <count>,
		...
	},

	...
}
```

材质对应字符串键值为空代表通配材质

当合成表内有特定材质物品时，通配材质会被覆盖

如果一个物品作为原料，即不应再作为合成物品，则其合成表文件应为

```
end.json
{}
```

具体例子参考craft/内文件

## 使用说明

要获取n个特定物品所需原料预算表，可以调用
```python
calc(name, count, material='')
```

calc函数会递归地计算出所需原料，返回值为存储预算表的字典

要添加合成表，可以手动编辑craft/下json文件，也可以调用
```python
add(name, craft_dict)
```

dict为存储合成表的字典，和合成表json格式类似，尽量使用通配材质

## TODO

1. 交互UI

2. 优化plus的实现

3. 导入合成表

