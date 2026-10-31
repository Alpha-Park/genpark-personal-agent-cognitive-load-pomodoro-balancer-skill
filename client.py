# -*- coding: utf-8 -*-
"""
Personal Agent Cognitive Load Pomodoro Balancer Client
Zero-dependency exponential mental fatigue accumulation modeler,
Yerkes-Dodson arousal curve optimizer, and dynamic micro-break recovery scheduler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentCognitiveLoadBalancer:
    """
    Dynamically balances cognitive workloads and rest intervals based on task intensity,
    arousal state, and cumulative mental fatigue curves.
    """

    def compute_dynamic_pomodoro_interval(
        self,
        task_cognitive_load: float,
        initial_fatigue: float = 0.10,
        target_focus_threshold: float = 0.75
    ) -> Dict[str, Any]:
        """
        Calculates optimal continuous focus interval in minutes before fatigue exceeds threshold.
        Fatigue: F(t) = F0 + (1 - F0) * (1 - exp(-lambda * C * t))
        """
        c = max(0.1, min(1.0, task_cognitive_load))
        f0 = max(0.0, min(0.9, initial_fatigue))
        target_f = max(f0 + 0.05, min(0.85, target_focus_threshold))
        lambda_rate = 0.025

        # Solve for t: 1 - (target_f - f0)/(1 - f0) = exp(-lambda * c * t)
        ratio = max(0.01, 1.0 - (target_f - f0) / (1.0 - f0))
        t_optimal = -math.log(ratio) / (lambda_rate * c)
        t_optimal_minutes = round(max(15.0, min(60.0, t_optimal)), 1)

        # Yerkes-Dodson optimal cognitive flow rating
        flow_efficiency = round(1.0 - abs(c - 0.70) * 0.8, 3)

        return {
            "task_cognitive_load": c,
            "initial_fatigue_level": f0,
            "target_fatigue_threshold": target_f,
            "recommended_focus_duration_minutes": t_optimal_minutes,
            "flow_efficiency_score": flow_efficiency,
            "task_intensity_classification": "DEEP_ANALYTIC" if c >= 0.75 else ("MODERATE_OPERATIONAL" if c >= 0.40 else "LIGHT_ADMIN"),
            "post_session_predicted_fatigue": target_f
        }

    def recommend_micro_break_intervention(
        self,
        cumulative_fatigue: float,
        current_arousal: float = 0.50
    ) -> Dict[str, Any]:
        """
        Recommends micro-break duration and specific recovery modality using Yerkes-Dodson arousal model.
        Break Duration = max(3, min(15, -ln(1 - 0.7 * Fatigue) / mu_recovery))
        """
        f = max(0.05, min(0.95, cumulative_fatigue))
        a = max(0.05, min(0.95, current_arousal))

        # Recovery rate constant
        mu_recovery = 0.18
        break_duration = max(3.0, min(15.0, -math.log(max(0.05, 1.0 - 0.75 * f)) / mu_recovery))
        break_duration_minutes = round(break_duration, 1)

        # Yerkes-Dodson performance: P = 4 * A * (1 - A)
        performance_index = round(4.0 * a * (1.0 - a), 3)

        if a > 0.75:
            modality = "DOWN_REGULATION_BREATHWORK (Physiological sigh: 4s inhale, 4s hold, 8s exhale)"
            state = "OVER_AROUSED_HYPERACTIVE"
        elif a < 0.35:
            modality = "UP_REGULATION_PHYSICAL (Brisk walking, cold water rinse, sunlight exposure)"
            state = "UNDER_AROUSED_DROWSY"
        else:
            modality = "PASSIVE_REST_VISION (20-20-20 visual horizon gaze, silent hydration)"
            state = "OPTIMAL_FLOW_BAND"

        return {
            "cumulative_fatigue": f,
            "current_arousal": a,
            "performance_index": performance_index,
            "recommended_break_duration_minutes": break_duration_minutes,
            "arousal_state": state,
            "prescribed_intervention_modality": modality,
            "expected_fatigue_reduction_pct": round(min(50.0, f * 45.0), 1)
        }

    def model_cognitive_fatigue_recovery(
        self,
        work_minutes: int,
        break_minutes: int,
        intensity: float = 0.70
    ) -> Dict[str, Any]:
        """
        Simulates two-phase work-rest cycle and returns net recovery efficiency.
        """
        c = max(0.1, min(1.0, intensity))
        fatigue_accumulated = round(1.0 - math.exp(-0.025 * c * work_minutes), 3)
        fatigue_cleared = round(fatigue_accumulated * (1.0 - math.exp(-0.18 * break_minutes)), 3)
        residual_fatigue = round(max(0.05, fatigue_accumulated - fatigue_cleared), 3)
        recovery_efficiency = round((fatigue_cleared / max(1e-9, fatigue_accumulated)) * 100.0, 1)

        return {
            "work_duration_minutes": work_minutes,
            "break_duration_minutes": break_minutes,
            "cognitive_intensity": c,
            "peak_session_fatigue": fatigue_accumulated,
            "fatigue_cleared_during_break": fatigue_cleared,
            "residual_baseline_fatigue": residual_fatigue,
            "recovery_efficiency_pct": recovery_efficiency,
            "sustainability_status": "HIGHLY_SUSTAINABLE" if residual_fatigue <= 0.25 else "ACCUMULATING_DEBT"
        }
