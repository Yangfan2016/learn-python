## Day-001

### Notes

- 注释

```py

# 单行注释

'''

多行注释

'''

"""

多行注释

"""

```

- pylint

在代码的开头加上注释，

```py

# pylint: disable=no-member

```

解决 pylint [E1101](http://pylint-messages.wikidot.com/messages:e1101) 误报错误（在当报错的对象是动态创建的，并且确实是在访问的同时已经存在的时候pylint仍然会报出E1101的错误）


### Experience
1. 翻译

```
Beautiful is better than ugly.

美比丑好

Explicit is better than implicit.

显式比隐式好

Simple is better than complex.

简单比复杂好

Complex is better than complicated.

复杂比难懂好

Flat is better than nested.

平铺比嵌套好

Sparse is better than dense.

稀疏比密集好

Readability counts.

可读性很重要

Special cases aren't special enough to break the rules. Although practicality beats purity.

特殊例子不足以破坏规则，尽管实用性打败了纯洁性

Errors should never pass silently. Unless explicitly silenced.

错误永远不要沉默忽视，除非故意这么做

In the face of ambiguity, refuse the temptation to guess.

面对模棱两可的情况，拒绝猜想的诱惑

There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch.

应该只有一种（并且更好的唯一一种）显而易见的方法去解决问题，尽管这种方法并不是第一个显而易见的，但你不是 python 作者

Now is better than never. Although never is often better than *right* now.

现在做总比永远不做好，尽管不做总比现在做 *正确*

If the implementation is hard to explain, it's a bad idea.

如果实现起来很难解释，那么它就是坏主意

If the implementation is easy to explain, it may be a good idea.

如果实现起来很容易解释，那么它就是好主意

Namespaces are one honking great idea -- let's do more of those!

命名空间是一个绝妙的好主意，让我们多加利用

```
