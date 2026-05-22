class ConversationMemory:

    def __init__(self, limit=5):
        self.limit = limit
        self.history = []

    def add(self, role, content):

        self.history.append({
            "role": role,
            "content": content
        })

        self.history = self.history[-self.limit:]

    def get(self):
        return self.history