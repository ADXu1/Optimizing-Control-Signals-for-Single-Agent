# bezier_curve_optimization/bezier_smoothing_loss.py
import numpy as np
from .throttle_optimization import optimize_throttle, objective as throttle_objective
from .steering_optimization import optimize_steering, objective as steering_objective

def bezier_smoothing_loss(t, actual_trajectory, reference_trajectory, alpha=0.5, beta=0.3, gamma=0.2):
    throttle = optimize_throttle(t)
    steering = optimize_steering(t)
    
    throttle_loss = throttle_objective(throttle, t)
    steering_loss = steering_objective(steering, t)
    tracking_loss = np.mean((actual_trajectory - reference_trajectory)**2)
    
    loss = alpha * throttle_loss + beta * steering_loss + gamma * tracking_loss
    return loss
