<div align="center">

# 🐍✨ Python

> **Python is a high-level, general-purpose programming language** known for its simple syntax, readability, and ease of learning.

### 👨‍💻 Created by Guido van Rossum | 📅 First Released in 1991

</div>

---

## 📌 About Python

| ✨ | Details |
|---|---|
| 🟢 | Python is **open-source** and freely available. |
| 🔤 | It is a **dynamically typed** language. |
| 📖 | Python has a simple and readable syntax. |
| 📄 | Python programs use the **.py** file extension. |
| 🧩 | Python supports **procedural, object-oriented, and functional programming**. |

---

## 🚀 Uses of Python

Python is widely used in many fields:

| # | 💡 Field | 🛠️ Examples / Technologies |
|---:|---|---|
| 1 | 🌐 **Web Development** | Django, Flask, FastAPI |
| 2 | 📊 **Data Analysis** | NumPy, Pandas |
| 3 | 🔬 **Data Science** | NumPy, Pandas, SciPy |
| 4 | 🤖 **Artificial Intelligence & Machine Learning** | Scikit-learn, Keras, Linear Regression |
| 5 | ⚙️ **Automation & Scripting** | Python Scripts, Task Automation |
| 6 | 💻 **Software Development** | Desktop & Application Development |
| 7 | 🧪 **Scientific Computing** | SciPy, NumPy |
| 8 | 🛡️ **Cybersecurity** | Security Tools & Automation |

---

## 💻 Simple Python Example

```python
print("Hello, World!")
```

### 📤 Output

```text
Hello, World!
```

---

## 🐍 Ways to Run Python

Python programs can be executed in different environments:

> 🔹 **Python Interpreter**  
> 🔹 **VS Code**  
> 🔹 **Python IDLE**  
> 🔹 **Jupyter Notebook**  
> 🔹 **Command Prompt / Terminal**

## 🐍 REPL

**REPL** stands for:

> 🔹 **R** = Read  
> 🔹 **E** = Evaluate  
> 🔹 **P** = Print  
> 🔹 **L** = Loop

REPL allows us to execute Python code directly in the Python interpreter.

Example:

```text
>>> name = "brijesh"
>>> print(name)
brijesh

>>> a = 10
>>> b = 20
>>> print("addition of numbers is :", a + b)
addition of numbers is : 30
```

---

## 🧮 Python Variables

A variable is used to store a value in Python.

Example:

```python
a = 20
b = 20
c = "hi"
d = "kyu"
e = """hi noori"""
f = 10.6565
```

Python variables can store different types of values.

---

## 🖥️ Creating a Windows Application

Python can be used to create a graphical Windows application using the `tkinter` module.

```python
import tkinter as tk

# create a windows screen
root = tk.Tk()

# create a title of windows app
root.title("vaidehi notepad app")

# create a geometry
root.geometry("550x468")

# display windows app
tk.mainloop()
```
--- 

## ⭐ Why Learn Python?

Python is popular because it is:

- 🎯 **Easy to Learn**
- ✍️ **Easy to Read and Write**
- 🔄 **Versatile**
- 🌍 **Open-Source**
- 👥 **Supported by a Large Community**
- 📚 **Rich in Libraries and Frameworks**

> 💡 Python is especially useful for beginners because its syntax is clean and relatively close to natural language.

---

## 📄 Python File Extension

> 🐍 Python source files use the **`.py`** extension.

---

## 💬 Comments in Python

Comments are used to add explanations or notes to Python code. They are ignored during normal program execution.

### 🔹 Single-Line Comment

A single-line comment starts with the `#` symbol.

```python
# Hello World
print("Hello World")
```

### 🔹 Multi-Line Comments

Python does not have a dedicated multi-line comment syntax. Triple-quoted strings are commonly used for multi-line documentation or text blocks.

```python
'''
Hello World
This is a multi-line text block.
'''
```

> 💡 **Note:** For functions, classes, and modules, triple-quoted strings are commonly used as **docstrings**.

---

## 📦 What is Module?

> 🧩 A module is that file which is run after saving it as **.py**.
>
> ♻️ Modules are reusable.

### 🔹 Sub Types

1. 👨‍💻 **User-Defined** = Defined by users, can be named by the user, and is reusable.

```python
mymodule.py
import mymodule
mymodule.greet()
def greet():
    print("Hello from my module!")

import mymodule
mymodule.greet()
```

2. 🐍 **Pre-Defined** = system defined, already defined so no need to install because they are pre-defined

```python
import sys
result = sys.version_info //used to print version of python in detail
print(result)

or

import math
num = int(input("Enter a Number"))
print(math.pow(num,2))

or

import datetime
print(datetime.datetime.now)

or

import calendar
print(calendar.calendar(2026))
print(calendar.calendar.month(2026,9))

or

import random
print(random.randomint(1,10))

```

3. 📦 **Third-Party** = pre made modules made by other people or users
> What is pip : python installp ackage , used to install package or module 
<div align="center">

### 🐍✨ Python • Learn • Build • Create ✨🐍

</div>
