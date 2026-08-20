#!/usr/bin/env python3
"""生成教程TXT + HTML教程页面"""
import os, base64

DL = os.path.join(os.path.dirname(__file__), "docs", "download")
TU = os.path.join(os.path.dirname(__file__), "docs", "tutorials")
os.makedirs(DL, exist_ok=True)
os.makedirs(TU, exist_ok=True)

# 教程内容（纯ASCII + 中文，避免shell转义问题）
tutorials = {
    "01-getting-started": [
        "曜语 YaoLang 教程 01: 快速入门",
        "1. 安装: cc -O2 -o yaoc yaolang.c -lm",
        "2. Hello World (hello.耀):",
        '   函数 主函数() { _yao_print_s("你好!"); _yao_print(42) }',
        "3. 编译运行: ./yaoc hello.耀 && ./hello",
        "4. 输出: 你好! / 42",
        "5. 查看C代码: ./yaoc hello.耀 -S",
    ],
    "02-variables-types": [
        "曜语 YaoLang 教程 02: 变量与类型",
        "类型: 整数 浮点 布尔 文本 字符 空",
        "可变: 变量 x: 整数 = 42",
        "不可变: 令 PI: 浮点 = 3.14",
        "自动推导: 变量 y = 100  ## 推导为整数",
        "运算符: + - * / % == != < > <= >= && || !",
    ],
    "03-control-flow": [
        "曜语 YaoLang 教程 03: 控制流",
        "条件: 若 cond { } 否则 { }",
        "当循环: 当 cond { }",
        "对于循环: 对于 i 在 0..100 { }",
        "跳出: 跳出  继续: 继续",
        "匹配: 匹配 val { 1 => {} _ => {} }",
    ],
    "04-functions": [
        "曜语 YaoLang 教程 04: 函数与递归",
        "定义: 函数 add(a:整数, b:整数):整数 { 返回 a + b }",
        "递归: 函数 fib(n:整数):整数 {",
        "  若 n <= 1 { 返回 n }",
        "  返回 fib(n-1) + fib(n-2)",
        "}",
        "入口: 函数 主函数() { _yao_print(fib(10)) }",
    ],
    "05-structs-enums": [
        "曜语 YaoLang 教程 05: 结构体与枚举",
        "结构 Point { x: 整数  y: 整数 }",
        "实现 Point {",
        "  函数 距离(self): 整数 { 返回 self.x*self.x + self.y*self.y }",
        "}",
        "枚举 Color { 红 = 0, 绿, 蓝 }",
        '匹配 c { Color.红 => { _yao_print_s("红") } _ => { } }',
    ],
    "06-strings-io": [
        "曜语 YaoLang 教程 06: 字符串与文件I/O",
        "输出: _yao_print_s(s) _yao_print(n)",
        "输入: _yao_read_line()",
        "字符串: _yao_str_len(s) _yao_str_concat(a,b) _yao_str_cmp(a,b)",
        "转换: _yao_int_to_str(n) _yao_str_to_int(s)",
        "文件: _yao_file_open(path,mode) _yao_file_write(fp,s) _yao_file_close(fp)",
    ],
    "07-runtime-library": [
        "曜语 YaoLang 教程 07: 内建函数库",
        "输出: _yao_print_s _yao_print _yao_print_c",
        "输入: _yao_read_line _yao_read_char",
        "字符串: _yao_str_len _yao_str_concat _yao_str_cmp _yao_int_to_str",
        "文件: _yao_file_open _yao_file_read _yao_file_write _yao_file_close",
        "系统: _yao_exit _yao_clock _yao_rand _yao_srand",
        "GUI: _yao_x11_init _yao_x11_create_window _yao_x11_draw_text",
    ],
    "08-android-build": [
        "曜语 YaoLang 教程 08: 构建Android APK",
        "步骤:",
        "  1. javac -classpath android.jar MainActivity.java",
        "  2. java -cp d8.jar com.android.tools.r8.D8 --output apk/ *.class",
        "  3. zip -> app-unsigned.apk (AndroidManifest.xml + classes.dex)",
        "  4. keytool -genkey -keystore debug.keystore",
        "  5. jarsigner -signedjar yaolang_app.apk app-unsigned.apk",
        "安装: adb install yaolang_app.apk 或复制到手机",
    ],
    "09-compiler-internals": [
        "曜语 YaoLang 教程 09: 编译器内部原理",
        "架构: .耀 -> 词法 -> 语法 -> 语义 -> C代码 -> gcc -> 可执行文件",
        "编译器: yaolang.c 约3700行C代码",
        "词法: UTF-8源码 -> Token序列 (关键字/标识符/字面量/运算符)",
        "语法: Token -> AST (抽象语法树)",
        "语义: 类型检查 + 作用域管理",
        "代码生成: AST -> C代码 (中文标识符 -> Unicode C标识符)",
        "自举: test/yao_lexer.耀 可以解析自身源文件",
    ],
    "10-editor-setup": [
        "曜语 YaoLang 教程 10: 编辑器使用教程",
        "Android上使用曜语:",
        "  1. 安装 Operit 或 Termux",
        "  2. 编译: cc -O2 -o yaoc yaolang.c -lm",
        "  3. 编写: nano hello.耀",
        "  4. 编译: ./yaoc hello.耀",
        "  5. 运行: ./hello",
        "下载: github.com/a737812/yaolang/releases",
    ],
}

# 生成TXT文件
all_content = ""
for name, lines in tutorials.items():
    content = "======================================\n" + "\n".join(lines) + "\n======================================\n"
    with open(os.path.join(DL, f"{name}.txt"), "w") as f:
        f.write(content)
    all_content += content + "\n\n"
    print(f"  {name}.txt ({len(content)} bytes)")

with open(os.path.join(DL, "all-tutorials.txt"), "w") as f:
    f.write(all_content)
print(f"  all-tutorials.txt ({len(all_content)} bytes)")

# 生成简单的HTML教程页面
for name, lines in tutorials.items():
    title = lines[0]
    body = "<br>\n".join(lines[1:])
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><title>{title}</title>
<style>
body{{font-family:sans-serif;max-width:700px;margin:40px auto;padding:0 20px;background:#0d1117;color:#e6edf3}}
a{{color:#58a6ff}}h1{{color:#f0883e}}
pre{{background:#161b22;padding:16px;border-radius:8px;overflow-x:auto}}
.back{{margin-bottom:20px}}
</style></head>
<body>
<p class="back"><a href="../index.html">← 返回首页</a></p>
<h1>{title}</h1>
<p>{body}</p>
</body></html>"""
    with open(os.path.join(TU, f"{name}.html"), "w") as f:
        f.write(html)

print(f"\n全部生成完成: {len(tutorials)} 篇教程")