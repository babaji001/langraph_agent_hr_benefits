from memory import memory


employee_id = "E1001"
session_id = "session_001"


# --------------------------------------------------
# Test 1: Save first message
# --------------------------------------------------

memory.save_context(
    employee_id,
    session_id,
    {
        "role": "user",
        "content": "How much PTO do I have?"
    }
)


# --------------------------------------------------
# Test 2: Save second message
# --------------------------------------------------

memory.save_context(
    employee_id,
    session_id,
    {
        "role": "assistant",
        "content": "You have 120 hours of PTO."
    }
)


# --------------------------------------------------
# Test 3: Save third message
# --------------------------------------------------

memory.save_context(
    employee_id,
    session_id,
    {
        "role": "user",
        "content": "Can I carry it over to next year?"
    }
)


# --------------------------------------------------
# Test 4: Get conversation history
# --------------------------------------------------

history = memory.get_context(
    employee_id,
    session_id
)

print("\nCONVERSATION HISTORY")
print("=" * 50)

for message in history:
    print(message)


# --------------------------------------------------
# Test 5: Get last message
# --------------------------------------------------

last_message = memory.get_last_message(
    employee_id,
    session_id
)

print("\nLAST MESSAGE")
print("=" * 50)

print(last_message)


# --------------------------------------------------
# Test 6: Test limit
# --------------------------------------------------

limited_history = memory.get_context(
    employee_id,
    session_id,
    limit=2
)

print("\nLAST 2 MESSAGES")
print("=" * 50)

for message in limited_history:
    print(message)


# --------------------------------------------------
# Test 7: Test different session
# --------------------------------------------------

memory.save_context(
    employee_id,
    "session_002",
    {
        "role": "user",
        "content": "What is my medical plan?"
    }
)

print("\nSESSION 002")
print("=" * 50)

print(
    memory.get_context(
        employee_id,
        "session_002"
    )
)


# --------------------------------------------------
# Test 8: Test clear memory
# --------------------------------------------------

memory.clear_memory(
    employee_id,
    session_id
)

print("\nAFTER CLEARING SESSION 001")
print("=" * 50)

print(
    memory.get_context(
        employee_id,
        session_id
    )
)
