"""
Project Chimera: Real-time AI Safety Monitoring System
=====================================================

Revolutionary AI safety monitoring for Meta Superintelligence Labs.
Created by Michael David Jaramillo.

Key Components:
- Real-time anomaly detection with LSTM + Attention
- Causal inference for root cause analysis  
- Explainable AI integration (SHAP + LIME)
- Kafka-based streaming for Meta-scale processing
"""

__version__ = "1.0.0"
__author__ = "Michael David Jaramillo"
__email__ = "jmichaeloficial@gmail.com"
__description__ = "Real-time AI Safety Monitoring for Meta Superintelligence Labs"

from .core.detector import StreamingAnomalyDetector
from .core.monitor import ChimeraMonitor
from .causal.inference_engine import CausalInferenceEngine
from .explainability.xai_analyzer import XAIAnalyzer

__all__ = [
    "StreamingAnomalyDetector",
    "ChimeraMonitor", 
    "CausalInferenceEngine",
    "XAIAnalyzer"
]