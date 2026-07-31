from backend.app.llm.session import ChatSession


def test_create_session():
    """
    测试创建聊天会话。
    """
    session = ChatSession()

    assert session.get_messages() == []


def test_add_user_message():
    """
    测试添加用户消息。
    """
    session = ChatSession()

    session.add_user_message("你好")

    messages = session.get_messages()

    assert len(messages) == 1
    assert messages[0].role == "user"
    assert messages[0].content == "你好"


def test_add_assistant_message():
    """
    测试添加助手消息。
    """
    session = ChatSession()

    session.add_assistant_message("你好，我是助手。")

    messages = session.get_messages()

    assert len(messages) == 1
    assert messages[0].role == "assistant"
    assert messages[0].content == "你好，我是助手。"


def test_add_system_message():
    """
    测试添加系统消息。
    """
    session = ChatSession()

    session.add_system_message("你是一名 AI 助手。")

    messages = session.get_messages()

    assert len(messages) == 1
    assert messages[0].role == "system"
    assert messages[0].content == "你是一名 AI 助手。"


def test_clear_messages():
    """
    测试清空聊天记录。
    """
    session = ChatSession()

    session.add_user_message("你好")
    session.add_assistant_message("你好！")

    assert len(session.get_messages()) == 2

    session.clear()

    assert session.get_messages() == []
