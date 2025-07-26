

from datetime import date
from typing import Dict,List
class User:
    
    def __init__(self,user_id,username,email):
        self.id = user_id
        self.username = username
        self.email = email
        self.reputation = 0
        self.questions = []
        self.answers = []
        self.comments = []
        
        
    def ask_question(self, title,content,tags):
        question = Question(self, title, content, tags)  # ✅ correct
        self.questions.append(question)
        self.update_reputation(5)  # Reward for asking a question)
        return question
    
    def answer_question(self, question, content):
        answer = Answer(self, question, content)  # ✅ correct
        self.answers.append(answer)
        question.add_answer(answer)
        self.update_reputation(10)  # Reward for answering a question
        return answer
    
    def comment_on(self, commentable, content):
        comment = Comment(self,content)
        commentable.add_comment(comment)
        self.comments.append(comment)
        self.update_reputation(2)  # Reward for commenting
        return comment
    
    def update_reputation(self, points):
        self.reputation += points
        self.reputation = max(0,self.reputation)  # Ensure reputation doesn't go below 0
        


from abc import ABC, abstractmethod

class Commentable(ABC):
    @abstractmethod
    def add_comment(self, comment):
        pass
    
    @abstractmethod
    def get_comments(self):
        pass
    
class Votable(ABC):
    @abstractmethod
    def vote(self, user, value):
        pass

    @abstractmethod
    def get_vote_count(self):
        pass
    
class Vote:
    def __init__(self, user, value):
        self.user = user
        self.value = value
        
        
class Question(Votable,Commentable):
    
    def __init__(self,author,title,content,tag_names):
        self.id = id(self)
        self.author = author
        self.title = title
        self.content = content
        self.tags = []
        self.votes = []
        self.answers = []
        self.tags = [Tag(name) for name in tag_names]
        self.comments = []
        
    def add_answer(self,answer):
        if answer not in self.answers:
            self.answers.append(answer)
            
    def vote(self, user, value):
        if value not in [-1, 1]:
            raise ValueError("Vote value must be either 1 or -1")
        self.votes = [v for v in self.votes if v.user != user]
        self.votes.append(Vote(user, value))
        print(self.author)
        self.author.update_reputation(value * 5)  # +5 for upvote, -5 for downvote

    def get_vote_count(self):
        return sum(v.value for v in self.votes)

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_comments(self) -> List['Comment']:
        return self.comments.copy()
        
    
    
class Answer(Votable, Commentable):
    def __init__(self, author, question, content):
        self.id = id(self)
        self.author = author
        self.question = question
        self.content = content
        self.creation_date = str(date.today())
        self.votes = []
        self.comments = []
        self.is_accepted = False

    def vote(self, user, value):
        if value not in [-1, 1]:
            raise ValueError("Vote value must be either 1 or -1")
        self.votes = [v for v in self.votes if v.user != user]
        self.votes.append(Vote(user, value))
        print(self.author)
        self.author.update_reputation(value * 10)  # +10 for upvote, -10 for downvote

    def get_vote_count(self) -> int:
        return sum(v.value for v in self.votes)

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_comments(self):
        return self.comments.copy()

    def accept(self):
        if self.is_accepted:
            raise ValueError("This answer is already accepted")
        self.is_accepted = True
        self.author.update_reputation(15)  # +15 reputation for accepted answer
        
        
class Comment:
    def __init__(self, author, content):
        self.id = id(self)
        self.author = author
        self.content = content
        self.creation_date = str(date.today())
        
        
class Tag:
    def __init__(self, name: str):
        self.id = id(self)
        self.name = name
        
        
class StackOverflow:
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.questions: Dict[int, Question] = {}
        self.answers: Dict[int, Answer] = {}
        self.tags: Dict[str, Tag] = {}

    def create_user(self, username, email):
        user_id = len(self.users) + 1
        user = User(user_id, username, email)
        self.users[user_id] = user
        return user

    def ask_question(self, user, title, content, tags):
        question = user.ask_question(title, content, tags)
        self.questions[question.id] = question
        for tag in question.tags:
            self.tags.setdefault(tag.name, tag)
        return question

    def answer_question(self, user, question, content):
        answer = user.answer_question(question, content)
        self.answers[answer.id] = answer
        return answer

    def add_comment(self, user, commentable, content):
        return user.comment_on(commentable, content)

    def vote_question(self, user, question, value):
        question.vote(user, value)

    def vote_answer(self, user, answer, value):
        answer.vote(user, value)

    def accept_answer(self, answer):
        answer.accept()

    def search_questions(self, query):
        return [q for q in self.questions.values() if 
                query.lower() in q.title.lower() or
                query.lower() in q.content.lower() or
                any(query.lower() == tag.name.lower() for tag in q.tags)]

    def get_questions_by_user(self, user):
        return user.questions

    def get_user(self, user_id):
        return self.users.get(user_id)

    def get_question(self, question_id):
        return self.questions.get(question_id)

    def get_answer(self, answer_id):
        return self.answers.get(answer_id)

    def get_tag(self, name: str):
        return self.tags.get(name)