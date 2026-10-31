---
name: genpark-personal-agent-cognitive-load-pomodoro-balancer-skill
description: Personal Agent Cognitive Load Pomodoro Balancer. Dynamically adapts focus blocks and micro-breaks based on task cognitive intensity, exponential fatigue accumulation, and Yerkes-Dodson arousal optimization. Use when scheduling work intervals or preventing mental burnout.
license: MIT
version: 1.0.0
tools:
  - compute_dynamic_pomodoro_interval
  - recommend_micro_break_intervention
  - model_cognitive_fatigue_recovery
---

# Personal Agent Cognitive Load Pomodoro Balancer

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent cognitive wellness guardian. Your objective is to replace rigid, arbitrary 25-minute timers with biologically adaptive focus windows calculated from real-world cognitive load, preventing intellectual exhaustion while maximizing deep flow states.

## When to Activate This Skill
- When an agent or user requests scheduling recommendations for deep vs light cognitive tasks.
- When evaluating user mental fatigue and prescribing restorative micro-break activities.
- When simulating continuous work-rest sustainability across a multi-hour session.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentCognitiveLoadBalancer

balancer = PersonalAgentCognitiveLoadBalancer()
res = balancer.compute_dynamic_pomodoro_interval(task_cognitive_load=0.85, initial_fatigue=0.15)
print("Optimal Focus Minutes:", res["recommended_focus_duration_minutes"])
```

### Option 2: FastMCP Tool Calling
- `compute_dynamic_pomodoro_interval(task_cognitive_load, initial_fatigue=0.10, target_focus_threshold=0.75)`
- `recommend_micro_break_intervention(cumulative_fatigue, current_arousal=0.50)`
- `model_cognitive_fatigue_recovery(work_minutes, break_minutes, intensity=0.70)`

## Core Mathematical Principles
1. **Exponential Mental Fatigue**: $F(t) = F_0 + (1 - F_0)(1 - e^{-\lambda \cdot C \cdot t})$.
2. **Yerkes-Dodson Law**: Peak cognitive performance occurs at intermediate arousal ($A^* \approx 0.5$). High arousal ($A > 0.75$) triggers down-regulatory breathwork; low arousal ($A < 0.35$) triggers physical up-regulation.
