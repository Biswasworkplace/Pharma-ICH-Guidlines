from calculations.yield_calc import calculate_yield
from calculations.molarity import calculate_molarity
from calculations.impurity import impurity_percentage
from calculations.ppm_pde import pde_compliance
from calculations.solvent_recovery import solvent_recovery

print("Reaction Yield:", calculate_yield(85, 100), "%")
print("Molarity:", calculate_molarity(10, 98, 0.5), "M")
print("Impurity %:", impurity_percentage(500, 100000), "%")

compliant, intake = pde_compliance(ppm=300, daily_dose_g=2, pde_limit_mg=50)
print("PDE compliant:", compliant, "| Intake (mg/day):", intake)

print("Solvent Recovery:", solvent_recovery(80, 100), "%")
