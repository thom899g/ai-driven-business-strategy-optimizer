from reinforcement_learning import StrategyLearner

class RecommendationEngine:
    def __init__(self):
        self.learner = StrategyLearner()
    
    def generate_recommendations(self, current_strategies):
        # Train the learner with current strategies
        self.learner.train(current_strategies)
        
        # Generate new recommendations using learned policy
        new_strategy = self.learner.predict()
        return [new_strategy]