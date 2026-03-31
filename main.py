from analyzer import PasswordAnalyzer

def get_rating(score):
    if score >= 65: return "⭐⭐⭐⭐⭐ (Strong)"
    if score >= 40: return "⭐⭐⭐ (Moderate)"
    return "⭐ (Weak/Risk)"

def main():
    print("--- AI Password Risk Shield ---")
    engine = PasswordAnalyzer()
    
    while True:
        pwd = input("\nEnter password to test : ").strip()
        if pwd.lower() == 'exit': break
        if not pwd: continue

        score, tips = engine.analyze(pwd)
        
        print(f"Risk Score: {score}")
        print(f"Security Level: {get_rating(score)}")
        for tip in tips:
            print(f" -> {tip}")

if __name__ == "__main__":
    main()
