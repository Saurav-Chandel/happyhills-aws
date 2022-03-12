

# from channels.consumer import SyncConsumer, AsyncConsumer
# from channels.exceptions import StopConsumer

# class SynConsumer(SyncConsumer):
    

#     def websocket_connect(self, event):
#         print("websocket connect........",event)  

#         self.send({
#             "type": "websocket.accept",
#         })

#     def websocket_receive(self, event):
#         print("websocket receive from client",event['text'])

#         self.send({
#             "type": "websocket.send",
#             "text":"message sent to cient",
#         })

#     def websocket_disconnect(self, event):
#         print("websocket doisconnect....",event)
#         raise StopConsumer()


# class AsynConsumer(AsyncConsumer):
        
#     async def websocket_connect(self, event):    #handler methods
#         print("websocket connect......",event)

#         await self.send({
#             "type": "websocket.accept",
#         })

#     async def websocket_receive(self, event):
#         print("websocket receive from client",event['text'])


#         await self.send({
#             "type": "websocket.send",
#             "text":"message sent to cient",

#         })

#     async def websocket_disconnect(self, event):
#         print("websocket doisconnect.....",event)
#         raise StopConsumer()

