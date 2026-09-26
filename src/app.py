def process_transaction(user_data):
    user_id = user_data.get("user_id")
    # Bug: Will crash if 'amount' is missing
    amount = user_data["amount"] 
    return {"status": "success", "user_id": user_id, "amount": amount}
