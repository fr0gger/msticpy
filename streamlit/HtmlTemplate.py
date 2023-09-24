css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex; align-items: center;
}
.chat-message.user {
    background-color: #2b313e;
}
.chat-message.bot {
    background-color: #475063;
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 100%;
  padding: 0 1.5rem;
  color: #fff;
  word-wrap: break-word;      /* Wrap long words onto the next line */
  max-width: 90%;            /* Adjust as per your requirements */
  overflow: hidden;          /* Hide the excess content */
}
</style>

'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://raw.githubusercontent.com/fr0gger/msticpy/271d15ce4f052dd862316daabbc6fa9bb6b41de4/avatar.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/vcLhRQf/secto.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''