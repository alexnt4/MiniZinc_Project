
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
final-project/
├── src/
│   ├── models/
│   │   ├── model.mzn       # MiniZinc Model
│   │   ├── data.txt        # Example input data
│   │   └── output.txt      # Example output data
│   ├── interface/
│   │   ├── main.py         # Main Python script
│   │   └── ui.py           # Graphical interface code
├── docs/
│   ├── report.pdf          # Technical report in IEEE format
├── tests/
│   ├── test_model.py       # Unit tests for the model
├── README.md
└── requirements.txt        # Project dependencies
```

---

## 📊 Example Execution

### Input
```txt
3
6 8
8 4
10 10
15
...
4
```

### Expected Output
```txt
120
240
6 8
8 4
10 10
2 3
5 5
12 1
13 15
```

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/final-project.git
   cd final-project
   ```
2. Install dependencies using `uv`:
   ```bash
   uv install
   ```
3. Ensure [MiniZinc](https://www.minizinc.org/) is installed and properly configured.


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