# 🟣 Day 5: Advanced Conditionals

Applying complex logical chains to real-world scenarios.

## 🛠️ Featured Project: Travel Weather Planner

The `main.py` script implements a decision tree to determine if a commute is feasible based on distance, weather conditions, and available transportation.

### Logic Flow:
1.  **Check Distance**: If 0, return `False`.
2.  **Short Distance (<= 1mi)**: Feasible if not raining.
3.  **Medium Distance (1-6mi)**: Feasible if has a bike AND not raining.
4.  **Long Distance (> 6mi)**: Feasible if has a car OR ride-share app.

---

## 🧠 Project Knowledge Checks

<details>
<summary><b>Q1: How do you handle a 'Falsy' check for distance?</b></summary>

Using `if not distance_mi:`.
![Distance Logic](Screenshot%202026-06-03%20at%206.46.22 PM.png)
</details>

<details>
<summary><b>Q2: What logic is used for the bike commute (1-6 miles)?</b></summary>

`if has_bike and not is_raining:`.
![Bike Logic](Screenshot%202026-06-03%20at%206.46.42 PM.png)
</details>

<details>
<summary><b>Q3: What logic is used for long-distance commutes (> 6 miles)?</b></summary>

`if has_car or has_ride_share_app:`.
![Car Logic](Screenshot%202026-06-03%20at%206.57.23 PM.png)
</details>

<details>
<summary><b>Q4: What is the final output of the Travel Weather Planner?</b></summary>

A boolean `True` or `False` printed to the console.
![Output Proof](Screenshot%202026-06-03%20at%206.57.29 PM.png)
</details>
