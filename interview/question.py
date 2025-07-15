class QuestionGenerator:

    @staticmethod
    def generate_initial(role):
        return f"Tell me about yourself and why you're interested in a {role} role"
    
    @staticmethod
    def generate_follow_up(response):
        # For now, use a static follow-up
        return "Can you give a more specific example from your experience?"