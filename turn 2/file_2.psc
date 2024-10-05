// Pharmacogenomics Model with Drug Effect
model Pharmacogenomics_Model

// Compartments
S -> I k1*S*I // Susceptible to Infected
I -> R k2*I // Infected to Recovered

// Parameters
param k1 = 0.5 // Infection rate constant
param k2 = 0.1 // Recovery rate constant
param drug_effect = 0.5 // Drug effect constant (will be modified later)

// Initial Conditions
S = 999
I = 1
R = 0

// Events: Drug administration at t=5
event drug_admin(time >= 5):
    k1 = k1 * drug_effect
end
