# Simple SIR model

# Species
S = 1  # Susceptible population
I = 2  # Infected population
R = 3  # Recovered population

# Reactions
R1: S + I -> 2*I  # Infection, rate constant k1
R2: I -> R       # Recovery, rate constant k2

# Initializations
InitExt
  S = 999        # Initial susceptible population
  I = 1          # Initial infected population
  R = 0          # Initial recovered population

# Parameters
InitPar
  k1 = 0.5       # Infection rate constant
  k2 = 0.1       # Recovery rate constant
