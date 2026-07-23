from app.agents.security_agent import SecurityAgent


agent = SecurityAgent()


diff = """

def login(username,password):

    query = (
        "SELECT * FROM users WHERE username='"
        + username
        + "'"
    )

    return query

"""


response = agent.review(diff)


print(response)