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
    probabil