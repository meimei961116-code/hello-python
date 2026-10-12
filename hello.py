from datetime import date

def main():
    today = date.today()
    intro = (
        f"Hello! I am Antigravity, an agentic AI coding assistant from Google DeepMind.\n"
        f"Today is {today}, ready to pair program with you!"
    )
    print(intro)

if __name__ == "__main__":
    main()
