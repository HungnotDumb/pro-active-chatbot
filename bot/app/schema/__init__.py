from graphene import Float, ObjectType, String, Schema, InputObjectType, Mutation, Field, Int
from chatbot import predict_intent, chatbot_model
import os, json, random


with open (os.path.join(
    os.getcwd(), 'chatbot/files/static/Intent.json'
)) as f:
    data = json.load(f)
    
intents = data["intents"]

class UserInput(InputObjectType):
    text = String(required=True)

class MetaType(ObjectType):
    programmer = String(required=True)
    project = String(required=True)
    main = String(required=True)

class ClassificationType(ObjectType):
    label = Int(required=True)
    intent = String(required=True)
    probability = Float(required=True)
    
class BotAnswer(ObjectType):
    response = String(required=True)
    
class UserQuestion(ObjectType):
    text =  String(required=True)
    
class BotResponse(ObjectType):
    classification = Field(ClassificationType, required=True)
    meta = Field(MetaType, required=True)
    answer = Field(BotAnswer, required=True)
    question = Field(UserQuestion, required=True)
    

class RespondBot(Mutation):
    class Arguments:
      