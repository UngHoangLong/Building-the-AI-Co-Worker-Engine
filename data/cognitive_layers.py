"""
CognitiveLayers: Quản lý 3 layer nhận thức cho mỗi persona
- Layer 1: Core Ontology
- Layer 2: Semantic Reflex
- Layer 3: Dynamic State (khởi tạo mặc định, cập nhật qua state_manager)
"""
import json
import os

class CognitiveLayers:
    def __init__(self, persona_json_path):
        with open(persona_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Layer 1: Core Ontology
        self.role_persona = data.get('role_persona', '')
        self.worldview_axioms = data.get('worldview_axioms', [])
        self.communication_style = data.get('communication_style', '')
        self.power_dynamic = data.get('power_dynamic', '')
        self.absolute_boundaries = data.get('absolute_boundaries', [])
        self.simulation_objectives = data.get('simulation_objectives', [])
        # Layer 2: Semantic Reflex
        self.red_flags = data.get('red_flags', [])
        self.green_flags = data.get('green_flags', [])
        # Layer 3: Dynamic State (khởi tạo mặc định)
        self.dynamic_state = {
            "trust_score": 50,
            "delta_score": 0,
            "accumulate_score_list": [],
            "patience_level": 100,
            "tension_score": 0,
            "list_task_done": [False for _ in self.simulation_objectives],
            "current_internal_monologue": "",
            "history_internal_monologue": []
        }
    def get_layer1(self):
        return {
            "role_persona": self.role_persona,
            "worldview_axioms": self.worldview_axioms,
            "communication_style": self.communication_style,
            "power_dynamic": self.power_dynamic,
            "absolute_boundaries": self.absolute_boundaries,
            "simulation_objectives": self.simulation_objectives
        }
    def get_layer2(self):
        return {
            "red_flags": self.red_flags,
            "green_flags": self.green_flags
        }
    def get_layer3(self):
        return self.dynamic_state
    def update_dynamic_state(self, state_dict):
        self.dynamic_state.update(state_dict)
