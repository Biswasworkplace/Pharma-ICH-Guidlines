import streamlit as st

from calculations.yield_calc import calculate_yield
from calculations.molarity import calculate_molarity
from calculations.impurity import impurity_percentage
from calculations.ppm_pde import pde_compliance
from calculations.solvent_recovery import solvent_recovery

st.set_page_config(page_title="Pharma Calculations Toolkit", layout="centered")

st.title("🧮 Pharma Calculations Toolkit")
st.write("API R&D | QA | Regulatory Calculators")

calculator = st.sidebar.selectbox(
    "Select Calculator",
    [
        "Reaction Yield",
        "Molarity",
        "Impurity Percentage (HPLC)",
        "Residual Solvent PDE Check",
        "Solvent Recovery"
    ]
)

# ------------------- Reaction Yield -------------------
if calculator == "Reaction Yield":
    st.header("⚗️ Reaction Yield Calculation")

    actual = st.number_input("Actual Yield", min_value=0.0)
    theoretical = st.number_input("Theoretical Yield", min_value=0.0)

    if st.button("Calculate Yield"):
        if theoretical == 0:
            st.error("Theoretical yield cannot be zero")
        else:
            result = calculate_yield(actual, theoretical)
            st.success(f"Reaction Yield = {result:.2f} %")

# ------------------- Molarity -------------------
elif calculator == "Molarity":
    st.header("🧪 Molarity Calculation")

    weight = st.number_input("Weight (g)", min_value=0.0)
    mw = st.number_input("Molecular Weight (g/mol)", min_value=0.1)
    volume = st.number_input("Volume (L)", min_value=0.001)

    if st.button("Calculate Molarity"):
        molarity = calculate_molarity(weight, mw, volume)
        st.success(f"Molarity = {molarity:.4f} M")

# ------------------- Impurity % -------------------
elif calculator == "Impurity Percentage (HPLC)":
    st.header("📊 Impurity Percentage (HPLC)")

    impurity_area = st.number_input("Impurity Area", min_value=0.0)
    total_area = st.number_input("Total Area", min_value=1.0)

    if st.button("Calculate Impurity %"):
        impurity = impurity_percentage(impurity_area, total_area)
        st.success(f"Impurity = {impurity:.3f} %")

# ------------------- PDE Check -------------------
elif calculator == "Residual Solvent PDE Check":
    st.header("🧯 Residual Solvent PDE Compliance")

    ppm = st.number_input("Residual Solvent (ppm)", min_value=0.0)
    daily_dose = st.number_input("Daily Dose (g/day)", min_value=0.0)
    pde_limit = st.number_input("PDE Limit (mg/day)", min_value=0.0)

    if st.button("Check PDE Compliance"):
        compliant, intake = pde_compliance(ppm, daily_dose, pde_limit)
        st.info(f"Daily Intake = {intake:.3f} mg/day")
        if compliant:
            st.success("✅ PDE COMPLIANT")
        else:
            st.error("❌ PDE NOT COMPLIANT")

# ------------------- Solvent Recovery -------------------
elif calculator == "Solvent Recovery":
    st.header("♻️ Solvent Recovery Calculation")

    recovered = st.number_input("Recovered Solvent (kg)", min_value=0.0)
    used = st.number_input("Used Solvent (kg)", min_value=0.1)

    if st.button("Calculate Recovery"):
        recovery = solvent_recovery(recovered, used)
        st.success(f"Solvent Recovery = {recovery:.2f} %")

st.markdown("---")
st.caption("Built for API R&D | QA | Interview Preparation")
