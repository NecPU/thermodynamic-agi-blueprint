import random
import math
import matplotlib.pyplot as plt

# Spatial grid environment (0 - free path, 1 - boundary/wall)
BASE_MAZE_STR = """00100
00101
10000
01110
00010"""

# Convert string representation into a 2D matrix
BASE_MAZE = [list(map(int, list(row))) for row in BASE_MAZE_STR.strip().split("\n")]

START = (0, 0)
GOAL = (4, 4)

DIRECTIONS = {
    "UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)
}

def get_sensory_imprint(pos, maze):
    """ Generates a multi-modal structural snapshot based on 3 distinct sensor types """
    r, c = pos
    
    # 1. Tactile Sensor: counts immediate boundary constraints (walls/edges)
    touch_sensors = 0
    for dr, dc in DIRECTIONS.values():
        nr, nc = r + dr, c + dc
        if not (0 <= nr < 5 and 0 <= nc < 5) or maze[nr][nc] == 1:
            touch_sensors += 1
            
    # 2. Acoustic Sensor: target vector resonance mapping (closer to goal = louder)
    goal_r, goal_c = GOAL
    distance_to_goal = math.sqrt((r - goal_r)**2 + (c - goal_c)**2)
    audio_sensor = round(10 / (distance_to_goal + 1), 1)
    
    # 3. Optical Sensor: localized invariant state illumination
    light_sensor = (r + c) % 3
    
    # Returns an indivisible multi-modal invariant configuration tensor
    return (touch_sensors, audio_sensor, light_sensor)

def run_advanced_experiment(use_thermodynamics=False):
    # Deep copy of the environment matrix for mutation injection
    current_maze = [row[:] for row in BASE_MAZE]
    current_pos = START
    energy = 120
    steps_taken = 0
    
    # TOPOLOGICAL MEMORY: Accumulates verified multi-modal sensory traces
    knowledge_base = set()
    energy_history = [energy]
    
    print(f"\n--- LAUNCHING AGENT (Thermodynamic Core Active: {use_thermodynamics}) ---")
    
    for turn in range(1, 100):
        if current_pos == GOAL:
            print(f"🎉 Success! Goal reached. Final energy: {energy} units. Physical steps: {steps_taken}")
            break
        if energy <= 0:
            print("💀 Energy exhausted! System execution halted.")
            break
            
        # Environmental Mutation Injection: Every 15 cycles, a boundary cell status toggles
        if turn % 15 == 0:
            mr, mc = random.randint(1, 3), random.randint(1, 3)
            current_maze[mr][mc] = 1 if current_maze[mr][mc] == 0 else 0
            
        # Exploratory actuation drive
        chosen_dir = random.choice(list(DIRECTIONS.keys()))
        dr, dc = DIRECTIONS[chosen_dir]
        
        curr_r, curr_c = current_pos
        next_r, next_c = curr_r + dr, curr_c + dc
        next_pos = (next_r, next_c)
        
        is_outside = not (0 <= next_r < 5 and 0 <= next_c < 5)
        is_wall = False if is_outside else (current_maze[next_r][next_c] == 1)
        
        if use_thermodynamics:
            # --- THERMODYNAMIC OPTIMIZATION ARCHITECTURE ---
            energy -= 1 # Base cognitive overhead per internal simulation cycle
            
            if is_outside or is_wall:
                print(f"Cycle {turn}: VIRTUAL SIMULATION detected spatial obstacle {chosen_dir}. VETO triggered. [Cost: 1 en.]")
                energy_history.append(energy)
                continue
                
            # Simulate sensorimotor causal feedback internally before execution
            predicted_imprint = get_sensory_imprint(next_pos, current_maze)
            
            # Evaluate informational value using the memory matrix
            if predicted_imprint in knowledge_base:
                # VETO: Informational value redundant (dI ~ 0). Physical execution suppressed.
                print(f"Cycle {turn}: VIRTUAL SIMULATION detected redundant imprint {chosen_dir}. VETO triggered. [Cost: 1 en.]")
                energy_history.append(energy)
                continue
            else:
                # Stabilization: Imprint added to knowledge base, executing high-power actuator signal
                knowledge_base.add(predicted_imprint)
                energy -= 10 # High-power physical actuator cost
                current_pos = next_pos
                steps_taken += 1
                print(f"Cycle {turn}: PATH APPROVED. System transitioned {chosen_dir} to {current_pos}. [Cost: 11 en.]")
        else:
            # --- AUTOREGRESSIVE BRUTE-FORCE AGENT ---
            energy -= 10 # Instantly commits high-power physical resources blindly
            if is_outside or is_wall:
                print(f"Cycle {turn}: Agent collided blindly with obstacle {chosen_dir}! State unchanged. [Cost: 10 en.]")
            else:
                current_pos = next_pos
                steps_taken += 1
                print(f"Cycle {turn}: Agent successfully shifted {chosen_dir} to {current_pos}. [Cost: 10 en.]")
                
        energy_history.append(energy)
        
    return energy_history, current_pos == GOAL, steps_taken

# Execute paired comparative testing
hist_blind, success_blind, steps_blind = run_advanced_experiment(use_thermodynamics=False)
hist_thermo, success_thermo, steps_thermo = run_advanced_experiment(use_thermodynamics=True)

# EMPIRICAL DATA PLOTTING
plt.figure(figsize=(11, 5))
plt.plot(hist_blind, label='Autoregressive AI (No Veto / No Imprints)', color='crimson', linewidth=2.5)
plt.plot(hist_thermo, label='Thermodynamic AGI (Sensory Invariants + VETO)', color='forestgreen', linewidth=2.5)
plt.axhline(0, color='grey', linestyle='--', alpha=0.7)
plt.title('Thermodynamic Efficiency Profile: Energy Consumption Comparison', fontsize=12)
plt.xlabel('Computational & Actuation Execution Cycles (Time Ticks)')
plt.ylabel('Internal Systemic Energy Potential')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("\n--- EXPERIMENT METRICS ---")
print(f"Autoregressive AI | Goal Reached: {success_blind} | Physical Steps Taken: {steps_blind}")
print(f"Thermodynamic AGI | Goal Reached: {success_thermo} | Physical Steps Taken: {steps_thermo}")
