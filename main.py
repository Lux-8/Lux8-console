import security
import console

def main():
    login = security.int_user_login()
    password = security.int_password(login)
    access = security.check_keys(password, login)
    console.console(login, access)

if __name__ == "__main__":
    main()
