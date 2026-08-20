# 曜语 YaoLang

> 关键字100%中文的系统编程语言

## 简介

曜语是一门关键字全部中文的编译型编程语言。源代码编译为C，再通过系统C编译器生成原生机器码。

## 特性

- 100%中文关键字: 函数、变量、若、当、对于、匹配、结构、枚举
- 原生编译: .耀 -> C代码 -> 可执行文件
- 静态类型: 整数、浮点、布尔、文本、字符
- Android APK构建: javac + d8 + jarsigner
- 40+内建函数
- 单文件编译器: ~3700行C代码

## 快速开始

    cc -O2 -o yaoc src/yaolang.c -lm
    echo '函数 主函数() { _yao_print_s("你好!"); _yao_print(42) }' > hello.耀
    ./yaoc hello.耀
    ./hello

## 教程

- [官方网站](https://a737812.github.io/yaolang)
- [教程下载](docs/download/)

## License

MIT
