// Pharmacogenomics_Model.psc

// Define the compartments
compartment S // Susceptible population
compartment I // Infected population
compartment R // Recovered population

// Define the parameters
param k1 = 0.5 // Rate of infection
param k2 = 0.1 // Rate of recovery

// Define the initial conditions
init S = 999
init I = 1
init R = 0

// Define the ODEs
dS/dt = -k1*S*I
dI/dt = k1*S*I - k2*I
dR/dt = k2*I
