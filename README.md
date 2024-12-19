
# 🌟 Final Project: Complexity and Optimization

This project aims to find the best locations for new Systems Engineering programs, maximizing social and economic impact within a mathematically modeled environment.

---

## 📋 Problem Description

The challenge involves:

- **Placing new educational programs** on a Cartesian plane of size \( n 	imes n \), ensuring:
  - Maximum distance from current locations.
  - Population segment covered ≥ 25.
  - Business environment ≥ 20.

### 🔍 Input Data
1. Coordinates of current locations.
2. Size of the Cartesian plane (\( n 	imes n \)).
3. Matrices of population segments and business environment.
4. Number of new locations to propose.

### 🛠️ Proposed Solution
- **MiniZinc Model** to solve the optimization problem.
- **Python Interface** for interaction and visualization.
- **Standard Outputs**:
  - Total gain before and after adding new locations.
  - Coordinates of proposed locations.

---

## 🚀 Features

- **Mathematical Optimization**: Maximizes social and economic impact.
- **Graphical Interface**: Input selection and results visualization.
- **Python-MiniZinc Integration**: Fast and scalable solutions.

---

## 📂 Project Structure

```
project/
├── src/
│   ├── models/
│   │   ├── model.mzn       # MiniZinc Model
│   ├── interface/
│   │   ├── mainwindow.py   # Main Python script
│   │   └── __init__.py     # Initialization script
├── data/
│   ├── data3.dzn           # Data file
│   ├── data4.dzn           # Data file
│   ├── data5.dzn           # Data file
│   └── data6.dzn           # Data file
├── docs/
│   ├── Informe proyecto 2 - ADA.pdf  # Project report
├── README.md
├── requirements.txt        # Project dependencies


```

---


## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/alexnt4/MiniZinc_Project
   ```

2. Ensure [MiniZinc](https://www.minizinc.org/) is installed and properly configured.

3. Create an enviroment with `uv env`

4. Activate the enviroment with `source .venv/bin/activate`

5. Install dependencies using `uv`:
   ```bash
   uv pip install -r requirements.txt
   ```

6. Use with `uv run mainwindow`


---

## 🌐 Useful Links

- [MiniZinc Documentation](https://docs.minizinc.org/en/stable/)
- [IEEE Format](https://www.ieee.org/conferences/publishing/templates.html)

---

## 👥 Authors

- **Alex** ([GitHub](https://github.com/alexnt4))


---

## 🏆 Acknowledgments

Special thanks to **Carlos Andres Delgado S.** for his guidance and foundational contributions to this project.

---

Feel free to customize it as needed! 😊