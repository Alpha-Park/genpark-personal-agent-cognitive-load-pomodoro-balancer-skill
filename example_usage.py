# -*- coding: utf-8 -*-
import json
from client import PersonalAgentCognitiveLoadBalancer

balancer = PersonalAgentCognitiveLoadBalancer()

print("=" * 64)
print("DEMO: Personal Cognitive Load & Dynamic Pomodoro Balancer")
print("=" * 64)

# 1. Compute dynamic focus session
focus = balancer.compute_dynamic_pomodoro_interval(task_cognitive_load=0.88, initial_fatigue=0.20)
print(f"\n1. Deep Work Task (Load: {focus['task_cognitive_load']}):")
print(f"   Recommended Focus Block: {focus['recommended_focus_duration_minutes']} min")
print(f"   Task Classification: {focus['task_intensity_classification']} (Flow Score: {focus['flow_efficiency_score']})")

# 2. Prescribe tailored micro-break
rest = balancer.recommend_micro_break_intervention(cumulative_fatigue=0.72, current_arousal=0.82)
print(f"\n2. Post-Session Rest Intervention (Fatigue: {rest['cumulative_fatigue']} | Arousal: {rest['current_arousal']}):")
print(f"   Break Duration: {rest['recommended_break_duration_minutes']} min")
print(f"   Arousal Diagnosis: {rest['arousal_state']}")
print(f"   Prescribed Modality: {rest['prescribed_intervention_modality']}")

# 3. Model fatigue recovery cycle
recovery = balancer.model_cognitive_fatigue_recovery(work_minutes=45, break_minutes=8, intensity=0.85)
print(f"\n3. Work-Rest Cycle Simulation (45m work + 8m rest):")
print(f"   Peak Fatigue: {recovery['peak_session_fatigue']} -> Residual Baseline: {recovery['residual_baseline_fatigue']}")
print(f"   Recovery Efficiency: {recovery['recovery_efficiency_pct']}% ({recovery['sustainability_status']})")
