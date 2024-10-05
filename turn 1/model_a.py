import pysces
from pysces import model
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Create a PySCeS model
m = model('Pharmacogenomic Model')

# Step 2: Define the model components and parameters

# Example model: A simple two-compartment model with drug interaction
m.param('V1', 1.0)  # Compartment 1 volume
m.param('V2', 2.0)  # Compartment 2 volume
m.param('k1', 0.1)  # Rate constant for reaction 1
m.param('k2', 0.2)  # Rate constant for reaction 2
m.param('Kd', 10.0)  # Dissociation constant for drug
m.param('D', 0.0)  # Initial drug concentration

m.var('S1', 10)  # Initial substrate concentration in compartment 1
m.var('S2', 0)  # Initial substrate concentration in compartment 2
m.var('P', 0)  # Initial product concentration

# Reactions
m.reaction('S1 -> S2', k1*S1)
m.reaction('S2 -> P', k2*S2)
m.reaction('D -> AD', D/(D+Kd))  # Drug binding
m.reaction('AD -> D + S2', k2*AD)  # Drug-mediated reaction

# Step 3: Define time points for simulation
t_start = 0
t_end = 20
t_points = 100
ts = np.linspace(t_start, t_end, t_points)

# Step 4: Simulate the model with time-series data
result = m.simulate(ts, ['S1', 'S2', 'P', 'D'])

#Step 5: Analyze the time-series data

#Let's analyze how the drug concentration ('D') affects the substrate concentrations ('S1' and 'S2') over time

plt.figure(figsize=(10, 6))
plt.plot(ts, result['S1'], label='Substrate 1')
plt.plot(ts, result['S2'], label='Substrate 2')
plt.plot(ts, result['D'], label='Drug')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.title('Effect of Drug on Substrate Concentrations')
plt.show()


#Step 6: Perform further analysis and determine drug efficacy

#Calculate the maximum substrate concentrations
max_S1 = np.max(result['S1'])
max_S2 = np.max(result['S2'])

print(f"Maximum Substrate 1 concentration: {max_S1}")
print(f"Maximum Substrate 2 concentration: {max_S2}")

#Analyze the area under the curve (AUC) to quantify drug efficacy
from scipy import integrate

auc_S1 = integrate.simps(result['S1'], ts)
auc_S2 = integrate.simps(result['S2'], ts)

print(f"AUC for Substrate 1: {auc_S1}")
print(f"AUC for Substrate 2: {auc_S2}")

# Interpretation:
# Higher AUC values indicate better drug efficacy in terms of substrate conversion.

# Step 7: (Optional) Parameter Sensitivity Analysis

# Perform sensitivity analysis to identify key parameters
from pysces.analysis import sensitivity

sa = sensitivity(m, params=['k1', 'k2', 'Kd'], obs=['S2'])
sa.plot()
plt.show()

print("Sensitivity analysis completed.")
