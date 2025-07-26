from util import User,Question,Answer,Comment
from datetime import date
class StackOverFlow:
    
    __instance__ = {}
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance__:
            StackOverFlow()
        return cls.__instance__
    
    def __init__(self):
        if StackOverFlow.__instance__ is not None:
            raise Exception("Singleton class")
        else:
            StackOverFlow.__instance__ = self
            self.users = []
            self.questions:list[Question] = []
            self.answers:list[Answer] = []
            
            
    def createUser(self,userName:str,email:str):
        user = User(userName,email)
        self.users.append(user)
        return user
    
    def createQuestion(self,title,content,author):
        question = Question(title,content,author)
        self.questions.append(question)
        return question
    
    def answerQuestion(self, question: Question, answer: str, user: User):
        answer = Answer(answer, user, question)
        for quest in self.questions:
            if quest == question:
                quest.answerQuestion(answer)
                self.answers.append(answer)
                return answer
    
    
    def commentOnQuestion(self, question: Question, comment: str, user: User):
        comment = Comment(comment, user,str(date.today()))
        
        for quest in self.questions:
            if quest == question:
                quest.addComments(comment)
                
    def commentOnAnswer(self,answer:Answer,comment:str,user:User):
        comment = Comment(comment,user,str(date.today()))
        
        for ans in self.answers:
            if ans == answer:
                ans.addComment(comment)
                
                
    def voteOnQuestion(self, question: Question, user: User, vote: bool):
        for quest in self.questions:
            if quest == question:
                if vote:
                    quest.upVoteQuestion(user)
                else:
                    quest.downVoteQuestion(user)
                    
    def voteOnAnswer(self, answer: Answer, user: User, vote: bool):
        for ans in self.answers:
            if ans == answer:
                if vote:
                    ans.upVoteAnswer(user)
                else:
                    ans.downVoteAnswer(user)
                    
                    
                    
    def addTagToQuestion(self, question: Question, tag: str):
        for quest in self.questions:
            if quest == question:
                quest.addTag(tag)
                
                

            
            
    
    
    