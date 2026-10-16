import streamlit as st
import sympy as sp

# Настройка страницы
st.set_page_config(page_title="AI Derivative Tutor", page_icon="📈", layout="centered")

st.title("📈 AI-Powered Derivative Tutor")
st.markdown(
    "An interactive learning assistant designed to guide students through "
    "calculus derivatives with step-by-step guidance and rules."
)

st.markdown("---")

# Секция 1: Интерактивный калькулятор производных
st.header("1. Symbolic Derivative Calculator")
expr_input = st.text_input("Enter a mathematical function f(x):", value="x**3 + 4*x**2 - 5*x + 7")

if st.button("Calculate Derivative"):
    try:
        x = sp.Symbol('x')
        expr = sp.sympify(expr_input)
        derivative = sp.diff(expr, x)
        
        st.success("Calculation Successful!")
        st.write("**Original Function $f(x)$:**")
        st.latex(sp.latex(expr))
        
        st.write("**Derivative $f'(x)$:**")
        st.latex(sp.latex(derivative))
    except Exception as e:
        st.error(f"Error parsing expression. Please check syntax (use `*` for multiplication, e.g., `3*x**2`).")

st.markdown("---")

# Секция 2: Дифференцированные задачи по уровням
st.header("2. Differentiated Practice Tasks")

level = st.radio(
    "Select Student Difficulty Level:",
    [
        "Level 1: Foundation (Power Rule & Basic Polynomials)",
        "Level 2: Standard (Product & Quotient Rules)",
        "Level 3: Advanced (Chain Rule & Trigonometric/Exponential Functions)"
    ]
)

if st.button("Generate Task & AI Scaffolding"):
    st.markdown("---")
    if "Level 1" in level:
        st.subheader("🎯 Task: Level 1 (Foundation)")
        st.write("Find the derivative of the function:")
        st.latex(r"f(x) = 5x^4 - 3x^2 + 8")
        
        with st.expander("💡 AI Pedagogical Hints & Guidance"):
            st.write("1. **Rule to apply:** Use the Power Rule $\\frac{d}{dx}[x^n] = n \\cdot x^{n-1}$.")
            st.write("2. **Step 1:** Bring the exponent to the front and multiply by the coefficient.")
            st.write("3. **Step 2:** Note that the derivative of a constant (like 8) is 0.")

    elif "Level 2" in level:
        st.subheader("🎯 Task: Level 2 (Standard)")
        st.write("Find the derivative of the function:")
        st.latex(r"f(x) = (2x^2 + 3)(x - 5)")
        
        with st.expander("💡 AI Pedagogical Hints & Guidance"):
            st.write("1. **Rule to apply:** Product Rule $\\frac{d}{dx}[u \\cdot v] = u'v + uv'$.")
            st.write("2. Identify $u = 2x^2 + 3$ and $v = x - 5$.")
            st.write("3. Compute $u'$ and $v'$ separately, then apply the formula.")

    else:
        st.subheader("🎯 Task: Level 3 (Advanced)")
        st.write("Find the derivative of the function:")
        st.latex(r"f(x) = \sin(3x^2 + 1)")
        
        with st.expander("💡 AI Pedagogical Hints & Guidance"):
            st.write("1. **Rule to apply:** Chain Rule $\\frac{d}{dx}[f(g(x))] = f'(g(x)) \\cdot g'(x)$.")
            st.write("2. Outer function: $\\sin(u)$, derivative is $\\cos(u)$.")
            st.write("3. Inner function: $u = 3x^2 + 1$, derivative is $6x$.")
            st.write("4. Multiply the outer derivative by the inner derivative.")
