# Scientific Calculator 

A comprehensive and advanced scientific calculator with a user interface inspired by Casio scientific calculators.

Built with Python and Tkinter, featuring full support for mathematical operations, symbolic algebra, plotting, De Moivre's theorem, and roots of unity.

---

## Key Features

- **Professional User Interface** inspired by classic Casio scientific calculators.  
- **Variable Support**: Define and use variables (e.g. `a=5`) in calculations.  
- **Angle Mode (Degrees / Radians)** with easy toggle button.  
- **Standard Mathematical Functions**: `sin`, `cos`, `tan`, `log`, `ln`, plus inverse functions via the SHIFT key.  
- **De Moivre's Theorem** with calculations and graphical visualization.  
- **Roots of Unity** calculation with results listing and plotting.  
- **2D Function Plotting** using SymPy's plotting capabilities.  
- **Operation History**: View last 20 performed calculations.  
- **Variable Management**: Display and reset current variables.  
- **SHIFT Mode** to activate inverse or special functions.  
- Clear screen and reset variables buttons for easy management.

---

## How to Use

1. **Run the Calculator**:  
   Execute the `calculator.py` file with Python 3.7+.

2. **Enter Expressions**:  
   - Perform direct calculations like `2+3*4`.  
   - Define variables: e.g. `a=5` then use `a*2`.  
   - Use math functions: `sin(30)`, `log(10)`, etc.  
   - Press `=` to evaluate.

3. **SHIFT Key**:  
   Toggles between normal and inverse functions (`sin` ↔ `asin`).

4. **Rad/Deg Button**:  
   Switch between radians and degrees for angle calculations.

5. **Special Buttons**:  
   - `DeMoivre`: Compute and visualize De Moivre's theorem.  
   - `Roots of Unity`: Calculate and plot roots of unity.  
   - `GRAPH`: Plot 2D functions.  
   - `HIST`: Show calculation history.  
   - `VARS`: Show current variables.  
   - `RESETVARS`: Clear all variables.  
   - `C`: Clear input field.

---

## Requirements

- Python 3.7 or higher  
- External libraries:  
  - `sympy` (symbolic mathematics and plotting)  
  - `matplotlib` (graph plotting)  
  - `numpy` (numerical computations)  

Install requirements via:

```bash
pip install sympy matplotlib numpy
