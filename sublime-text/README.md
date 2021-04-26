## Sublime Text

- [官网](https://www.sublimetext.com)
- [下载](https://www.sublimetext.com/3)

### 说明

- 简单的文本编辑器
- 免费使用

### 快捷键

- `Ctrl` + `B` 运行
- `Shift` + `Ctrl` + `B` 运行于

### 指定 Python 命令

- Tools
    - Build System
        - New Build System
            ```
            {
                "cmd": ["python3", "-u", "$file"],
            }
            ```

### 问题

- 文件未保存时执行

```
/usr/bin/python3: can't find '__main__' module in ''
[Finished in 0.1s with exit code 1]
```

