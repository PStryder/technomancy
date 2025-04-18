# signalkeeper_setup.py

def run_signalkeeper_setup():
    print("📡 Signalkeeper AE Profile Setup")
    ae_name = input("Your full name: ")
    ae_email = input("Your work email: ")
    territory_focus = input("Territory or agency focus (e.g., FL state, DoD, Fed Civilian): ")
    typical deal size = input("Typical deal size or range (e.g., $80K–$250K): ")
    primary products sold = input("Primary product focus (e.g., Records, Cloud Backup, EnPower): ")

    thread_style = input("How do you prefer to drop deals? (1) Raw email threads, (2) Bullet summaries, (3) Call notes, (4) Mixed: ")

    print("\n✅ Setup complete. Signalkeeper will now parse your inputs in this format:")
    print(f"- AE: {ae_name} ({ae_email})")
    print(f"- Focus: {territory_focus}")
    print(f"- Product: {primary_products_sold}")
    print(f"- Deal Size: {typical_deal_size}")
    print(f"- Preferred Input: {thread_style}")
    print("\nUse this profile to accelerate scoring and insight generation.")

run_signalkeeper_setup()
