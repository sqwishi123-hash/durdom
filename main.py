def check_password_strength(password):
    if len(password) < 8:
        print("Пароль слишком короткий! Нужно минимум 8 символов.")
        return
    elif not re.search(r"\d", password):
        print("Добавьте хотя бы одну цифру.")
    elif not re.search(r"[A-Z]", password):
        print("Добавьте хотя бы одну заглавную букву.")
    else:
        print("Отличный пароль!")