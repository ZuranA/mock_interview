from interview.question import QuestionGenerator

class InterviewSession:

    def __init__(self, user_id, role, questions, responses):
        self.user_id = user_id
        self.role = role 
        self.questions = [QuestionGenerator.generate_initial(role)]
        self.responses = []


    def next_question(self):
        if not self.responses:
            return self.questions[0]
        
        follow_up = QuestionGenerator.generate_follow_up(self.responses[-1])
        self.questions.append(follow_up)
        return follow_up
    
    def add_response(self, response):
        self.response.append(response)