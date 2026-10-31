# -*- coding: utf-8 -*-
"""
Personal Agent Cognitive Load Pomodoro Balancer FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentCognitiveLoadBalancer

mcp = FastMCP("genpark-personal-agent-cognitive-load-pomodoro-balancer-skill")
balancer = PersonalAgentCognitiveLoadBalancer()

@mcp.tool()
def compute_dynamic_pomodoro_interval(
    task_cognitive_load: float,
    initial_fatigue: float = 0.10,
    target_focus_threshold: float = 0.75
) -> str:
    """
    Calculates personalized focus duration in minutes based on task cognitive intensity.
    """
    res = balancer.compute_dynamic_pomodoro_interval(task_cognitive_load, initial_fatigue, target_focus_threshold)
    return json.dumps(res, indent=2)

@mcp.tool()
def recommend_micro_break_intervention(
    cumulative_fatigue: float,
    current_arousal: float = 0.50
) -> str:
    """
    Recommends micro-break duration and restorative activity using Yerkes-Dodson arousal law.
    """
    res = balancer.recommend_micro_break_intervention(cumulative_fatigue, current_arousal)
    return json.dumps(res, indent=2)

@mcp.tool()
def model_cognitive_fatigue_recovery(
    work_minutes: int,
    break_minutes: int,
    intensity: float = 0.70
) -> str:
    """
    Simulates a work-rest session and evaluates net cognitive recovery sustainability.
    """
    res = balancer.model_cognitive_fatigue_recovery(work_minutes, break_minutes, intensity)
    return json.dumps(res, indent=2)

def main():
    print("Testing Cognitive Load Pomodoro Balancer FastMCP Server:")
    print(compute_dynamic_pomodoro_interval(0.85, 0.15))

if __name__ == "__main__":
    main()
